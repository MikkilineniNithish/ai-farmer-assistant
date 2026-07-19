import requests
import os
from dotenv import load_dotenv

load_dotenv(override=True)

def get_weather(city: str) -> dict:
    api_key = os.getenv("OPENWEATHER_API_KEY")

    # Check if city is GPS coordinates (lat,lon format)
    if "," in city and all(part.replace(".", "").replace("-", "").isdigit() for part in city.split(",")):
        lat, lon = city.split(",")
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    else:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city},IN&appid={api_key}&units=metric"

    response = requests.get(url)

    if response.status_code != 200:
        return {"error": f"Could not fetch weather. Status: {response.status_code}"}

    data = response.json()

    return {
        "city": data.get("name", city),
        "temperature_celsius": data["main"]["temp"],
        "humidity_percent": data["main"]["humidity"],
        "description": data["weather"][0]["description"],
        "wind_speed_mps": data["wind"]["speed"],
        "feels_like_celsius": data["main"]["feels_like"]
    }

if __name__ == "__main__":
    result = get_weather("Tirupati")
    print(result)