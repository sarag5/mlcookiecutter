import os
import click
import requests

def create_directory(path):
    os.makedirs(path, exist_ok=True)

def create_file(path, content=""):
    with open(path, "w") as f:
        f.write(content)

def get_license_content(license_type):
    url = f"https://api.github.com/licenses/{license_type}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['body']
    else:
        return "Failed to fetch license. Please add manually."

def create_github_workflows(base_dir):
    workflows_dir = os.path.join(base_dir, ".github", "workflows")
    create_directory(workflows_dir)

    # Test and Lint Workflow
    test_lint_workflow = """name: Test and Lint

on: [push, pull_request]

jobs:
  test-lint:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.9'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Run tests
      run: pytest
    - name: Run lint
      run: flake8 src/ tests/
"""
    create_file(os.path.join(workflows_dir, "test-lint.yml"), test_lint_workflow)

    # ML Model Validation Workflow
    ml_validation_workflow = """name: ML Model Validation

on:
  push:
    paths:
      - 'src/model/**'
      - 'data/**'

jobs:
  validate-model:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.9'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Train and validate model
      run: |
        python src/model/train_model.py
        python src/model/validate_model.py
"""
    create_file(os.path.join(workflows_dir, "ml-validation.yml"), ml_validation_workflow)

    # Data Quality Check Workflow
    data_quality_workflow = """name: Data Quality Check

on:
  push:
    paths:
      - 'data/**'

jobs:
  check-data-quality:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.9'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Run data quality checks
      run: python src/data_engineering/check_data_quality.py
"""
    create_file(os.path.join(workflows_dir, "data-quality.yml"), data_quality_workflow)
    
@click.command()
@click.option('--project_name', prompt='Enter project name', default='default_project', help='Name of the project')
@click.option('--license_type', prompt='Enter license type (e.g., mit, apache-2.0)', default='mit', help='Type of license')
@click.option('--codeowners', prompt='Enter CODEOWNERS (comma-separated)', default='', help='CODEOWNERS for the project')
def mlcookiecutter(project_name, license_type, codeowners):
    base_dir = os.path.join(os.getcwd(), project_name)
    
    # Create main project directory
    create_directory(base_dir)
    create_github_workflows(base_dir)
    # Create subdirectories
    directories = [
        "data/raw",
        "data/processed",
        "src/data_engineering",
        "src/feature_engineering",
        "src/model",
        "src/utils",
        "notebooks",
        "tests/data_engineering",
        "tests/model",
        "models",
        "scripts",
        "deployment"
    ]
    
    for directory in directories:
        create_directory(os.path.join(base_dir, directory))
    
    # Create __init__.py files
    init_dirs = [
        "src/data_engineering",
        "src/feature_engineering",
        "src/model",
        "src/utils"
    ]
    
    for init_dir in init_dirs:
        create_file(os.path.join(base_dir, init_dir, "__init__.py"))
    
    # Create sample files
    sample_files = {
        "data/raw/sample_raw_data.csv": "id,feature1,feature2,target\n1,0.5,0.7,1\n2,0.3,0.2,0\n3,0.8,0.9,1",
        "data/processed/sample_processed_data.csv": "id,normalized_feature1,normalized_feature2,target\n1,0.25,0.56,1\n2,0.11,0.04,0\n3,0.64,0.81,1",
        "src/data_engineering/data_processor.py": "def process_data(raw_data):\n    # Add your data processing logic here\n    return processed_data",
        "src/feature_engineering/feature_creator.py": "def create_features(data):\n    # Add your feature engineering logic here\n    return data_with_new_features",
        "src/model/model.py": "from sklearn.ensemble import RandomForestClassifier\n\ndef train_model(X, y):\n    model = RandomForestClassifier()\n    model.fit(X, y)\n    return model",
        "notebooks/exploratory_data_analysis.ipynb": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": [\"# Exploratory Data Analysis\"]\n  },\n  {\n   \"cell_type\": \"code\",\n   \"execution_count\": null,\n   \"metadata\": {},\n   \"source\": [\"import pandas as pd\\nimport matplotlib.pyplot as plt\\n\\n# Load your data here\\n# df = pd.read_csv('../data/raw/sample_raw_data.csv')\\n\\n# Add your EDA code here\"]\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 4\n}",
        "tests/data_engineering/test_data_processor.py": "import unittest\nfrom src.data_engineering.data_processor import process_data\n\nclass TestDataProcessor(unittest.TestCase):\n    def test_process_data(self):\n        # Add your test cases here\n        pass",
        "tests/model/test_model.py": "import unittest\nfrom src.model.model import train_model\n\nclass TestModel(unittest.TestCase):\n    def test_train_model(self):\n        # Add your test cases here\n        pass",
        "models/.gitkeep": "",
        "src/model/train_model.py": "# Add your model training code here\n",
        "src/model/validate_model.py": "# Add your model validation code here\n",
        "src/data_engineering/check_data_quality.py": "# Add your data quality check code here\n",
        "scripts/run_pipeline.sh": "#!/bin/bash\n\n# Add your pipeline execution commands here\necho \"Running data processing...\"\n# python -m src.data_engineering.data_processor\n\necho \"Running feature engineering...\"\n# python -m src.feature_engineering.feature_creator\n\necho \"Training model...\"\n# python -m src.model.model",
        "deployment/Dockerfile": "FROM python:3.9-slim\n\nWORKDIR /app\n\nCOPY requirements.txt .\nRUN pip install --no-cache-dir -r requirements.txt\n\nCOPY . .\n\nCMD [\"python\", \"-m\", \"src.model.model\"]"
    }
    
    for file_path, content in sample_files.items():
        create_file(os.path.join(base_dir, file_path), content)
    
    # Create other necessary files
    create_file(os.path.join(base_dir, ".gitignore"), "*.pyc\n__pycache__\n.ipynb_checkpoints\n")
    create_file(os.path.join(base_dir, "requirements.txt"), "pandas\nnumpy\nscikit-learn\nmatplotlib\njupyter\nrequests\ninvoke\nblack\nflake8\npytest\npytest-cov\ngreat-expectations")
    
    # Create LICENSE file
    license_content = get_license_content(license_type)
    create_file(os.path.join(base_dir, "LICENSE"), license_content)
    
    # Create CODEOWNERS file
    codeowners_content = "# This file lists the code owners for this project\n\n"
    if codeowners:
        for owner in codeowners.split(','):
            codeowners_content += f"* {owner.strip()}\n"
    else:
        codeowners_content += "# Add CODEOWNERS here\n"
    create_file(os.path.join(base_dir, "CODEOWNERS"), codeowners_content)
    
    # Create tasks.py file
    tasks_content = """from invoke import task

@task
def run_locally(c):
    print("Running locally...")
    # Add commands to run your project locally

@task
def run_tests(c):
    print("Running tests...")
    c.run("pytest tests/")

@task
def run_lint(c):
    print("Running linter...")
    c.run("flake8 src/ tests/")

@task
def run_build(c):
    print("Running build...")
    # Add commands to build your project

@task
def check_format(c):
    print("Checking code format...")
    c.run("black --check src/ tests/")

@task
def correct_format(c):
    print("Correcting code format...")
    c.run("black src/ tests/")
"""
    create_file(os.path.join(base_dir, "tasks.py"), tasks_content)
    
    # Create README.md file with enhanced content
    readme_content = f"""# {project_name}

## Project Description

Add your project description here.

## Installation

To set up the project environment:

1. Clone the repository:
```bash
git clone https://github.com/yourusername/{project_name}.git
cd {project_name}
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate # On Windows, use venv\\Scripts\\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Available Tasks

This project uses [Invoke](http://www.pyinvoke.org/) to manage various tasks. Here are the available tasks:

- `run_locally`: Run the project locally

invoke run-locally


- `run_tests`: Run the test suite

invoke run-tests


- `run_lint`: Run the linter (flake8)

invoke run-lint


- `run_build`: Run the build process

invoke run-build


- `check_format`: Check the code formatting

invoke check-format


- `correct_format`: Correct the code formatting

invoke correct-format


To see all available tasks, run:

invoke --list


## Project Structure

```text
{project_name}/
├── data/
│ ├── raw/
│ └── processed/
├── src/
│ ├── data_engineering/
│ ├── feature_engineering/
│ ├── model/
│ └── utils/
├── notebooks/
├── tests/
│ ├── data_engineering/
│ └── model/
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

## License

This project is licensed under the {license_type.upper()} License - see the [LICENSE](LICENSE) file for details.

## Contributors

See the [CODEOWNERS](CODEOWNERS) file for the list of contributors.
"""
    create_file(os.path.join(base_dir, "README.md"), readme_content)
    
    click.echo(f"Project structure created in {base_dir}")

if __name__ == "__main__":
    mlcookiecutter()
