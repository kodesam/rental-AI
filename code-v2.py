
# Initialize OpenAI API key

openai.api_key = ""



# Streamlit app title

st.title("OpenAI GPT-3.5 Turbo Instruct using Streamlit")



# User input prompt

prompt = st.text_area("Enter your prompt:", "")



# Parameters for the API call

temperature = st.slider("Temperature:", min_value=0.0, max_value=1.0, value=1.0)

max_tokens = st.slider("Max tokens:", min_value=1, max_value=1024, value=256)

top_p = st.slider("Top P:", min_value=0.0, max_value=1.0, value=1.0)

frequency_penalty = st.slider("Frequency Penalty:", min_value=0.0, max_value=2.0, value=0.0)

presence_penalty = st.slider("Presence Penalty:", min_value=0.0, max_value=2.0, value=0.0)



# Generate response on button click

if st.button("Generate Response"):

    if prompt.strip() == "":

        st.warning("Please enter a prompt.")

    else:

        try:

            response = openai.Completion.create(

                model="gpt-3.5-turbo-instruct",

                prompt=prompt,

                temperature=temperature,

                max_tokens=max_tokens,

                top_p=top_p,

                frequency_penalty=frequency_penalty,

                presence_penalty=presence_penalty

            )

            st.success("Response generated successfully!")

            st.text_area("Response:", response.choices[0].text.strip(), height=200)

        except Exception as e:

            st.error(f"An error occurred: {e}")

