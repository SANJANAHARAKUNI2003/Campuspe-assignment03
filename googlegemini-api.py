import os
import google.generativeai as genai
from dotenv import load_dotenv

# load env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-3.1-flash-lite-preview")

print("\033[1;31mGoogle gemini Chatbot (type 'exit' to quit)\033[0m\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("\033[1mChatbot: Goodbye!\033[0m")
        break

    response = model.generate_content(user_input)

    bot_reply = response.text

    print("\033[1mChatbot:\033[0m", "\033[1m" + bot_reply + "\033[0m")