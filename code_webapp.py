import streamlit as st
from oalib.solutions import submit_question

st.title("OpenAI Chatbot")
st.write("This is a simple chatbot powered by OpenAI's GPT-3.5 model. Ask me anything!")

question = st.text_input("Ask a question:")

if st.button("Submit"):
    with st.spinner(text="Thinking..."):
        response = submit_question(question)
        st.success(response)
