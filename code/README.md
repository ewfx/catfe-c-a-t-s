
# Testing tool for context based application

The repository to generate a high level BDD.

## install

```
pip install -r requirements.txt
```

# BDD Test Case Generator

This Python application reads structured test cases from an Excel file, generates AI-powered test scenarios, and converts them into BDD (Gherkin format).

## Setup Instructions

### Prerequisites
- Python 3.13
- Install dependencies using:
  ```sh
  pip install -r requirements.txt
  ```

### Usage
1. Place your structured test cases in `Data`.
2. Run the script:
   ```sh
   python src/main.py
   ```
3. Generated BDD scenarios will be saved in `output.feature`.

### Directory Structure
```
project_root/
│-- src/
│   │-- main.py
│   │-- utils.py
│   │-- generator.py
│-- test/
│   │-- test_generator.py
│-- README.md
│-- requirements.txt
```

### Testing
Run unit tests with:
```sh
pytest test/
```
"""
```
with open("README.md", "w") as f:
    f.write(readme_content)

print("README file generated.")