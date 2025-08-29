import requests
import os
from dotenv import load_dotenv

# Load variables from .env into environment
load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city: str):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    # Check if the response contains an error (e.g., city not found)
    if response.status_code != 200 or "main" not in data:
        return {"error": data.get("message", "Unable to retrieve weather data.")}

    return {
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"],
        "condition": data["weather"][0]["description"]
    }
