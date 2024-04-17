from src.summarize import summarize


def test_summarize():
    text = "This is a conversation."
    expected_summary = "???"

    summary = summarize(text)
    assert summary == expected_summary
