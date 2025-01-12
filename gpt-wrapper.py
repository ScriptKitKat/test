from openai import OpenAI
import streamlit as st

api_key = st.secrets["api_key"]

client = OpenAI(api_key=api_key)
completion = client.Completion.create(
    model="gpt-3.5-turbo",
    store=True,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
    ]
)