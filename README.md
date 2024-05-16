# Branch: 4-Summarization

Welcome to the 4-summarization branch of our AI Testing workshop! In this section, you will tackle the challenge of summarizing text and testing the effectiveness of those summaries under various scenarios.

## Installation

Follow the same installation steps as in the previous exercises:

```
poetry install
```
 
## Running the Tests

To run the tests, you can run

```bash
poetry install
poetry run pytest tests/test_summarize.py
poetry run pytest tests/test_security.py
poetry run pytest tests
```

## Understanding the Challenge

Testing automatic text summarization introduces unique challenges, as the output can vary with each run. This makes it difficult to predict and verify the accuracy of the summary programmatically. You'll need to consider these variations when designing your tests.

## Exercises

**Exercise 1:**
Create a basic test case to evaluate if the summarization function works correctly. This test should check whether the function returns a summary and whether the summary is non-empty.
**Exercise 2:**
Modify the summarization prompt to generate summaries shorter than 10 words. Implement a test to verify that the summary adheres to this length constraint.
**Exercise 3:**
Develop a random text generator using another model. This generator will serve as input to test the robustness of your summarization function under different text inputs.
**Exercise 4:**
Take a look into the security tests and try to fix the prompt to avoid the issues. Create more tests to ensure the model is secure.


## Tips for Testing

The best way to do verifications is using libraries for evaluation. Some libraries you can use are:
- [Langchain Evaluators](https://python.langchain.com/v0.1/docs/guides/productionization/evaluation/). For this case you can use [criteria evaluation](https://python.langchain.com/v0.1/docs/guides/productionization/evaluation/string/criteria_eval_chain/).
- [ROUGE](https://en.wikipedia.org/wiki/ROUGE_(metric)). You can use the Python implementation [rouge](https://pypi.org/project/rouge/)
- [Hugging Face Evaluate](https://huggingface.co/docs/evaluate/en/index). Use its Python library [evaluate](https://pypi.org/project/evaluate/)

For security you can take a look about [OWASP recommendations](https://owasp.org/www-project-top-10-for-large-language-model-applications/).

## Support

For any questions or issues you encounter, please reach out to the workshop organizers.

---

Explore the complexities of AI-driven text summarization and enhance your testing strategies!

---