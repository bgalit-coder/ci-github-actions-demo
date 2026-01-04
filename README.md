# ci-github-actions-demo

This repository demonstrates Continuous Integration (CI) concepts using GitHub Actions.
It was built step by step as part of a CI learning exercise, starting from a basic workflow
and gradually adding testing, matrix builds, and a self-hosted runner.

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

## Task 4: Matrix Builds

### Description
This task further extends the workflow by introducing **matrix builds**.

The same test suite is executed across multiple Python versions to ensure compatibility
and consistent behavior.

### Python Versions Tested
- Python 3.7
- Python 3.8
- Python 3.9
- Python 3.10

The workflow uses a matrix strategy so that the job runs once for each Python version.

> Note: The workflow uses the Ubuntu 22.04 runner to ensure compatibility with Python 3.7.

---

## GitHub Actions Workflow

### Trigger
The workflow runs automatically on every push to:
- main
- master (if configured)

### Steps Performed
1. Check out the repository code
2. Print a Hello message
3. Set up the required Python version (using a matrix build)
4. Install dependencies (if a requirements.txt file exists)
5. Run unit tests using unittest

---

## Project Structure

.
├── main.py
├── test_main.py
├── README.md
└── .github
  └── workflows
      ├── hello-ci.yml
      └── hello-ci-self-hosted.yml
---

## Running Tests Locally

To run the tests locally, use:

python -m unittest -v

---

## Expected CI Result

When changes are pushed to the repository:
- The workflow runs automatically
- The Hello message is printed in the logs
- Tests are executed for each Python version in the matrix
- Test results are displayed in the GitHub Actions logs
- The workflow completes successfully if all tests pass

---

## Bonus: Self-Hosted Runner (Windows)

### Goal
Set up a self-hosted GitHub Actions runner on a Windows machine and run a workflow using it.

### Setup Summary
- A self-hosted runner was configured from the repository settings:
  **Settings → Actions → Runners**
- The runner was installed and configured on a local Windows machine
- The runner was registered to this repository using a temporary registration token
- The runner is executed manually using `run.cmd`

### Workflow Configuration
A dedicated workflow was created to run on the self-hosted runner without affecting the existing CI workflows.

Key characteristics:
- Triggered manually using `workflow_dispatch`
- Runs on:self-hosted
- Uses the Windows Python launcher (`py`) to run tests
- Uses Windows PowerShell as the execution shell

### Notes
- On self-hosted runners, required tools (such as Python and Git) must be installed manually on the runner machine
- The workflow uses `py -m unittest -v` instead of `python` to match the local Windows environment

### Verification
The workflow was successfully executed on the self-hosted Windows runner, and the job logs confirm that the runner handled the execution.

---

## Summary

This repository demonstrates a complete CI process using GitHub Actions:
- Automatic workflows on push
- Python unit testing
- Matrix builds across multiple Python versions
- Execution on both GitHub-hosted and self-hosted runners

Each task was implemented incrementally, with commits documenting the progression.

