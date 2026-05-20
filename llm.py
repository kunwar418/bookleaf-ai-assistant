import requests
import os

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

def interpret_query(query: str):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {"role": "system", "content": "You are a query classifier for BookLeaf author support."},
            {"role": "user", "content": query}
        ]
    }
    response = requests.post(url, headers=headers, json=data)
    result = response.json()
    return result["choices"][0]["message"]["content"]
