import streamlit as st
from openai import OpenAI

# Create OpenAI client
client = OpenAI()

# Input textbox in streamlit for prompt
prompt = st.text_input('Enter your prompt')

# When user enters prompt and hits Enter, generate completions
if prompt:
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        temperature=0,
        max_tokens=2901,
        top_p=1,
        best_of=8,
        frequency_penalty=0,
        presence_penalty=0
    )
    
    # Show the response on the screen
    st.write(response.choices[0].text.strip())
