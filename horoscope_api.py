import requests

sign = input("Aries, Taurus, Gemini, Cancer, Leo, Virgo, Libra, Scorpio, Sagittarius, Capricorn, Aquarius, and Pisces\nZodiac sign: ")
date = input("Today, tomorrow, yesterday, date in format 2024-04-15: ")

base_url = "https://horoscope-app-api.vercel.app/api/v1/get-horoscope/daily"
response = requests.get(base_url + "?sign=" + sign + "&day=" + date)

print(response.json()['data']['horoscope_data'])