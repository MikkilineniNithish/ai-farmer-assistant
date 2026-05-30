from groq import Groq
import os
from dotenv import load_dotenv
from weather_tool import get_weather

load_dotenv(override=True)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_farmer_agent(question: str, city: str = "Tirupati") -> str:

    print(f"\n🌤️  Getting weather for {city}...")
    weather = get_weather(city)

    if "error" in weather:
        return f"Sorry, couldn't get weather data: {weather['error']}"

    prompt = f"""
You are a helpful AI Farmer Assistant for Indian farmers.
Speak in simple friendly English. Give practical advice.

Current weather in {weather['city']}:
- Temperature   : {weather['temperature_celsius']}°C (feels like {weather['feels_like_celsius']}°C)
- Humidity      : {weather['humidity_percent']}%
- Sky condition : {weather['description']}
- Wind speed    : {weather['wind_speed_mps']} m/s

Farmer's question: "{question}"

Give clear farming advice based on this weather.
Keep answer under 5 sentences. Be friendly!
"""

    print("🤖  Thinking...")
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    print("=" * 50)
    print("🌾  Welcome to AI Farmer Assistant!")
    print("    Type your question. Type 'quit' to exit.")
    print("=" * 50)

    city = input("\nEnter your city name: ").strip() or "Tirupati"

    while True:
        question = input("\n👨‍🌾 Your question: ").strip()

        if question.lower() in ["quit", "exit", "bye"]:
            print("\n👋 Goodbye, happy farming!")
            break

        if not question:
            print("Please type a question!")
            continue

        answer = ask_farmer_agent(question, city)

        print("\n🌾 Farmer Assistant says:")
        print("-" * 40)
        print(answer)
        print("-" * 40)