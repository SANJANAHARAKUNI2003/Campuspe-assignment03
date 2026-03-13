import requests
import os
from dotenv import load_dotenv

# load env file
load_dotenv("../.env")

api_key = os.getenv("HF_API_KEY")

API_URL = "https://router.huggingface.co/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

print("\033[1;31mHugging Face Chatbot (type 'exit' to quit)\033[0m\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("\033[1mChatbot: Goodbye!\033[0m")
        break

    payload = {
        "model": "meta-llama/Meta-Llama-3-8B-Instruct",
        "messages": [
            {"role": "user", "content": user_input}
        ],
        "max_tokens": 200
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        result = response.json()
        

        bot_reply = result["choices"][0]["message"]["content"]

    except Exception as e:
        bot_reply = f"Error: {e}"

    print("\033[1mChatbot:\033[0m", "\033[1m" + bot_reply + "\033[0m")