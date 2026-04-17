
import streamlit as st
import random

phrases = [
    "รักมากนะะะ พิมพ์อะไรมาก็รักหมดดด",
    "เมื่อไรจะกลับมาาาา",
    "ง้ออออออ",
    "รักแพรรรรรรรรร"
]

st.set_page_config(page_title="Random Phrase App", page_icon=":speech_balloon:")

st.title("Random Thai Phrase Generator")

if st.button("Get a new phrase!"):
    random_phrase = random.choice(phrases)
    st.write(f"## {random_phrase}")

