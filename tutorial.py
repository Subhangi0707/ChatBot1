import streamlit as st
import google.generativeai as genai
import os

os.environ['GOOGLE_API_KEY'] = "AIzaSyDp0gCU3LqtIA8UYEFbl34lQYw3aL7NSdE"
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
model = genai.GenerativeModel('gemini-pro')

def chatbot_response(user_input):
    if user_input.lower() in ['quit', 'bye', 'exit']:
        return "Goodbye!"
    response = model.generate_content(user_input)
    return response.text

st.title("Chatbot")
user_input = st.text_input("You:")
response = chatbot_response(user_input)
if response:
    st.text_area("Chatbot:", response)
else:
    st.text("Waiting for user input...")

if __name__ == "__main__":
    st.write("")
