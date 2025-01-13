#!/usr/bin/env python3

import click
from oalib.solutions import submit_question


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
