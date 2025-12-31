# ci-github-actions-demo

This repository demonstrates basic Continuous Integration (CI) using GitHub Actions.

The project includes:
- A basic GitHub Actions workflow triggered on every push to the main branch
- A simple shell command execution
- A Python script
- Unit tests using Python’s built-in unittest framework
- Automated test execution as part of the CI process

---

## Part 1: Continuous Integration with GitHub Actions

### Repository Setup
- Repository name: ci-github-actions-demo
- Initialized with a README.md file
- GitHub Actions workflow located under:
  .github/workflows/hello-ci.yml

---

## Task 1: Basic GitHub Actions Workflow

### Description
A GitHub Actions workflow is configured to run whenever code is pushed to the main branch.

### Workflow Steps
1. Check out the repository code using actions/checkout
2. Run a shell command that prints:
   Hello, CI with GitHub Actions!

### Expected Output
- A successful workflow run
- The message "Hello, CI with GitHub Actions!" appears in the workflow logs

---

## Task 2: Running Tests

### Description
This task extends the existing workflow to run Python unit tests automatically.

### Files Added

#### main.py
Contains a simple Python function that prints a name to standard output.

#### test_main.py
Contains unit tests written using the unittest framework.
The test verifies that the expected output is printed by the function in main.py.

Only Python standard library modules are used, so no external dependencies are required.

---

## GitHub Actions Workflow

### Trigger
The workflow runs automatically on every push to:
- main
- master (if configured)

### Steps Performed
1. Check out the repository code
2. Set up Python version 3.9 using actions/setup-python@v4
3. Install dependencies (only if a requirements.txt file exists)
4. Run unit tests using unittest

---

## Project Structure

.
├── main.py
├── test_main.py
├── README.md
└── .github
    └── workflows
        └── hello-ci.yml

---

## Running Tests Locally

To run the tests locally, use:

python -m unittest -v

---

## Expected CI Result

When changes are pushed to the repository:
- The workflow runs automatically
- The Hello message is printed in the logs
- Unit tests are executed
- The workflow completes successfully if all tests pass

---

## Summary

This repository demonstrates a simple but complete CI setup using GitHub Actions,
including automated testing with Python.

