# Test task for the Radium company


## Description

- Write a script that runs asynchronous tasks that output after a random amount of time (up to 5 seconds): your name, the name of this vacancy, the expected salary level in a year.
- After executing all asynchronous tasks, the script should read the stdin and output the sha256 hash from the read data.
- The code must pass the `wemake-python-styleguide` linter check without any comments. Nitpick configuration - https://gitea.radium.group/radium/project-configuration
- 100% test coverage is required


## Execution

Lint: `$ flake8`

Test: `$ pytest --cov tests/`

Start: `$ python main.py`
