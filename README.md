# Branch: 4-Summarization

Welcome to the 4-summarization branch of our AI Testing workshop! In this section, you will tackle the challenge of summarizing text and testing the effectiveness of those summaries under various scenarios.

## Installation

Follow the same installation steps as in the previous exercises:

```
poetry install
```
 
## Running the Tests

To run the summarization tests, use the following commands:

```bash
poetry install
poetry run pytest tests/test_summarize.py
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


## Tips for Testing

The best way to do verifications is using [Langchain Evaluators](https://python.langchain.com/v0.1/docs/guides/productionization/evaluation/). For this case you can use [criteria evaluation](https://python.langchain.com/v0.1/docs/guides/productionization/evaluation/string/criteria_eval_chain/).
Using this library, some of the things you need to evaluate for testing are:

- **Consistency Checks:** Even though the content may vary, certain aspects like summary length or specific keyword presence can be consistently tested.
- **Regression Tests:** If you have a set of known good inputs and outputs, you can use these for regression testing to ensure the model's performance remains stable over updates.
- **Automated vs Manual Testing:** Consider automating what is consistent and reviewing variabilities manually or with a less strict automated test to allow for natural language variation.

## Support

For any questions or issues you encounter, please reach out to the workshop organizers.

---

Explore the complexities of AI-driven text summarization and enhance your testing strategies!

---