from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="mlcookiecutter",
    version="1.1.0",
    author="sarag5",
    author_email="sabarinathan_96@proton.me",
    description="A tool to create project structures for ml/data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sarag5/mlcookiecutter",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "mlcookiecutter=mlcookiecutter.main:mlcookiecutter",
        ],
    },
    python_requires=">=3.6",
    install_requires=[
        "click",
        "requests",
    ],
)
