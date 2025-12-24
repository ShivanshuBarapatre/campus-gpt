import os
import requests
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

def ask_groq(messages):
    payload = {
        "model": "llama3-70b-8192",
        "messages": messages,
        "temperature": 0.3
    }

    response = requests.post(GROQ_URL, headers=HEADERS, json=payload)

    if response.status_code != 200:
        return "Sorry, something went wrong with AI."

    return response.json()["choices"][0]["message"]["content"]
