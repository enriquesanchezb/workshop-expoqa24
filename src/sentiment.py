"""
Get sentiment analysis results for the given text
"""

from transformers import pipeline

sentiment_pipeline = pipeline(
    task="text-classification", model="SamLowe/roberta-base-go_emotions", top_k=None
)


def analyze_sentiment(text: str) -> dict:
    """Returns the sentiment analysis results for the given text"""
    try:
        results = sentiment_pipeline(text)
        sentiment_results = {result["label"]: result["score"] for result in results[0]}
        max_sentiment = max(sentiment_results, key=sentiment_results.get)
        return max_sentiment
    except Exception as e:
        print(f"Error in analyze_sentiment: {e}")
        return {}
