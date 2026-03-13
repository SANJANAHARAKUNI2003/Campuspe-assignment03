import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

print("\033[1;31mOpenAI Chatbot (type 'exit' to quit)\033[0m\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("\033[1mChatbot: Goodbye!\033[0m")
        break

    try:
        response = client.chat.completions.create(
            model="gpt-5-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ],
            max_tokens=200,   # token limit
            temperature=0.7
        )

        reply = response.choices[0].message.content

        # Bold output
        print("\033[1mChatbot:\033[0m", "\033[1m" + reply + "\033[0m")

    except Exception as e:
        print("\033[1mChatbot Error:\033[0m", str(e))