#!/usr/bin/env python3

"""
An openai api key is required to use this script.
This uses an advanced GPT-3 model and I also used AI via Github Copilot to write this command-line interface.
"""

import openai
import os
import click


# build a function to submit a question with the latest version of the openai api and completition
def submit_question(question):
    openai.api_key = os.environ.get("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-4",  # You can use "gpt-3.5-turbo" for a cheaper option
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question},
        ],
        max_tokens=100,  # Adjust token limit based on your use case
        temperature=0.7,  # Adjust creativity level
    )
    # Return the generated response text
    return response["choices"][0]["message"]["content"].strip()


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
    echo(response)


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    main()
