#!/usr/bin/env python3

"""
An openai api key is required to use this script.
This uses an advanced GPT-3 model and I also used AI via Github Copilot to write this command-line interface.
"""
from dotenv import load_dotenv
from openai import OpenAI
import os
import click

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


@click.group()
def main():
    """This is a CLI for asking questions using the OpenAI API"""


@main.command()
@click.argument("question")
def ask(question):
    """Ask a question and get a response

    Example: ./questionCLI.py ask "What is the capital of France?"
    """
    response = submit_question(question)
    # echo rhe response with color
    click.echo(click.style(response, fg="green"))


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    main()
