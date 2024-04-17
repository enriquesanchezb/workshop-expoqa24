# Workshop instructions

## Sentiment analysis

Here you have a simple app, that is able to analyze the sentiment of your voice. Your mission is test it properly!

## Installation

Install Python and Poetry first. After that simply run:

```bash
poetry install
```

Depending on your OS you can have some problems installing `Tensorflow` or `tf-keras`. If it happens, review how to install Tensorflow [here](https://www.tensorflow.org/install)

## How to run the app

```bash
poetry run app.py
```

You have to have a message like this:

```bash
> poetry run python app.py
Running on local URL:  http://127.0.0.1:7860

To create a public link, set `share=True` in `launch()`.
```

The app will be running in `http://127.0.0.1:7860`

## How to run the test cases

```bash
poetry run pytest
```

## Exercises

1. Fix `/tests/test_sentiment.py`! is not working and it should works
2. Fix `/tests/test_transcribe.py`. You have a sample audio in `/tests/samples` you can use.