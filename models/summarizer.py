import os
import requests

HF_API_TOKEN = os.getenv("HF_API_TOKEN")  # set this on Render or .env

def summarize_text(text: str) -> str:
    if not HF_API_TOKEN:
        return "Summarization not available (Hugging Face API key missing)."

    headers = {
        "Authorization": f"Bearer {HF_API_TOKEN}"
    }
    payload = {
        "inputs": text,
        "parameters": {
            "max_length": 50,
            "min_length": 10,
            "do_sample": False
        }
    }

    response = requests.post(
        "https://api-inference.huggingface.co/models/sshleifer/distilbart-cnn-12-6",
        headers=headers,
        json=payload
    )

    if response.status_code == 200:
        result = response.json()
        if isinstance(result, list):
            return result[0].get("summary_text", "No summary")
        return "Unexpected response format"
    else:
        return f"Error from Hugging Face API: {response.status_code}"
