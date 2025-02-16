import requests
from config import OPENAI_API_KEY, ELEVEN_LABS_API_KEY, HUGGINGFACE_API_KEY

# OpenAI API Call
def generate_text(prompt):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {"Authorization": f"Bearer {OPENAI_API_KEY}", "Content-Type": "application/json"}
    payload = {"model": "gpt-4", "messages": [{"role": "user", "content": prompt}]}

    response = requests.post(url, json=payload, headers=headers)
    return response.json()["choices"][0]["message"]["content"] if response.ok else "Error in OpenAI API"

# 11 Labs API Call
def generate_audio(text):
    url = f"https://api.elevenlabs.io/v1/text-to-speech"
    headers = {"xi-api-key": ELEVEN_LABS_API_KEY, "Content-Type": "application/json"}
    payload = {"text": text, "voice": "Adam"}

    response = requests.post(url, json=payload, headers=headers)
    return response.content if response.ok else "Error in Eleven Labs API"

# Hugging Face API Call
def generate_summary(text):
    url = f"https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
    payload = {"inputs": text}

    response = requests.post(url, json=payload, headers=headers)
    return response.json()[0]["summary_text"] if response.ok else "Error in Hugging Face API"
