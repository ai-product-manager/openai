from oalib.solutions import submit_question


def test_submit_question():
    """Test the submit_question function."""

    question = "What is the capital of France?"
    response = submit_question(question)
    assert "Paris" in response
