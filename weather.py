import requests
import os
from dotenv import load_dotenv
from datetime import datetime

# ==========================
# Weather App
# ==========================

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

try:
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        city_name = data["name"]
        country = data["sys"]["country"]

        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]

        weather = data["weather"][0]["main"]
        description = data["weather"][0]["description"]

        wind_speed = data["wind"]["speed"]

        sunrise = data["sys"]["sunrise"]
        sunset = data["sys"]["sunset"]

        sunrise_time = datetime.fromtimestamp(sunrise).strftime("%I:%M %p")
        sunset_time = datetime.fromtimestamp(sunset).strftime("%I:%M %p")

        print("\n========== WEATHER ==========")
        print(f"City        : {city_name}, {country}")
        print(f"Weather     : {weather}")
        print(f"Description : {description}")
        print(f"Temperature : {temperature} °C")
        print(f"Feels Like  : {feels_like} °C")
        print(f"Humidity    : {humidity}%")
        print(f"Pressure    : {pressure} hPa")
        print(f"Wind Speed  : {wind_speed} m/s")
        print(f"🌅 Sunrise   : {sunrise_time}")
        print(f"🌇 Sunset    : {sunset_time}")
        print("================================")
    else:
        print("City not found.")
except Exception as e:
    print("Error:", e)

