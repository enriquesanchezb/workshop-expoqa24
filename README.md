# Workshop instructions

## Summarization

Let's add some complexity. Now we gonna try to summarize a text. Our problem now is knowing if the summarization is useful and real under different scenarios.

How to test something that gonna be different everytime you run the test?

## Installation

Same steps than the previous exercise
 
## How to run the tests

```bash
poetry install
poetry run pytest tests/test_summarize.py
```

## Exercises

- Create a simple test case to evaluate if summarize works.
- Change the prompt to make the summary less than 10 words. Now add a verification in the test to be sure is working.
- Create a random text generator using another model.
