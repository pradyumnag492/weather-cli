import requests
import argparse
import json
import sys

parser = argparse.ArgumentParser()

parser.add_argument("-c", "--city", type=str, help="enter your city")
parser.add_argument("-co", "--country", type=str, help="enter your country, full country name")
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

    print("------------------------------------------------------------------------------")

    print(f"Success! Weather found.")



else: print(f"Error {response.status_code}. Could not find weather")
if "daily" in response and "time" in response["daily"] and len(response["daily"]["time"]) > 0:
    day1 = response["daily"]["time"][0]

if "daily" in response and "time" in response["daily"] and len(response["daily"]["time"]) > 1:
    day2 = response["daily"]["time"][1]

if "daily" in response and "time" in response["daily"] and len(response["daily"]["time"]) > 2:
    day3 = response["daily"]["time"][2]

if "daily" in response and "time" in response["daily"] and len(response["daily"]["time"]) > 3:
    day4 = response["daily"]["time"][3]

if "daily" in response and "time" in response["daily"] and len(response["daily"]["time"]) > 4:
    day5 = response["daily"]["time"][4]

if "daily" in response and "time" in response["daily"] and len(response["daily"]["time"]) > 5:
    day6 = response["daily"]["time"][5]

if "daily" in response and "time" in response["daily"] and len(response["daily"]["time"]) > 6:
    day7 = response["daily"]["time"][6]

if "daily" in response and "time" in response["daily"] and len(response["daily"]["time"]) > 7:
    day8 = response["daily"]["time"][7]

if "daily" in response and "time" in response["daily"] and len(response["daily"]["time"]) > 8:
    day9 = response["daily"]["time"][8]

if "daily" in response and "time" in response["daily"] and len(response["daily"]["time"]) > 9:
    day10 = response["daily"]["time"][9]

if "daily" in response and "time" in response["daily"] and len(response["daily"]["time"]) > 10:
    day11 = response["daily"]["time"][10]

if "daily" in response and "time" in response["daily"] and len(response["daily"]["time"]) > 11:
    day12 = response["daily"]["time"][11]

if "daily" in response and "time" in response["daily"] and len(response["daily"]["time"]) > 12:
    day13 = response["daily"]["time"][12]

if "daily" in response and "time" in response["daily"] and len(response["daily"]["time"]) > 13:
    day14 = response["daily"]["time"][13]

if "daily" in response and "time" in response["daily"] and len(response["daily"]["time"]) > 14:
    day15 = response["daily"]["time"][14]

if "daily" in response and "time" in response["daily"] and len(response["daily"]["time"]) > 15:
    day16 = response["daily"]["time"][15]

print("------------------------------------------------------------------------------")

counter = 0






for codes in response["daily"]["weather_code"]:
    if codes is not None:
        counter += 1
        if counter == 1:
            nvar = day1
        if counter == 2:
            nvar = day2
        if counter == 3:
            nvar = day3
        if counter == 4:
            nvar = day4
        if counter == 5:
            nvar = day5
        if counter == 6:
            nvar = day6
        if counter == 7:
            nvar = day7
        if counter == 8:
            nvar = day8
        if counter == 9:
            nvar = day9
        if counter == 10:
            nvar = day10
        if counter == 11:
            nvar = day11
        if counter == 12:
            nvar = day12
        if counter == 13:
            nvar = day13
        if counter == 14:
            nvar = day14
        if counter == 15:
            nvar = day15
        if counter == 16:
            nvar = day16

        if codes == 0:

            print(f"weather for day {nvar}: Clear skies.")
            if counter == {args.days}:
                break
        if codes == 1:

            print(f"weather for day {nvar}: Mainly clear.")
            if counter == {args.days}:
                break
        if codes == 2:

            print(f"weather for day {nvar}: Partly cloudy.")
            if counter == {args.days}:
                break
        if codes == 3:

            print(f"weather for day {nvar}: Overcast.")
            if counter == {args.days}:
                break
        if codes == 45:

            print(f"weather for day {nvar}: Fog.")
            if counter == {args.days}:
                break
        if codes == 48:

            print(f"weather for day {nvar}: Depositing rime fog.")
            if counter == {args.days}:
                break
        if codes == 51:

            print(f"weather for day {nvar}: Light drizzle.")
            if counter == {args.days}:
                break
        if codes == 53:

            print(f"weather for day {nvar}: Moderate drizzle.")
            if counter == {args.days}:
                break
        if codes == 55:

            print(f"weather for day {nvar}: Dense drizzle.")
            if counter == {args.days}:
                break
        if codes == 56:

            print(f"weather for day {nvar}: Light freezing drizzle.")
            if counter == {args.days}:
                break
        if codes == 57:

            print(f"weather for day {nvar}: Dense freezing drizzle.")
            if counter == {args.days}:
                break
        if codes == 61:

            print(f"weather for day {nvar}: Slight rain.")
            if counter == {args.days}:
                break
        if codes == 63:

            print(f"weather for day {nvar}: Moderate rain.")
            if counter == {args.days}:
                break
        if codes == 65:

            print(f"weather for day {nvar}: Heavy rain.")
            if counter == {args.days}:
                break
        if codes == 66:

            print(f"weather for day {nvar}: Light freezing rain.")
            if counter == {args.days}:
                break
        if codes == 67:

            print(f"weather for day {nvar}: Heavy freezing rain.")
            if counter == {args.days}:
                break
        if codes == 71:

            print(f"weather for day {nvar}: Slight snowfall.")
            if counter == {args.days}:
                break
        if codes == 73:

            print(f"weather for day {nvar}: Moderate snowfall.")
            if counter == {args.days}:
                break
        if codes == 75:

            print(f"weather for day {nvar}: Heavy snowfall.")
            if counter == {args.days}:
                break
        if codes == 77:

            print(f"weather for day {nvar}: Snow grains.")
            if counter == {args.days}:
                break
        if codes == 80:

            print(f"weather for day {nvar}: Slight rain showers.")
            if counter == {args.days}:
                break
        if codes == 81:

            print(f"weather for day {nvar}: Moderate rain showers.")
            if counter == {args.days}:
                break
        if codes == 82:

            print(f"weather for day {nvar}: Violent rain showers.")
            if counter == {args.days}:
                break
        if codes == 85:

            print(f"weather for day {nvar}: Slight snow showers.")
            if counter == {args.days}:
                break
        if codes == 86:

            print(f"weather for day {nvar}: Heavy snow showers.")
            if counter == {args.days}:
                break
        if codes == 95:

            print(f"weather for day {nvar}: Thunderstorm.")
            if counter == {args.days}:
                break
        if codes == 96:

            print(f"weather for day {nvar}: Thunderstorm with slight hail.")
            if counter == {args.days}:
                break
        if codes == 99:

            print(f"weather for day {nvar}: Thunderstorm with heavy hail.")
            if counter == {args.days}:
                break
print("------------------------------------------------------------------------------")

#i have to admit: this part was made by ai. 
# i tried to fix it myself but i just couldn't fucking understand.
#i caved, but i made it explain each step to me so at least i understood the code instead of blindly copy pasting
# im so fucking sorry
# im weak

countt = 0

for temps1 in response["daily"]["temperature_2m_max"]:
    if temps1 is not None:
        countt += 1
        if countt == 1:
            mvar = day1
        if countt == 2:
            mvar = day2
        if countt == 3:
            mvar = day3
        if countt == 4:
            mvar = day4
        if countt == 5:
            mvar = day5
        if countt == 6:
            mvar = day6
        if countt == 7:
            mvar = day7
        if countt == 8:
            mvar = day8
        if countt == 9:
            mvar = day9
        if countt == 10:
            mvar = day10
        if countt == 11:
            mvar = day11
        if countt == 12:
            mvar = day12
        if countt == 13:
            mvar = day13
        if countt == 14:
            mvar = day14
        if countt == 15:
            mvar = day15
        if countt == 16:
            mvar = day16



    temps = response["daily"]["temperature_2m_min"][countt - 1]
    if temps is not None:

        print(f"({args.temp_unit}) Minimum and maximum 2 meter temperatures for Day {mvar}: {temps} and {temps1} {args.temp_unit}")
        if countt == args.days:
            break

print("------------------------------------------------------------------------------") 
l = 0
for probs in response["daily"]["precipitation_probability_max"]:
    if probs is not None:
        l += 1
        if l == 1:
            e = day1
        if l == 2:
            e = day2
        if l == 3:
            e = day3
        if l == 4:
            e = day4
        if l == 5:
            e = day5
        if l == 6:
            e = day6
        if l == 7:
            e = day7
        if l == 8:
            e = day8
        if l == 9:
            e = day9
        if l == 10:
            e = day10
        if l == 11:
            e = day11
        if l == 12:
            e = day12
        if l == 13:
            e = day13
        if l == 14:
            e = day14
        if l == 15:
            e = day15
        if l == 16:
            e = day16

        print(f"Precipitation probabilities for Day {e} is {probs} %.")

print("------------------------------------------------------------------------------") 
l = 0
for sums in response["daily"]["rain_sum"]:
    if sums is not None:
        l += 1
        if l == 1:
            e = day1
        if l == 2:
            e = day2
        if l == 3:
            e = day3
        if l == 4:
            e = day4
        if l == 5:
            e = day5
        if l == 6:
            e = day6
        if l == 7:
            e = day7
        if l == 8:
            e = day8
        if l == 9:
            e = day9
        if l == 10:
            e = day10
        if l == 11:
            e = day11
        if l == 12:
            e = day12
        if l == 13:
            e = day13
        if l == 14:
            e = day14
        if l == 15:
            e = day15
        if l == 16:
            e = day16

        print(f"({args.precipitation_unit}) Rain sum Day {e} is {sums} {args.precipitation_unit}.")
print("------------------------------------------------------------------------------") 
l = 0
for sumss in response["daily"]["showers_sum"]:
    if sumss is not None:
        l += 1
        if l == 1:
            e = day1
        if l == 2:
            e = day2
        if l == 3:
            e = day3
        if l == 4:
            e = day4
        if l == 5:
            e = day5
        if l == 6:
            e = day6
        if l == 7:
            e = day7
        if l == 8:
            e = day8
        if l == 9:
            e = day9
        if l == 10:
            e = day10
        if l == 11:
            e = day11
        if l == 12:
            e = day12
        if l == 13:
            e = day13
        if l == 14:
            e = day14
        if l == 15:
            e = day15
        if l == 16:
            e = day16

        print(f"({args.precipitation_unit}) Showers sum Day {e} is {sumss} {args.precipitation_unit}.")

print("------------------------------------------------------------------------------") 

l = 0

for sumsss in response["daily"]["snowfall_sum"]:
    if sumsss is not None:
        l += 1
        if l == 1:
            e = day1
        if l == 2:
            e = day2
        if l == 3:
            e = day3
        if l == 4:
            e = day4
        if l == 5:
            e = day5
        if l == 6:
            e = day6
        if l == 7:
            e = day7
        if l == 8:
            e = day8
        if l == 9:
            e = day9
        if l == 10:
            e = day10
        if l == 11:
            e = day11
        if l == 12:
            e = day12
        if l == 13:
            e = day13
        if l == 14:
            e = day14
        if l == 15:
            e = day15
        if l == 16:
            e = day16

        print(f"({args.precipitation_unit}) Snowfall sum Day {e} is {sumsss} {args.precipitation_unit}.")
print("------------------------------------------------------------------------------") 
l = 0

for sumssss in response["daily"]["precipitation_sum"]:
    if sumssss is not None:
        l += 1
        if l == 1:
            e = day1
        if l == 2:
            e = day2
        if l == 3:
            e = day3
        if l == 4:
            e = day4
        if l == 5:
            e = day5
        if l == 6:
            e = day6
        if l == 7:
            e = day7
        if l == 8:
            e = day8
        if l == 9:
            e = day9
        if l == 10:
            e = day10
        if l == 11:
            e = day11
        if l == 12:
            e = day12
        if l == 13:
            e = day13
        if l == 14:
            e = day14
        if l == 15:
            e = day15
        if l == 16:
            e = day16

        print(f"({args.precipitation_unit}) Precipitation sum Day {e} is {sumssss} {args.precipitation_unit}.")
print("------------------------------------------------------------------------------") 



