"""Library with OpenAI solutions."""

from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()


# build a function to submit a question with the latest version of the openai api and completition
def submit_question(question):

    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
    )

    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question},
        ],
        model="gpt-3.5-turbo",
        max_tokens=100,
        temperature=0.7,
    )

    completition = response.choices[0].message.content

    return completition

#build a function that converts language to python code
def convert_to_code(question):
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
    )

    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question},
        ],
        model="gpt-3.5-turbo",
        max_tokens=100,
        temperature=0.7,
    )

    completition = response.choices[0].message.content

    return completition