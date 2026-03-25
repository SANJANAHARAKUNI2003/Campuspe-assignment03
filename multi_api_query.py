import os
import streamlit as st
from dotenv import load_dotenv
from tenacity import retry, stop_after_attempt, wait_exponential

# Load env
load_dotenv()

# APIs
from groq import Groq
import cohere
import google.generativeai as genai
from huggingface_hub import InferenceClient

# Clients
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))
cohere_client = cohere.Client(os.getenv("COHERE_API_KEY"))
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
hf_client = InferenceClient(token=os.getenv("HF_API_KEY"))

#  RETRY 
@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
def safe_call(func, *args, **kwargs):
    return func(*args, **kwargs)


#  API FUNCTIONS 

def query_groq(prompt, stream=False):
    if stream:
        completion = groq_client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            stream=True
        )
        result = ""
        placeholder = st.empty()

        for chunk in completion:
            content = chunk.choices[0].delta.content or ""
            result += content
            placeholder.markdown(result)

        return result
    else:
        res = safe_call(
            groq_client.chat.completions.create,
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile"
        )
        return res.choices[0].message.content


def query_cohere(prompt):
    res = safe_call(
        cohere_client.generate,
        model="command-a-03-2025",
        prompt=prompt,
        max_tokens=150
    )
    return res.generations[0].text


def query_gemini(prompt):
    model = genai.GenerativeModel("gemini-3.1-flash-lite-preview")
    res = safe_call(model.generate_content, prompt)
    return res.text


def query_hf(prompt):
    res = safe_call(
        hf_client.text_generation,
        prompt,
        model="meta-llama/Meta-Llama-3-8B-Instruct",
        max_new_tokens=100
    )
    return res


# STREAMLIT UI 

st.set_page_config(page_title="Multi API Chat", layout="wide")
st.title(" Multi-API Chatbot")

# Session history
if "history" not in st.session_state:
    st.session_state.history = []

# Sidebar
option = st.sidebar.selectbox(
    "Choose API",
    ["Groq (Streaming)", "Cohere", "Gemini", "HuggingFace", "Compare All"]
)

# Input
prompt = st.text_input("Enter your prompt")

# Submit
if st.button("Submit"):

    if not prompt:
        st.warning("Please enter a prompt")
    else:
        st.session_state.history.append({"user": prompt})

        if option == "Groq (Streaming)":
            response = query_groq(prompt, stream=True)

        elif option == "Cohere":
            response = query_cohere(prompt)
            st.write(response)

        elif option == "Gemini":
            response = query_gemini(prompt)
            st.write(response)

        elif option == "HuggingFace":
            response = query_hf(prompt)
            st.write(response)

        elif option == "Compare All":
            st.subheader(" Comparison Results")

            st.write("### Groq")
            st.write(query_groq(prompt))

            st.write("### Cohere")
            st.write(query_cohere(prompt))

            st.write("### Gemini")
            st.write(query_gemini(prompt))

            st.write("### HuggingFace")
            st.write(query_hf(prompt))

            response = "Compared all APIs"

        st.session_state.history.append({"bot": response})


#  HISTORY DISPLAY 

st.subheader(" Conversation History")

for chat in st.session_state.history:
    if "user" in chat:
        st.markdown(f"** You:** {chat['user']}")
    else:
        st.markdown(f"** Bot:** {chat['bot']}")