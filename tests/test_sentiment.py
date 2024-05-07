from src.sentiment import analyze_sentiment


def test_analyze_sentiment_positive():
    text = "I love this product!"
    expected_result = "positive"
    assert analyze_sentiment(text) == expected_result


def test_analyze_sentiment_negative():
    text = "This movie is terrible."
    expected_result = "negative"
    assert analyze_sentiment(text) == expected_result


def test_analyze_sentiment_empty_text():
    text = ""
    expected_result = "neutral"
    assert analyze_sentiment(text) == expected_result


def test_analyze_sentiment_exception():
    text = "Some text"
    # Assuming sentiment_pipeline raises an exception
    expected_result = "neutral"
    assert analyze_sentiment(text) == expected_result


# TODO: Fix the tests above to use the correct expected results. Add more tests.
