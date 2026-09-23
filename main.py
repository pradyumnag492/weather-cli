import requests
import argparse
import json

parser = argparse.ArgumentParser()

parser.add_argument("city", type=str, help="enter your city")
parser.add_argument("country", type=str, help="enter your country, full country name")
parser.add_argument("-tu", "--temp_unit", type=str, default="fahrenheit", choices=["celsius", "fahrenheit"], help="enter your preferred temperature unit, celsius or fahrenheit")
parser.add_argument("-wsu", "--wind_speed_unit", type=str, default="mph", choices=["kmh", "mph", "knots", "ms"], help="enter preferred wind speed unit")
parser.add_argument("-pru", "--precipitation_unit", type=str, default="inch", choices=["inch", "mm"], help="enter preferred precipitation unit")
parser.add_argument("-la", "--latitude", type=float, help="enter optional latitude")
parser.add_argument("-lo", "--longitude", type=float, help="enter optional longitude")
parser.add_argument("-d", "--days", type=int, default=3, choices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ,16], help="enter forecast length")

args = parser.parse_args()

if args.latitude is not None and args.longitude is not None:
    lat = args.latitude
    lon = args.longitude
elif args.city and args.country:
    params = {"name": f"{args.city}, {args.country}"}

    thing = requests.get(
        f"https://geocoding-api.open-meteo.com/v1/search", params=params
    )
    thing1 = thing.json()

    if "results" not in thing1:
        print(f"geocoding results for {args.city}, {args.country} not found")
        sys.exit(1)

    city = thing1["results"][0]
    lat = city["latitude"]
    lon = city["longitude"]

else:
    print(
        "Error: You must provide either 'city country' OR '-la LATITUDE -lo LONGITUDE'."
    )
    sys.exit(1)



thing1 = requests.get(f"https://geocoding-api.open-meteo.com/v1/search", params=params).json()
city = thing1["results"][0]
lat = city["latitude"]
lon = city["longitude"]

response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=weather_code,temperature_2m_min,temperature_2m_max,precipitation_probability_max,rain_sum,showers_sum,snowfall_sum,precipitation_sum&wind_speed_unit={args.wind_speed_unit}&temperature_unit={args.temp_unit}&precipitation_unit={args.precipitation_unit}").json()
print(response)
response2 = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=weather_code,temperature_2m_min,temperature_2m_max,precipitation_probability_max,rain_sum,showers_sum,snowfall_sum,precipitation_sum&wind_speed_unit={args.wind_speed_unit}&temperature_unit={args.temp_unit}&precipitation_unit={args.precipitation_unit}")
if response2.status_code == 200:
    print(f"Success! Weather for {args.city} found.")
else: print(f"Error {response.status_code}. Could not find weather for {args.city}, {args.country}")


