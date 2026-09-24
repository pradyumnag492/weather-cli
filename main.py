import requests
import argparse
import json
import sys

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
        f"https://geocoding-api.open-meteo.com/v1/search", params=params)
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



response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=weather_code,temperature_2m_min,temperature_2m_max,precipitation_probability_max,rain_sum,showers_sum,snowfall_sum,precipitation_sum&wind_speed_unit={args.wind_speed_unit}&temperature_unit={args.temp_unit}&precipitation_unit={args.precipitation_unit}&forecast_days={args.days}").json()
thing = json.loads(response)


response2 = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=weather_code,temperature_2m_min,temperature_2m_max,precipitation_probability_max,rain_sum,showers_sum,snowfall_sum,precipitation_sum&wind_speed_unit={args.wind_speed_unit}&temperature_unit={args.temp_unit}&precipitation_unit={args.precipitation_unit}&forecast_days={args.days}")
if response2.status_code == 200:
    print(f"Success! Weather found.")
    print(response)
    
else: print(f"Error {response.status_code}. Could not find weather")


#holy shit this is inefficient
#oh shit i forgot index 0 because i forgot python indexes @ 1
#fixed lol
if response["daily"]["weather_code"][0] is not None:
    if response["daily"]["weather_code"][0] == 0:
        print("clear skies")
    if response["daily"]["weather_code"][0] == 1:
        print("mainly clear")
    if response["daily"]["weather_code"][0] == 2:
        print("partly cloudy")
    if response["daily"]["weather_code"][0] == 3:
        print("overcast")
    if response["daily"]["weather_code"][0] == 45:
        print("fog")
    if response["daily"]["weather_code"][0] == 48:
        print("depositing rime fog.")
    if response["daily"]["weather_code"][0] == 51:
        print("Light drizzle")
    if response["daily"]["weather_code"][0] == 53:
        print("moderate drizzle.")
    if response["daily"]["weather_code"][0] == 55:
        print("dense drizzle")
    if response["daily"]["weather_code"][0] == 56:
        print("light freeing drizzle.")
    if response["daily"]["weather_code"][0] == 57:
        print("Dense freezing drizzle")
    if response["daily"]["weather_code"][0] == 61:
        print("slight rain.")
    if response["daily"]["weather_code"][0] == 63:
        print("moderate rain.")
    if response["daily"]["weather_code"][0] == 65:
        print("heavy rain.")
    if response["daily"]["weather_code"][0] == 66:
        print("light freezing rain")
    if response["daily"]["weather_code"][0] == 67:
        print("heavy freezing rain")
    if response["daily"]["weather_code"][0] == 71:
        print("slight snow fall")
    if response["daily"]["weather_code"][0] == 73:
        print("moderate snowfall")
    if response["daily"]["weather_code"][0] == 75:
        print("heavy snowfall")
    if response["daily"]["weather_code"][0] == 77:
        print("snow grains")
    if response["daily"]["weather_code"][0] == 80:
        print("slight rain showers")
    if response["daily"]["weather_code"][0] == 81:
        print("moderate rain showers")
    if response["daily"]["weather_code"][0] == 82:
        print("Violent rain showers.")
    if response["daily"]["weather_code"][0] == 85:
        print("slight snow showers")
    if response["daily"]["weather_code"][0] == 86:
        print("heavy snow showers")
    if response["daily"]["weather_code"][0] == 95:
        print("thunderstorm")
    if response["daily"]["weather_code"][0] == 96:
        print("thunderstorm with slight hail")
    if response["daily"]["weather_code"][0] == 99:
        print("thunderstorm with heavy hail")


if response["daily"]["weather_code"][1]:
    if response["daily"]["weather_code"][1] == 0:
        print("clear skies")
    if response["daily"]["weather_code"][1] == 1:
        print("mainly clear")
    if response["daily"]["weather_code"][1] == 2:
         print("partly cloudy")
    if response["daily"]["weather_code"][1] == 3:
         print("overcast")
    if response["daily"]["weather_code"][1] == 45:
        print("fog")
    if response["daily"]["weather_code"][1] == 48:
        print("depositing rime fog.")
    if response["daily"]["weather_code"][1] == 51:
        print("Light drizzle")
    if response["daily"]["weather_code"][1] == 53:
        print("moderate drizzle.")
    if response["daily"]["weather_code"][1] == 55:
        print("dense drizzle")
    if response["daily"]["weather_code"][1] == 56:
        print("light freeing drizzle.")
    if response["daily"]["weather_code"][1] == 57:
        print("Dense freezing drizzle")
    if response["daily"]["weather_code"][1] == 61:
        print("slight rain.")
    if response["daily"]["weather_code"][1] == 63:
        print("moderate rain.")
    if response["daily"]["weather_code"][1] == 65:
        print("heavy rain.")
    if response["daily"]["weather_code"][1] == 66:
        print("light freezing rain")
    if response["daily"]["weather_code"][1] == 67:
        print("heavy freezing rain")
    if response["daily"]["weather_code"][1] == 71:
        "slight snow fall"
    if response["daily"]["weather_code"][1] == 73:
        "moderate snowfall"
    if response["daily"]["weather_code"][1] == 75:
        print("heavy snowfall")
    if response["daily"]["weather_code"][1] == 77:
        print("snow grains")
    if response["daily"]["weather_code"][1] == 80:
        print("slight rain showers")
    if response["daily"]["weather_code"][1] == 81:
        print("moderate rain showers")
    if response["daily"]["weather_code"][1] == 82:
        print("Violent rain showers.")
    if response["daily"]["weather_code"][1] == 85:
        print("slight snow showers")
    if response["daily"]["weather_code"][1] == 86:
        print("heavy snow showers")
    if response["daily"]["weather_code"][1] == 95:
        print("thunderstorm")
    if response["daily"]["weather_code"][1] == 96:
        print("thunderstorm with slight hail")
    if response["daily"]["weather_code"][1] == 99:
        print("thunderstorm with heavy hail")
        
if response["daily"]["weather_code"][2] is not None:
    if response["daily"]["weather_code"][2] == 0:
        print("clear skies")
    if response["daily"]["weather_code"][2] == 1:
        print("mainly clear")
    if response["daily"]["weather_code"][2] == 2:
        print("partly cloudy")
    if response["daily"]["weather_code"][2] == 3:
        print("overcast")
    if response["daily"]["weather_code"][2] == 45:
        print("fog")
    if response["daily"]["weather_code"][2] == 48:
        print("depositing rime fog.")
    if response["daily"]["weather_code"][2] == 51:
        print("Light drizzle")
    if response["daily"]["weather_code"][2] == 53:
        print("moderate drizzle.")
    if response["daily"]["weather_code"][2] == 55:
        print("dense drizzle")
    if response["daily"]["weather_code"][2] == 56:
        print("light freeing drizzle.")
    if response["daily"]["weather_code"][2] == 57:
        print("Dense freezing drizzle")
    if response["daily"]["weather_code"][2] == 61:
        print("slight rain.")
    if response["daily"]["weather_code"][2] == 63:
        print("moderate rain.")
    if response["daily"]["weather_code"][2] == 65:
        print("heavy rain.")
    if response["daily"]["weather_code"][2] == 66:
        print("light freezing rain")
    if response["daily"]["weather_code"][2] == 67:
        print("heavy freezing rain")
    if response["daily"]["weather_code"][2] == 71:
        print("slight snow fall")
    if response["daily"]["weather_code"][2] == 73:
        print("moderate snowfall")
    if response["daily"]["weather_code"][2] == 75:
        print("heavy snowfall")
    if response["daily"]["weather_code"][2] == 77:
        print("snow grains")
    if response["daily"]["weather_code"][2] == 80:
        print("slight rain showers")
    if response["daily"]["weather_code"][2] == 81:
        print("moderate rain showers")
    if response["daily"]["weather_code"][2] == 82:
        print("Violent rain showers.")
    if response["daily"]["weather_code"][2] == 85:
        print("slight snow showers")
    if response["daily"]["weather_code"][2] == 86:
        print("heavy snow showers")
    if response["daily"]["weather_code"][2] == 95:
        print("thunderstorm")
    if response["daily"]["weather_code"][2] == 96:
        print("thunderstorm with slight hail")
    if response["daily"]["weather_code"][2] == 99:
        print("thunderstorm with heavy hail")

if response["daily"]["weather_code"][3] is not None:
    if response["daily"]["weather_code"][3] == 0:
        print("clear skies")
    if response["daily"]["weather_code"][3] == 1:
        print("mainly clear")
    if response["daily"]["weather_code"][3] == 2:
        print("partly cloudy")
    if response["daily"]["weather_code"][3] == 3:
        print("overcast")
    if response["daily"]["weather_code"][3] == 45:
        print("fog")
    if response["daily"]["weather_code"][3] == 48:
        print("depositing rime fog.")
    if response["daily"]["weather_code"][3] == 51:
        print("Light drizzle")
    if response["daily"]["weather_code"][3] == 53:
        print("moderate drizzle.")
    if response["daily"]["weather_code"][3] == 55:
        print("dense drizzle")
    if response["daily"]["weather_code"][3] == 56:
        print("light freeing drizzle.")
    if response["daily"]["weather_code"][3] == 57:
        print("Dense freezing drizzle")
    if response["daily"]["weather_code"][3] == 61:
        print("slight rain.")
    if response["daily"]["weather_code"][3] == 63:
        print("moderate rain.")
    if response["daily"]["weather_code"][3] == 65:
        print("heavy rain.")
    if response["daily"]["weather_code"][3] == 66:
        print("light freezing rain")
    if response["daily"]["weather_code"][3] == 67:
        print("heavy freezing rain")
    if response["daily"]["weather_code"][3] == 71:
        print("slight snow fall")
    if response["daily"]["weather_code"][3] == 73:
        print("moderate snowfall")
    if response["daily"]["weather_code"][3] == 75:
        print("heavy snowfall")
    if response["daily"]["weather_code"][3] == 77:
        print("snow grains")
    if response["daily"]["weather_code"][3] == 80:
        print("slight rain showers")
    if response["daily"]["weather_code"][3] == 81:
        print("moderate rain showers")
    if response["daily"]["weather_code"][3] == 82:
        print("Violent rain showers.")
    if response["daily"]["weather_code"][3] == 85:
        print("slight snow showers")
    if response["daily"]["weather_code"][3] == 86:
        print("heavy snow showers")
    if response["daily"]["weather_code"][3] == 95:
        print("thunderstorm")
    if response["daily"]["weather_code"][3] == 96:
        print("thunderstorm with slight hail")
    if response["daily"]["weather_code"][3] == 99:
        print("thunderstorm with heavy hail")

if response["daily"]["weather_code"][4] is not None:
    if response["daily"]["weather_code"][4] == 0:
        print("clear skies")
    if response["daily"]["weather_code"][4] == 1:
        print("mainly clear")
    if response["daily"]["weather_code"][4] == 2:
        print("partly cloudy")
    if response["daily"]["weather_code"][4] == 3:
        print("overcast")
    if response["daily"]["weather_code"][4] == 45:
        print("fog")
    if response["daily"]["weather_code"][4] == 48:
        print("depositing rime fog.")
    if response["daily"]["weather_code"][4] == 51:
        print("Light drizzle")
    if response["daily"]["weather_code"][4] == 53:
        print("moderate drizzle.")
    if response["daily"]["weather_code"][4] == 55:
        print("dense drizzle")
    if response["daily"]["weather_code"][4] == 56:
        print("light freeing drizzle.")
    if response["daily"]["weather_code"][4] == 57:
        print("Dense freezing drizzle")
    if response["daily"]["weather_code"][4] == 61:
        print("slight rain.")
    if response["daily"]["weather_code"][4] == 63:
        print("moderate rain.")
    if response["daily"]["weather_code"][4] == 65:
        print("heavy rain.")
    if response["daily"]["weather_code"][4] == 66:
        print("light freezing rain")
    if response["daily"]["weather_code"][4] == 67:
        print("heavy freezing rain")
    if response["daily"]["weather_code"][4] == 71:
        print("slight snow fall")
    if response["daily"]["weather_code"][4] == 73:
        print("moderate snowfall")
    if response["daily"]["weather_code"][4] == 75:
        print("heavy snowfall")
    if response["daily"]["weather_code"][4] == 77:
        print("snow grains")
    if response["daily"]["weather_code"][4] == 80:
        print("slight rain showers")
    if response["daily"]["weather_code"][4] == 81:
        print("moderate rain showers")
    if response["daily"]["weather_code"][4] == 82:
        print("Violent rain showers.")
    if response["daily"]["weather_code"][4] == 85:
        print("slight snow showers")
    if response["daily"]["weather_code"][4] == 86:
        print("heavy snow showers")
    if response["daily"]["weather_code"][4] == 95:
        print("thunderstorm")
    if response["daily"]["weather_code"][4] == 96:
        print("thunderstorm with slight hail")
    if response["daily"]["weather_code"][4] == 99:
        print("thunderstorm with heavy hail")

if response["daily"]["weather_code"][5] is not None:
    if response["daily"]["weather_code"][5] == 0:
        print("clear skies")
    if response["daily"]["weather_code"][5] == 1:
        print("mainly clear")
    if response["daily"]["weather_code"][5] == 2:
        print("partly cloudy")
    if response["daily"]["weather_code"][5] == 3:
        print("overcast")
    if response["daily"]["weather_code"][5] == 45:
        print("fog")
    if response["daily"]["weather_code"][5] == 48:
        print("depositing rime fog.")
    if response["daily"]["weather_code"][5] == 51:
        print("Light drizzle")
    if response["daily"]["weather_code"][5] == 53:
        print("moderate drizzle.")
    if response["daily"]["weather_code"][5] == 55:
        print("dense drizzle")
    if response["daily"]["weather_code"][5] == 56:
        print("light freeing drizzle.")
    if response["daily"]["weather_code"][5] == 57:
        print("Dense freezing drizzle")
    if response["daily"]["weather_code"][5] == 61:
        print("slight rain.")
    if response["daily"]["weather_code"][5] == 63:
        print("moderate rain.")
    if response["daily"]["weather_code"][5] == 65:
        print("heavy rain.")
    if response["daily"]["weather_code"][5] == 66:
        print("light freezing rain")
    if response["daily"]["weather_code"][5] == 67:
        print("heavy freezing rain")
    if response["daily"]["weather_code"][5] == 71:
        print("slight snow fall")
    if response["daily"]["weather_code"][5] == 73:
        print("moderate snowfall")
    if response["daily"]["weather_code"][5] == 75:
        print("heavy snowfall")
    if response["daily"]["weather_code"][5] == 77:
        print("snow grains")
    if response["daily"]["weather_code"][5] == 80:
        print("slight rain showers")
    if response["daily"]["weather_code"][5] == 81:
        print("moderate rain showers")
    if response["daily"]["weather_code"][5] == 82:
        print("Violent rain showers.")
    if response["daily"]["weather_code"][5] == 85:
        print("slight snow showers")
    if response["daily"]["weather_code"][5] == 86:
        print("heavy snow showers")
    if response["daily"]["weather_code"][5] == 95:
        print("thunderstorm")
    if response["daily"]["weather_code"][5] == 96:
        print("thunderstorm with slight hail")
    if response["daily"]["weather_code"][5] == 99:
        print("thunderstorm with heavy hail")

if response["daily"]["weather_code"][6] is not None:
    if response["daily"]["weather_code"][6] == 0:
        print("clear skies")
    if response["daily"]["weather_code"][6] == 1:
        print("mainly clear")
    if response["daily"]["weather_code"][6] == 2:
        print("partly cloudy")
    if response["daily"]["weather_code"][6] == 3:
        print("overcast")
    if response["daily"]["weather_code"][6] == 45:
        print("fog")
    if response["daily"]["weather_code"][6] == 48:
        print("depositing rime fog.")
    if response["daily"]["weather_code"][6] == 51:
        print("Light drizzle")
    if response["daily"]["weather_code"][6] == 53:
        print("moderate drizzle.")
    if response["daily"]["weather_code"][6] == 55:
        print("dense drizzle")
    if response["daily"]["weather_code"][6] == 56:
        print("light freeing drizzle.")
    if response["daily"]["weather_code"][6] == 57:
        print("Dense freezing drizzle")
    if response["daily"]["weather_code"][6] == 61:
        print("slight rain.")
    if response["daily"]["weather_code"][6] == 63:
        print("moderate rain.")
    if response["daily"]["weather_code"][6] == 65:
        print("heavy rain.")
    if response["daily"]["weather_code"][6] == 66:
        print("light freezing rain")
    if response["daily"]["weather_code"][6] == 67:
        print("heavy freezing rain")
    if response["daily"]["weather_code"][6] == 71:
        print("slight snow fall")
    if response["daily"]["weather_code"][6] == 73:
        print("moderate snowfall")
    if response["daily"]["weather_code"][6] == 75:
        print("heavy snowfall")
    if response["daily"]["weather_code"][6] == 77:
        print("snow grains")
    if response["daily"]["weather_code"][6] == 80:
        print("slight rain showers")
    if response["daily"]["weather_code"][6] == 81:
        print("moderate rain showers")
    if response["daily"]["weather_code"][6] == 82:
        print("Violent rain showers.")
    if response["daily"]["weather_code"][6] == 85:
        print("slight snow showers")
    if response["daily"]["weather_code"][6] == 86:
        print("heavy snow showers")
    if response["daily"]["weather_code"][6] == 95:
        print("thunderstorm")
    if response["daily"]["weather_code"][6] == 96:
        print("thunderstorm with slight hail")
    if response["daily"]["weather_code"][6] == 99:
        print("thunderstorm with heavy hail")

if response["daily"]["weather_code"][7] is not None:
    if response["daily"]["weather_code"][7] == 0:
        print("clear skies")
    if response["daily"]["weather_code"][7] == 1:
        print("mainly clear")
    if response["daily"]["weather_code"][7] == 2:
        print("partly cloudy")
    if response["daily"]["weather_code"][7] == 3:
        print("overcast")
    if response["daily"]["weather_code"][7] == 45:
        print("fog")
    if response["daily"]["weather_code"][7] == 48:
        print("depositing rime fog.")
    if response["daily"]["weather_code"][7] == 51:
        print("Light drizzle")
    if response["daily"]["weather_code"][7] == 53:
        print("moderate drizzle.")
    if response["daily"]["weather_code"][7] == 55:
        print("dense drizzle")
    if response["daily"]["weather_code"][7] == 56:
        print("light freeing drizzle.")
    if response["daily"]["weather_code"][7] == 57:
        print("Dense freezing drizzle")
    if response["daily"]["weather_code"][7] == 61:
        print("slight rain.")
    if response["daily"]["weather_code"][7] == 63:
        print("moderate rain.")
    if response["daily"]["weather_code"][7] == 65:
        print("heavy rain.")
    if response["daily"]["weather_code"][7] == 66:
        print("light freezing rain")
    if response["daily"]["weather_code"][7] == 67:
        print("heavy freezing rain")
    if response["daily"]["weather_code"][7] == 71:
        print("slight snow fall")
    if response["daily"]["weather_code"][7] == 73:
        print("moderate snowfall")
    if response["daily"]["weather_code"][7] == 75:
        print("heavy snowfall")
    if response["daily"]["weather_code"][7] == 77:
        print("snow grains")
    if response["daily"]["weather_code"][7] == 80:
        print("slight rain showers")
    if response["daily"]["weather_code"][7] == 81:
        print("moderate rain showers")
    if response["daily"]["weather_code"][7] == 82:
        print("Violent rain showers.")
    if response["daily"]["weather_code"][7] == 85:
        print("slight snow showers")
    if response["daily"]["weather_code"][7] == 86:
        print("heavy snow showers")
    if response["daily"]["weather_code"][7] == 95:
        print("thunderstorm")
    if response["daily"]["weather_code"][7] == 96:
        print("thunderstorm with slight hail")
    if response["daily"]["weather_code"][7] == 99:
        print("thunderstorm with heavy hail")

if response["daily"]["weather_code"][8] is not None:
    if response["daily"]["weather_code"][8] == 0:
        print("clear skies")
    if response["daily"]["weather_code"][8] == 1:
        print("mainly clear")
    if response["daily"]["weather_code"][8] == 2:
        print("partly cloudy")
    if response["daily"]["weather_code"][8] == 3:
        print("overcast")
    if response["daily"]["weather_code"][8] == 45:
        print("fog")
    if response["daily"]["weather_code"][8] == 48:
        print("depositing rime fog.")
    if response["daily"]["weather_code"][8] == 51:
        print("Light drizzle")
    if response["daily"]["weather_code"][8] == 53:
        print("moderate drizzle.")
    if response["daily"]["weather_code"][8] == 55:
        print("dense drizzle")
    if response["daily"]["weather_code"][8] == 56:
        print("light freeing drizzle.")
    if response["daily"]["weather_code"][8] == 57:
        print("Dense freezing drizzle")
    if response["daily"]["weather_code"][8] == 61:
        print("slight rain.")
    if response["daily"]["weather_code"][8] == 63:
        print("moderate rain.")
    if response["daily"]["weather_code"][8] == 65:
        print("heavy rain.")
    if response["daily"]["weather_code"][8] == 66:
        print("light freezing rain")
    if response["daily"]["weather_code"][8] == 67:
        print("heavy freezing rain")
    if response["daily"]["weather_code"][8] == 71:
        print("slight snow fall")
    if response["daily"]["weather_code"][8] == 73:
        print("moderate snowfall")
    if response["daily"]["weather_code"][8] == 75:
        print("heavy snowfall")
    if response["daily"]["weather_code"][8] == 77:
        print("snow grains")
    if response["daily"]["weather_code"][8] == 80:
        print("slight rain showers")
    if response["daily"]["weather_code"][8] == 81:
        print("moderate rain showers")
    if response["daily"]["weather_code"][8] == 82:
        print("Violent rain showers.")
    if response["daily"]["weather_code"][8] == 85:
        print("slight snow showers")
    if response["daily"]["weather_code"][8] == 86:
        print("heavy snow showers")
    if response["daily"]["weather_code"][8] == 95:
        print("thunderstorm")
    if response["daily"]["weather_code"][8] == 96:
        print("thunderstorm with slight hail")
    if response["daily"]["weather_code"][8] == 99:
        print("thunderstorm with heavy hail")


if response["daily"]["weather_code"][9] is not None:
    if response["daily"]["weather_code"][9] == 0:
        print("clear skies")
    if response["daily"]["weather_code"][9] == 1:
        print("mainly clear")
    if response["daily"]["weather_code"][9] == 2:
        print("partly cloudy")
    if response["daily"]["weather_code"][9] == 3:
        print("overcast")
    if response["daily"]["weather_code"][9] == 45:
        print("fog")
    if response["daily"]["weather_code"][9] == 48:
        print("depositing rime fog.")
    if response["daily"]["weather_code"][9] == 51:
        print("Light drizzle")
    if response["daily"]["weather_code"][9] == 53:
        print("moderate drizzle.")
    if response["daily"]["weather_code"][9] == 55:
        print("dense drizzle")
    if response["daily"]["weather_code"][9] == 56:
        print("light freeing drizzle.")
    if response["daily"]["weather_code"][9] == 57:
        print("Dense freezing drizzle")
    if response["daily"]["weather_code"][9] == 61:
        print("slight rain.")
    if response["daily"]["weather_code"][9] == 63:
        print("moderate rain.")
    if response["daily"]["weather_code"][9] == 65:
        print("heavy rain.")
    if response["daily"]["weather_code"][9] == 66:
        print("light freezing rain")
    if response["daily"]["weather_code"][9] == 67:
        print("heavy freezing rain")
    if response["daily"]["weather_code"][9] == 71:
        print("slight snow fall")
    if response["daily"]["weather_code"][9] == 73:
        print("moderate snowfall")
    if response["daily"]["weather_code"][9] == 75:
        print("heavy snowfall")
    if response["daily"]["weather_code"][9] == 77:
        print("snow grains")
    if response["daily"]["weather_code"][9] == 80:
        print("slight rain showers")
    if response["daily"]["weather_code"][9] == 81:
        print("moderate rain showers")
    if response["daily"]["weather_code"][9] == 82:
        print("Violent rain showers.")
    if response["daily"]["weather_code"][9] == 85:
        print("slight snow showers")
    if response["daily"]["weather_code"][9] == 86:
        print("heavy snow showers")
    if response["daily"]["weather_code"][9] == 95:
        print("thunderstorm")
    if response["daily"]["weather_code"][9] == 96:
        print("thunderstorm with slight hail")
    if response["daily"]["weather_code"][9] == 99:
        print("thunderstorm with heavy hail")


if response["daily"]["weather_code"][10] is not None:
    if response["daily"]["weather_code"][10] == 0:
        print("clear skies")
    if response["daily"]["weather_code"][10] == 1:
        print("mainly clear")
    if response["daily"]["weather_code"][10] == 2:
        print("partly cloudy")
    if response["daily"]["weather_code"][10] == 3:
        print("overcast")
    if response["daily"]["weather_code"][10] == 45:
        print("fog")
    if response["daily"]["weather_code"][10] == 48:
        print("depositing rime fog.")
    if response["daily"]["weather_code"][10] == 51:
        print("Light drizzle")
    if response["daily"]["weather_code"][10] == 53:
        print("moderate drizzle.")
    if response["daily"]["weather_code"][10] == 55:
        print("dense drizzle")
    if response["daily"]["weather_code"][10] == 56:
        print("light freeing drizzle.")
    if response["daily"]["weather_code"][10] == 57:
        print("Dense freezing drizzle")
    if response["daily"]["weather_code"][10] == 61:
        print("slight rain.")
    if response["daily"]["weather_code"][10] == 63:
        print("moderate rain.")
    if response["daily"]["weather_code"][10] == 65:
        print("heavy rain.")
    if response["daily"]["weather_code"][10] == 66:
        print("light freezing rain")
    if response["daily"]["weather_code"][10] == 67:
        print("heavy freezing rain")
    if response["daily"]["weather_code"][10] == 71:
        print("slight snow fall")
    if response["daily"]["weather_code"][10] == 73:
        print("moderate snowfall")
    if response["daily"]["weather_code"][10] == 75:
        print("heavy snowfall")
    if response["daily"]["weather_code"][10] == 77:
        print("snow grains")
    if response["daily"]["weather_code"][10] == 80:
        print("slight rain showers")
    if response["daily"]["weather_code"][10] == 81:
        print("moderate rain showers")
    if response["daily"]["weather_code"][10] == 82:
        print("Violent rain showers.")
    if response["daily"]["weather_code"][10] == 85:
        print("slight snow showers")
    if response["daily"]["weather_code"][10] == 86:
        print("heavy snow showers")
    if response["daily"]["weather_code"][10] == 95:
        print("thunderstorm")
    if response["daily"]["weather_code"][10] == 96:
        print("thunderstorm with slight hail")
    if response["daily"]["weather_code"][10] == 99:
        print("thunderstorm with heavy hail")


if response["daily"]["weather_code"][11] is not None:
    if response["daily"]["weather_code"][11] == 0:
        print("clear skies")
    if response["daily"]["weather_code"][11] == 1:
        print("mainly clear")
    if response["daily"]["weather_code"][11] == 2:
        print("partly cloudy")
    if response["daily"]["weather_code"][11] == 3:
        print("overcast")
    if response["daily"]["weather_code"][11] == 45:
        print("fog")
    if response["daily"]["weather_code"][11] == 48:
        print("depositing rime fog.")
    if response["daily"]["weather_code"][11] == 51:
        print("Light drizzle")
    if response["daily"]["weather_code"][11] == 53:
        print("moderate drizzle.")
    if response["daily"]["weather_code"][11] == 55:
        print("dense drizzle")
    if response["daily"]["weather_code"][11] == 56:
        print("light freeing drizzle.")
    if response["daily"]["weather_code"][11] == 57:
        print("Dense freezing drizzle")
    if response["daily"]["weather_code"][11] == 61:
        print("slight rain.")
    if response["daily"]["weather_code"][11] == 63:
        print("moderate rain.")
    if response["daily"]["weather_code"][11] == 65:
        print("heavy rain.")
    if response["daily"]["weather_code"][11] == 66:
        print("light freezing rain")
    if response["daily"]["weather_code"][11] == 67:
        print("heavy freezing rain")
    if response["daily"]["weather_code"][11] == 71:
        print("slight snow fall")
    if response["daily"]["weather_code"][11] == 73:
        print("moderate snowfall")
    if response["daily"]["weather_code"][11] == 75:
        print("heavy snowfall")
    if response["daily"]["weather_code"][11] == 77:
        print("snow grains")
    if response["daily"]["weather_code"][11] == 80:
        print("slight rain showers")
    if response["daily"]["weather_code"][11] == 81:
        print("moderate rain showers")
    if response["daily"]["weather_code"][11] == 82:
        print("Violent rain showers.")
    if response["daily"]["weather_code"][11] == 85:
        print("slight snow showers")
    if response["daily"]["weather_code"][11] == 86:
        print("heavy snow showers")
    if response["daily"]["weather_code"][11] == 95:
        print("thunderstorm")
    if response["daily"]["weather_code"][11] == 96:
        print("thunderstorm with slight hail")
    if response["daily"]["weather_code"][11] == 99:
        print("thunderstorm with heavy hail")


if response["daily"]["weather_code"][12] is not None:
    if response["daily"]["weather_code"][12] == 0:
        print("clear skies")
    if response["daily"]["weather_code"][12] == 1:
        print("mainly clear")
    if response["daily"]["weather_code"][12] == 2:
        print("partly cloudy")
    if response["daily"]["weather_code"][12] == 3:
        print("overcast")
    if response["daily"]["weather_code"][12] == 45:
        print("fog")
    if response["daily"]["weather_code"][12] == 48:
        print("depositing rime fog.")
    if response["daily"]["weather_code"][12] == 51:
        print("Light drizzle")
    if response["daily"]["weather_code"][12] == 53:
        print("moderate drizzle.")
    if response["daily"]["weather_code"][12] == 55:
        print("dense drizzle")
    if response["daily"]["weather_code"][12] == 56:
        print("light freeing drizzle.")
    if response["daily"]["weather_code"][12] == 57:
        print("Dense freezing drizzle")
    if response["daily"]["weather_code"][12] == 61:
        print("slight rain.")
    if response["daily"]["weather_code"][12] == 63:
        print("moderate rain.")
    if response["daily"]["weather_code"][12] == 65:
        print("heavy rain.")
    if response["daily"]["weather_code"][12] == 66:
        print("light freezing rain")
    if response["daily"]["weather_code"][12] == 67:
        print("heavy freezing rain")
    if response["daily"]["weather_code"][12] == 71:
        print("slight snow fall")
    if response["daily"]["weather_code"][12] == 73:
        print("moderate snowfall")
    if response["daily"]["weather_code"][12] == 75:
        print("heavy snowfall")
    if response["daily"]["weather_code"][12] == 77:
        print("snow grains")
    if response["daily"]["weather_code"][12] == 80:
        print("slight rain showers")
    if response["daily"]["weather_code"][12] == 81:
        print("moderate rain showers")
    if response["daily"]["weather_code"][12] == 82:
        print("Violent rain showers.")
    if response["daily"]["weather_code"][12] == 85:
        print("slight snow showers")
    if response["daily"]["weather_code"][12] == 86:
        print("heavy snow showers")
    if response["daily"]["weather_code"][12] == 95:
        print("thunderstorm")
    if response["daily"]["weather_code"][12] == 96:
        print("thunderstorm with slight hail")
    if response["daily"]["weather_code"][12] == 99:
        print("thunderstorm with heavy hail")


if response["daily"]["weather_code"][13] is not None:
    if response["daily"]["weather_code"][13] == 0:
        print("clear skies")
    if response["daily"]["weather_code"][13] == 1:
        print("mainly clear")
    if response["daily"]["weather_code"][13] == 2:
        print("partly cloudy")
    if response["daily"]["weather_code"][13] == 3:
        print("overcast")
    if response["daily"]["weather_code"][13] == 45:
        print("fog")
    if response["daily"]["weather_code"][13] == 48:
        print("depositing rime fog.")
    if response["daily"]["weather_code"][13] == 51:
        print("Light drizzle")
    if response["daily"]["weather_code"][13] == 53:
        print("moderate drizzle.")
    if response["daily"]["weather_code"][13] == 55:
        print("dense drizzle")
    if response["daily"]["weather_code"][13] == 56:
        print("light freeing drizzle.")
    if response["daily"]["weather_code"][13] == 57:
        print("Dense freezing drizzle")
    if response["daily"]["weather_code"][13] == 61:
        print("slight rain.")
    if response["daily"]["weather_code"][13] == 63:
        print("moderate rain.")
    if response["daily"]["weather_code"][13] == 65:
        print("heavy rain.")
    if response["daily"]["weather_code"][13] == 66:
        print("light freezing rain")
    if response["daily"]["weather_code"][13] == 67:
        print("heavy freezing rain")
    if response["daily"]["weather_code"][13] == 71:
        print("slight snow fall")
    if response["daily"]["weather_code"][13] == 73:
        print("moderate snowfall")
    if response["daily"]["weather_code"][13] == 75:
        print("heavy snowfall")
    if response["daily"]["weather_code"][13] == 77:
        print("snow grains")
    if response["daily"]["weather_code"][13] == 80:
        print("slight rain showers")
    if response["daily"]["weather_code"][13] == 81:
        print("moderate rain showers")
    if response["daily"]["weather_code"][13] == 82:
        print("Violent rain showers.")
    if response["daily"]["weather_code"][13] == 85:
        print("slight snow showers")
    if response["daily"]["weather_code"][13] == 86:
        print("heavy snow showers")
    if response["daily"]["weather_code"][13] == 95:
        print("thunderstorm")
    if response["daily"]["weather_code"][13] == 96:
        print("thunderstorm with slight hail")
    if response["daily"]["weather_code"][13] == 99:
        print("thunderstorm with heavy hail")


if response["daily"]["weather_code"][14] is not None:
    if response["daily"]["weather_code"][14] == 0:
        print("clear skies")
    if response["daily"]["weather_code"][14] == 1:
        print("mainly clear")
    if response["daily"]["weather_code"][14] == 2:
        print("partly cloudy")
    if response["daily"]["weather_code"][14] == 3:
        print("overcast")
    if response["daily"]["weather_code"][14] == 45:
        print("fog")
    if response["daily"]["weather_code"][14] == 48:
        print("depositing rime fog.")
    if response["daily"]["weather_code"][14] == 51:
        print("Light drizzle")
    if response["daily"]["weather_code"][14] == 53:
        print("moderate drizzle.")
    if response["daily"]["weather_code"][14] == 55:
        print("dense drizzle")
    if response["daily"]["weather_code"][14] == 56:
        print("light freeing drizzle.")
    if response["daily"]["weather_code"][14] == 57:
        print("Dense freezing drizzle")
    if response["daily"]["weather_code"][14] == 61:
        print("slight rain.")
    if response["daily"]["weather_code"][14] == 63:
        print("moderate rain.")
    if response["daily"]["weather_code"][14] == 65:
        print("heavy rain.")
    if response["daily"]["weather_code"][14] == 66:
        print("light freezing rain")
    if response["daily"]["weather_code"][14] == 67:
        print("heavy freezing rain")
    if response["daily"]["weather_code"][14] == 71:
        print("slight snow fall")
    if response["daily"]["weather_code"][14] == 73:
        print("moderate snowfall")
    if response["daily"]["weather_code"][14] == 75:
        print("heavy snowfall")
    if response["daily"]["weather_code"][14] == 77:
        print("snow grains")
    if response["daily"]["weather_code"][14] == 80:
        print("slight rain showers")
    if response["daily"]["weather_code"][14] == 81:
        print("moderate rain showers")
    if response["daily"]["weather_code"][14] == 82:
        print("Violent rain showers.")
    if response["daily"]["weather_code"][14] == 85:
        print("slight snow showers")
    if response["daily"]["weather_code"][14] == 86:
        print("heavy snow showers")
    if response["daily"]["weather_code"][14] == 95:
        print("thunderstorm")
    if response["daily"]["weather_code"][14] == 96:
        print("thunderstorm with slight hail")
    if response["daily"]["weather_code"][14] == 99:
        print("thunderstorm with heavy hail")


if response["daily"]["weather_code"][15] is not None:
    if response["daily"]["weather_code"][15] == 0:
        print("clear skies")
    if response["daily"]["weather_code"][15] == 1:
        print("mainly clear")
    if response["daily"]["weather_code"][15] == 2:
        print("partly cloudy")
    if response["daily"]["weather_code"][15] == 3:
        print("overcast")
    if response["daily"]["weather_code"][15] == 45:
        print("fog")
    if response["daily"]["weather_code"][15] == 48:
        print("depositing rime fog.")
    if response["daily"]["weather_code"][15] == 51:
        print("Light drizzle")
    if response["daily"]["weather_code"][15] == 53:
        print("moderate drizzle.")
    if response["daily"]["weather_code"][15] == 55:
        print("dense drizzle")
    if response["daily"]["weather_code"][15] == 56:
        print("light freeing drizzle.")
    if response["daily"]["weather_code"][15] == 57:
        print("Dense freezing drizzle")
    if response["daily"]["weather_code"][15] == 61:
        print("slight rain.")
    if response["daily"]["weather_code"][15] == 63:
        print("moderate rain.")
    if response["daily"]["weather_code"][15] == 65:
        print("heavy rain.")
    if response["daily"]["weather_code"][15] == 66:
        print("light freezing rain")
    if response["daily"]["weather_code"][15] == 67:
        print("heavy freezing rain")
    if response["daily"]["weather_code"][15] == 71:
        print("slight snow fall")
    if response["daily"]["weather_code"][15] == 73:
        print("moderate snowfall")
    if response["daily"]["weather_code"][15] == 75:
        print("heavy snowfall")
    if response["daily"]["weather_code"][15] == 77:
        print("snow grains")
    if response["daily"]["weather_code"][15] == 80:
        print("slight rain showers")
    if response["daily"]["weather_code"][15] == 81:
        print("moderate rain showers")
    if response["daily"]["weather_code"][15] == 82:
        print("Violent rain showers.")
    if response["daily"]["weather_code"][15] == 85:
        print("slight snow showers")
    if response["daily"]["weather_code"][15] == 86:
        print("heavy snow showers")
    if response["daily"]["weather_code"][15] == 95:
        print("thunderstorm")
    if response["daily"]["weather_code"][15] == 96:
        print("thunderstorm with slight hail")
    if response["daily"]["weather_code"][15] == 99:
        print("thunderstorm with heavy hail")
    
    
     







