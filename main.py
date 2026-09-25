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



response2 = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=weather_code,temperature_2m_min,temperature_2m_max,precipitation_probability_max,rain_sum,showers_sum,snowfall_sum,precipitation_sum&wind_speed_unit={args.wind_speed_unit}&temperature_unit={args.temp_unit}&precipitation_unit={args.precipitation_unit}&forecast_days={args.days}")
if response2.status_code == 200:
    print(f"Success! Weather found.")
    print(response)

else: print(f"Error {response.status_code}. Could not find weather")









counter = 0





for codes in response["daily"]["weather_code"]:
    if codes is not None:
        if codes == 0:
            counter += 1
            print(f"weather for day {counter}: Clear skies.")
            if counter == {args.days}:
                break
        if codes == 1:
            counter += 1
            print(f"weather for day {counter}: Mainly clear.")
            if counter == {args.days}:
                break
        if codes == 2:
            counter += 1
            print(f"weather for day {counter}: Partly cloudy.")
            if counter == {args.days}:
                break
        if codes == 3:
            counter += 1
            print(f"weather for day {counter}: Overcast.")
            if counter == {args.days}:
                break
        if codes == 45:
            counter += 1
            print(f"weather for day {counter}: Fog.")
            if counter == {args.days}:
                break
        if codes == 48:
            counter += 1
            print(f"weather for day {counter}: Depositing rime fog.")
            if counter == {args.days}:
                break
        if codes == 51:
            counter += 1
            print(f"weather for day {counter}: Light drizzle.")
            if counter == {args.days}:
                break
        if codes == 53:
            counter += 1
            print(f"weather for day {counter}: Moderate drizzle.")
            if counter == {args.days}:
                break
        if codes == 55:
            counter += 1
            print(f"weather for day {counter}: Dense drizzle.")
            if counter == {args.days}:
                break
        if codes == 56:
            counter += 1
            print(f"weather for day {counter}: Light freezing drizzle.")
            if counter == {args.days}:
                break
        if codes == 57:
            counter += 1
            print(f"weather for day {counter}: Dense freezing drizzle.")
            if counter == {args.days}:
                break
        if codes == 61:
            counter += 1
            print(f"weather for day {counter}: Slight rain.")
            if counter == {args.days}:
                break
        if codes == 63:
            counter += 1
            print(f"weather for day {counter}: Moderate rain.")
            if counter == {args.days}:
                break
        if codes == 65:
            counter += 1
            print(f"weather for day {counter}: Heavy rain.")
            if counter == {args.days}:
                break
        if codes == 66:
            counter += 1
            print(f"weather for day {counter}: Light freezing rain.")
            if counter == {args.days}:
                break
        if codes == 67:
            counter += 1
            print(f"weather for day {counter}: Heavy freezing rain.")
            if counter == {args.days}:
                break
        if codes == 71:
            counter += 1
            print(f"weather for day {counter}: Slight snowfall.")
            if counter == {args.days}:
                break
        if codes == 73:
            counter += 1
            print(f"weather for day {counter}: Moderate snowfall.")
            if counter == {args.days}:
                break
        if codes == 75:
            counter += 1
            print(f"weather for day {counter}: Heavy snowfall.")
            if counter == {args.days}:
                break
        if codes == 77:
            counter += 1
            print(f"weather for day {counter}: Snow grains.")
            if counter == {args.days}:
                break
        if codes == 80:
            counter += 1
            print(f"weather for day {counter}: Slight rain showers.")
            if counter == {args.days}:
                break
        if codes == 81:
            counter += 1
            print(f"weather for day {counter}: Moderate rain showers.")
            if counter == {args.days}:
                break
        if codes == 82:
            counter += 1
            print(f"weather for day {counter}: Violent rain showers.")
            if counter == {args.days}:
                break
        if codes == 85:
            counter += 1
            print(f"weather for day {counter}: Slight snow showers.")
            if counter == {args.days}:
                break
        if codes == 86:
            counter += 1
            print(f"weather for day {counter}: Heavy snow showers.")
            if counter == {args.days}:
                break
        if codes == 95:
            counter += 1
            print(f"weather for day {counter}: Thunderstorm.")
            if counter == {args.days}:
                break
        if codes == 96:
            counter += 1
            print(f"weather for day {counter}: Thunderstorm with slight hail.")
            if counter == {args.days}:
                break
        if codes == 99:
            counter += 1
            print(f"weather for day {counter}: Thunderstorm with heavy hail.")
            if counter == {args.days}:
                break
print("------------------------------------------------------------------------------")

countt = 0
for temps1 in response["daily"]["temperature_2m_max"]:
    if temps1 is not None:
        countt += 1
        if countt == args.days:
            break

count = 0
for temps in response["daily"]["temperature_2m_min"]:
    if temps is not None:
        count += 1
        print(f"({args.temp_unit}) Minimum and maximum 2 meter temperatures for Day {count}: {temps} and {temps1} {args.temp_unit}")
        if count == args.days:
            break

print("------------------------------------------------------------------------------") 









