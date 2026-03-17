# **Assignment 03 Chatbots using API's**
---
## This Assignment contains terminal-based chatbots built using different AI APIs.
### APIs Used

1. Groq API  [Visit GitHub](groq-chatbot)
2. Hugging Face API [Visit GitHub](huggingface-chatbot)
3. Google Gemini API [Visit GitHub](googlegemini-chatbot)
4. Cohere API [Visit GitHub](cohere-chatbot)

---
## Project Structure
```
chatbots/
│
├── groq-chatbot/
│   ├── groq-api.py
│   ├── requirements.txt
│   └── venv/
│
├── huggingface-chatbot/
│   ├── huggingface-api.py
│   ├── requirements.txt
│   └── venv/
│
├── googlegemini-chatbot/
│   ├── googlegemini-api.py
│   ├── requirements.txt
│   └── venv/
│
├── cohere-chatbot/
│   ├── cohere-api.py
│   ├── requirements.txt
│   └── venv/
│
│
├── .env.example
└── README.md
```
---
## Important Setup Note

### Each chatbot uses its own virtual environment (venv) and requirements.txt file.
### This means dependencies must be installed separately for each chatbot.
---
## Setup Instructions
### 1. Clone the Repository
- `git clone https://github.com/SANJANAHARAKUNI2003/Campuspe-assignment03.git`
- `cd chatbots`
---
## 2. Setup Environment Variables
### Create a `.env` file using `.env.example` and add your API keys.

Example:
GROQ_API_KEY=your_key
HF_API_KEY=your_key
COHERE_API_KEY=your_key
GEMINI_API_KEY=your_key

---
## 3. Install Dependencies (Example: Groq Chatbot)

1. Navigate to the chatbot folder: `cd groq-chatbot`
2. Create virtual environment: `python -m venv venv`
3. Activate virtual environment (Windows): `venv\Scripts\activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run the chatbot: `python groq-api.py`

Repeat the same steps for other chatbot folders.

---
## Chatbot Screenshots
Groq Chatbot

