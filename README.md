# 🌾 AgriSmart AI Platform — Backend

Flask REST API powering the AI Farmer Assistant.

## 🚀 Live API
👉 https://ai-farmer-assistant.onrender.com

## 🌐 Frontend
👉 https://ai-farmer-frontend.vercel.app

## ✨ Features
- 💬 AI farming advice using Groq (Llama 3.3 70B)
- 🌤️ Live weather data from OpenWeatherMap
- 🌿 Crop disease detection using OpenRouter Vision AI
- 📜 Conversation history saved in Supabase
- 🔐 User authentication via Supabase Auth
- 🐳 Dockerized with GitHub Actions CI/CD

## 🛠️ Tech Stack
- Python, Flask, Gunicorn
- Groq API (Llama 3.3 70B)
- OpenRouter Vision AI
- OpenWeatherMap API
- Supabase (PostgreSQL + Auth)
- Docker, GitHub Actions, Render

## 📦 Setup Locally
```bash
git clone https://github.com/MikkilineniNithish/ai-farmer-assistant
cd ai-farmer-assistant
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Create `.env` file:# 🌾 AgriSmart AI Platform — Backend

Flask REST API powering the AI Farmer Assistant.

## 🚀 Live API
👉 https://ai-farmer-assistant.onrender.com

## 🌐 Frontend
👉 https://ai-farmer-frontend.vercel.app

## ✨ Features
- 💬 AI farming advice using Groq (Llama 3.3 70B)
- 🌤️ Live weather data from OpenWeatherMap
- 🌿 Crop disease detection using OpenRouter Vision AI
- 📜 Conversation history saved in Supabase
- 🔐 User authentication via Supabase Auth
- 🐳 Dockerized with GitHub Actions CI/CD

## 🛠️ Tech Stack
- Python, Flask, Gunicorn
- Groq API (Llama 3.3 70B)
- OpenRouter Vision AI
- OpenWeatherMap API
- Supabase (PostgreSQL + Auth)
- Docker, GitHub Actions, Render

## 📦 Setup Locally

git clone https://github.com/MikkilineniNithish/ai-farmer-assistant
cd ai-farmer-assistant
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

Create .env file:
GROQ_API_KEY=your_key
OPENWEATHER_API_KEY=your_key
OPENROUTER_API_KEY=your_key
SUPABASE_URL=your_url
SUPABASE_KEY=your_key

Run:
python main.py

## 🔗 API Endpoints
| Method | Endpoint | Description |
|---|---|---|
| GET | / | Health check |
| POST | /ask | Ask farming question |
| POST | /detect-disease | Upload crop image |
| GET | /history | Get conversation history |