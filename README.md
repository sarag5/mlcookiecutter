# mlcookiecutter


## Overview

**mlcookiecutter** is a command-line tool that helps you quickly set up a structured project directory for data science and machine learning projects. It creates a predefined folder structure, initializes necessary files, and provides a template for your project, making it easier to start new projects with best practices in mind.

## Features

- Create a well-organized project structure
- Generate essential files such as `README.md`, `LICENSE`, and `requirements.txt`
- Supports various license types
- Allows specifying CODEOWNERS for collaborative projects

## Installation

You can install the package directly from PyPI using pip:

```bash
pip install mlcookiecutter
```
Or clone this repository and install it locally:
```bash
git clone https://github.com/sarag5/mlcookiecutter.git
cd mlcookiecutter
pip install -e .
```
Usage
To create a new project structure, use the command line interface:
```bash
project_creator --project_name <your_project_name> --license_type <license_type> --codeowners <comma_separated_owners>
```
Example
```bash
project_creator --project_name my_data_project --license_type mit --codeowners user1@example.com,user2@example.com
```
This command will create a new directory called my_data_project with the following structure:
```text
my_data_project/
├── data/
│   ├── raw/
│   └── processed/
├── src/
│   ├── data_engineering/
│   ├── feature_engineering/
│   ├── model/
│   └── utils/
├── notebooks/
├── tests/
│   ├── data_engineering/
│   └── model/
├── models/
├── scripts/
├── deployment/
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── CODEOWNERS
└── tasks.py
```
Available Tasks
This project uses Invoke to manage various tasks. Here are the available tasks:
run_locally: Run the project locally.
run_tests: Run the test suite.
run_lint: Run the linter (flake8).
run_build: Run the build process.
check_format: Check the code formatting.
correct_format: Correct the code formatting.
To see all available tasks, run:
```bash
invoke --list
```
Contributing
Contributions are welcome! Please feel free to submit issues or pull requests.
Fork the repository.
Create your feature branch (git checkout -b feature/YourFeature).
Commit your changes (git commit -m 'Add some feature').
Push to the branch (git push origin feature/YourFeature).
Open a pull request.
License
This project is licensed under the MIT License - see the LICENSE file for details.
Contributors
See the CODEOWNERS file for the list of contributors.
Acknowledgments
Inspired by various open-source projects that aim to streamline project setup.
Thanks to all contributors for their valuable input!
