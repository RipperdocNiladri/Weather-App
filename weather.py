# Imports
import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

# ==========================
# Weather App
# ==========================

# Configuration
load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

# Constants (weather_icons)
weather_icons = {
    "Clear": "☀️",
    "Clouds": "☁️",
    "Rain": "🌧️",
    "Drizzle": "🌦️",
    "Thunderstorm": "⛈️",
    "Snow": "❄️",
    "Mist": "༄.°",
    "Fog": "🌫",
    "Haze": "･༄",
    "Smoke": "💨"
}

# User Input
while True:
    
    city = input("Enter city name: ")

# API Request
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

# Data Processing
    try:
        response = requests.get(url)
        data = response.json()
        current_time = datetime.now()

        timezone_offset = data["timezone"]
        utc_time = datetime.utcnow()
        local_time = utc_time + timedelta(seconds=timezone_offset)

        if response.status_code == 200:
            city_name = data["name"]
            country = data["sys"]["country"]

            latitude = data["coord"]["lat"]
            longitude = data["coord"]["lon"]

            temperature = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            humidity = data["main"]["humidity"]
            pressure = data["main"]["pressure"]
            visibility = data["visibility"] / 1000
            clouds = data["clouds"]["all"]
            wind_degree = data["wind"]["deg"]

            weather = data["weather"][0]["main"]
            description = data["weather"][0]["description"]
            icon = weather_icons.get(weather, "🌍")

            wind_speed = data["wind"]["speed"]

            formatted_date = current_time.strftime("%d %B %Y")
            formatted_time = current_time.strftime("%I:%M:%S %p")

            location_date = local_time.strftime("%d %B %Y")
            location_time = local_time.strftime("%I:%M:%S %p")

            sunrise = data["sys"]["sunrise"]
            sunset = data["sys"]["sunset"]

            sunrise_time = datetime.fromtimestamp(sunrise).strftime("%I:%M %p")
            sunset_time = datetime.fromtimestamp(sunset).strftime("%I:%M %p")

# Output
            print("╔════════════════════════════════════════════╗")
            print("             ⛅ WEATHER REPORT                ")
            print("╚════════════════════════════════════════════╝")
            
            print(f"📅 Your Date   : {formatted_date}")
            print(f"🕒 Your Time   : {formatted_time}")

            print("-" * 40)

            print(f"📅 {city_name} Date : {location_date}")
            print(f"🕒 {city_name} Time : {location_time}")

            print("-" * 40)
            
            print(f"📍 City          : {city_name}, {country}")
            print(f"🌐 Coordinates   : {latitude}, {longitude}")
            print(f"🌍 Weather       : {weather} {icon}")
            print(f"📝 Description   : {description}")
            print(f"🌡️ Temperature    : {temperature} °C")
            print(f"🥵 Feels Like    : {feels_like} °C")
            print(f"💧 Humidity      : {humidity}%")
            print(f"🎈 Pressure      : {pressure} hPa")
            print(f"💨 Wind Speed    : {wind_speed} m/s")
            print(f"🧭 Wint dir.     : {wind_degree}°")
            print(f"☁️  Clouds        : {clouds}%")
            print(f"👁️  Visibility    : {visibility} km")
            print(f"🌅 Sunrise       : {sunrise_time}")
            print(f"🌇 Sunset        : {sunset_time}")
            print("═" * 40)
        else:
            print("City not found.")
    except Exception as e:
        print("Error:", e)

    again = input("\nsearch another city? (y/n): ").lower()

    if again !="y":
        print("\nThanks for using weather app!")
        break


