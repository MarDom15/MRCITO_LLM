import streamlit as st
import requests

st.title("Chatbot MRC - Élections 2025")

question = st.text_input("Posez votre question sur le programme du MRC :")
if st.button("Envoyer"):
    response = requests.get(f"http://127.0.0.1:8000/ask/?question={question}")
    st.write(response.json()["response"])
