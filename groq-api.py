import os
from dotenv import load_dotenv
from groq import Groq


load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)

print("\033[1;31mGroq Chatbot (type 'exit' to quit)\033[0m\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("\033[1mChatbot: Goodbye!\033[0m")
        break

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": user_input}
            ]
        )

        bot_reply = response.choices[0].message.content
        print("\033[1mChatbot:\033[0m", "\033[1m"+bot_reply+"\033[0m")

    except Exception as e:
        print("Error:", e)