import streamlit as st
from multi_api_query import query_groq, query_cohere, query_gemini, query_hf

st.title(" Multi-LLM Chat")

option = st.selectbox("Choose API", ["Groq", "Cohere", "Gemini", "HuggingFace"])

prompt = st.text_input("Enter your prompt")

if st.button("Submit"):
    if option == "Groq":
        result = query_groq(prompt)
    elif option == "Cohere":
        result = query_cohere(prompt)
    elif option == "Gemini":
        result = query_gemini(prompt)
    else:
        result = query_hf(prompt)

    st.write("### Response")
    st.write(result)