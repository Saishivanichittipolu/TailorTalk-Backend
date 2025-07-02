# app.py
import streamlit as st
import requests

st.title("👕 TailorTalk – Appointment Bot")
st.write("Chat with the bot to check available slots or book an appointment.")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("You:", key="input")

if user_input:
    response = requests.post("http://127.0.0.1:8000/chat", json={"message": user_input})
    bot_reply = response.json()["response"]
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", bot_reply))

for sender, message in st.session_state.chat_history:
    st.markdown(f"**{sender}:** {message}")
