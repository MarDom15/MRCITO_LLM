import streamlit as st
import requests

st.title("Chatbot MRC - Élections 2025")

question = st.text_input("Ask you question about MRC :")
if st.button("send"):
    response = requests.get(f"http://127.0.0.1:8000/ask/?question={question}")
    st.write(response.json()["Answer"])
