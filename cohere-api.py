import os
import cohere
from dotenv import load_dotenv

# load env file
load_dotenv()
api_key = os.getenv("COHERE_API_KEY")

co = cohere.Client(api_key)

print("\033[1;31mCohere Chatbot (type 'exit' to quit)\033[0m\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("\033[1mChatbot: Goodbye!\033[0m")
        break

    try:
        response = co.chat(
            model="command-a-03-2025",
            message=user_input,
            max_tokens=600
        )

        bot_reply = response.text

    except Exception as e:
        bot_reply = f"Error: {e}"

    print("\033[1mChatbot:\033[0m", "\033[1m" + bot_reply + "\033[0m")
















   