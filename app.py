import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

def generate_content(prompt):
    if not prompt or not prompt.strip():
        return ""  
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response.text


# Create the UI

import streamlit as st

st.title("The Best Chat App in 2024")
st.sidebar.title("Ask and you will be answered")
question = st.sidebar.text_input("Question:")
st.sidebar.button("Submit")
st.text("This is a chat app that uses the power of Artificial Intelligence")

answer = generate_content(question)

st.write(answer if answer else "")