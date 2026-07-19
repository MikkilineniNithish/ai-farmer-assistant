import requests
import base64
import os
from dotenv import load_dotenv

load_dotenv(override=True)

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")


def detect_disease(image_bytes: bytes) -> str:
    base64_image = base64.b64encode(image_bytes).decode("utf-8")

    prompt = """You are an expert agricultural plant pathologist helping Indian farmers.
Look at this crop/plant leaf image carefully and provide:

1. Plant identification (if possible)
2. Disease/Pest detected (name it clearly, or say Healthy if no issue)
3. Severity (Mild / Moderate / Severe)
4. Treatment advice (2-3 practical steps a farmer can take)
5. Prevention tips (1-2 tips for future)

Keep your answer simple, practical, and farmer-friendly.
Do NOT use markdown formatting like ### or ** or --.
Use plain text with numbers and line breaks only."""

    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "nvidia/nemotron-nano-12b-v2-vl:free",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            }
                        }
                    ]
                }
            ]
        }
    )

    result = response.json()
    return result["choices"][0]["message"]["content"]


if __name__ == "__main__":
    with open("test_leaf.jpg", "rb") as f:
        image_data = f.read()

    result = detect_disease(image_data)
    print(result)