# Branch: 5-GitHub-Actions

Welcome to the `5-github-actions` branch of our AI Testing workshop! This section introduces you to using GitHub Actions to automate the installation of models and execution of test cases in a continuous integration pipeline.

## Overview
In this branch, we'll integrate the work from previous exercises into a CI/CD pipeline using GitHub Actions. This will allow us to automatically run tests and ensure our models function correctly with each new change to the codebase.

## How to run the pipeline

1. **Examine the Workflow File:**
The GitHub Actions workflow is defined in .github/workflows/main.yml. This file contains all the necessary steps to install dependencies, set up environments, and run tests.
2. **Understand the Workflow Steps:**
   - **Setup:** Initializes the runner with the required version of Python and sets up caching for faster builds.
   - **Install Dependencies:** Uses Poetry to install all necessary dependencies from the pyproject.toml file.
   - **Run Tests:** Executes the test suite to verify that all parts of the application are functioning as expected.
3. **Triggering the Workflow:**
   - The workflow will automatically trigger on any push or pull request to relevant branches.
   - You can also manually trigger the workflow through the GitHub Actions tab on the repository.

## Modifications and Testing

Feel free to modify the `.github/workflows/main.yml` file to adjust the pipeline or add new steps. Testing these changes can ensure that your modifications meet the desired outcomes without disrupting the existing functionality.

## Exercises
- Review the provided `main.yml` and understand each action's role within the workflow.
- Experiment by adding a new step or job to the workflow, such as a linter or a different type of test.
- Monitor the pipeline execution via GitHub Actions and analyze the output to learn how CI/CD pipelines help in maintaining code quality.

## Support
If you encounter any issues or have questions about setting up or modifying the GitHub Actions workflow, please reach out to the workshop organizers.

--- 
**Dive into automating your testing and deployment processes with GitHub Actions!**

---