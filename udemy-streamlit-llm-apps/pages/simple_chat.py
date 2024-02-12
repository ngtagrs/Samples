import streamlit as st
import openai
# from openai import OpenAI

st.title("simple chat")

user_message = st.text_input(label="どうしましたか？")

if user_message:
    # client = OpenAI()
    #completion = client.chat.completions.create(
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0,
        messages=[
            {"role": "system", "content": "Assistant is a large language model trained by OpenAI."},
            {"role": "user", "content": user_message}
        ]
    )
    st.write(completion)