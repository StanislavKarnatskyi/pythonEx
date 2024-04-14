import requests

city = input("City: ")


api_key = ''
base_url = 'https://api.openweathermap.org/data/2.5/weather?'

response = requests.get(base_url + 'q=' + city + '&appid=' + api_key)

kelvin = response.json()['main']['temp']
celsium = int(round(kelvin - 273.15, 0))


humidity = response.json()['main']['humidity']
wind_speed = response.json()['wind']['speed']
weather_desc = response.json()['weather'][0]['description']

print(f"In {city} current temperature {celsium}°C, and weather {weather_desc}.\nHumidity {humidity}. Current wind speed {wind_speed}m/s")
