# 🌾 AI Farmer Assistant

An AI-powered farming assistant that gives real-time advice to Indian farmers based on live weather data.

## 🚀 Features
- 🌤️ Live weather data from any Indian city
- 🤖 AI-powered farming advice using Llama 3.3 70B
- 🌱 Crop recommendations based on current weather
- 💧 Irrigation and pesticide timing advice

## 🛠️ Tech Stack
- **Python** — core language
- **Groq API** — LLM (Llama 3.3 70B)
- **OpenWeatherMap API** — live weather data
- **AWS Lambda** — serverless deployment (Week 2)
- **React** — farmer chat UI (Week 3)
- **Docker + GitHub Actions** — CI/CD pipeline (Week 6)

## 📦 Setup

```bash
git clone https://github.com/MikkilineniNithish/ai-farmer-assistant.git
cd ai-farmer-assistant
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file: