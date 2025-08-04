# Form Submission Test Automation

Form submission test automation tool using Playwright and Python. This project helps to test forms on the DemoQA website automatically with many flexible options.

## Author
Created by **CuongPT24** - Project practice Python automation testing

**Disclaimer**: This is a studying project for testing submission in demoqa. 

## Main features

- **Multiple test mode**: Direct mode, Pytest mode, Interactive Menu
- **Cross-browser testing**: Suppor Chromium, Firefox, WebKit
- **Headless/Headed mode**: Can run with hidden browser or with interface
- **Multiple test runs**: Run multiple test with delay between test
- **Random data generation**: Auto generate fake data to test
- **Logging & Reporting**: Detail log record and screenshots for successful submission
- **CLI interface**: Command line interface with flexible options

## Technical stacks

For detail packages and version, please read `requirements.txt`:
- **Python 3.8+**: Main programming language
- **Playwright**: Framework for automation browser
- **Pytest**: Framework testing
- **Faker**: Library to generate fake data


## Project structure

```
project/
├── README.md  
│   ├── requirements.txt         # Dependencies
│   └──  README.md               # README.md
├── main/
│   └── main_program.py          # Main program
├── tests/
│   ├── conftest.py              # Pytest fixtures
│   └── test_form_submission.py  # Test main logic
├── utils/
│   ├── cli_parser.py            # Handles CLI arguments
│   ├── data_generator.py        # Generates fake data
│   └── log_submission_result.py # Logging functionality
├── screenshots/
│   └── .png                     # Screenshots
└── reports/                    
    └── test_submission_log.csv  # Test result
```

## Installing

### Step 1: System requirements
- Python 3.8 or above
- pip package manager
- Git (to clone project)

### Step 2: Clone project
```bash
git clone <'https://github.com/CuongPT2811/python_training/tree/main/python_mock_project'>
cd python_mock_project 
```

### Step 3: Create virtual environment 
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
```

### Step 4: Install dependencies
```bash
# Install packages from requirements.txt
pip install -r requirements.txt

# Install browsers for Playwright
playwright install
```

### Step 5: Checking installation
```bash
# Check Python and pip version
python --version
pip --version

# Check Playwright version
playwright --version
```

## Usage Guide

### First time running 
```bash
python main/main_program.py
```
The program will display interactive menu for you to choose how to run test

### Other run modes

#### 1. Direct mode
```bash
python main/main_program.py --mode direct
```

#### 2. Pytest mode
```bash
python main/main_program.py --mode pytest
```

#### 3. Run hidden browser
```bash
python main/main_program.py --mode direct --headless
```

#### 4. Run multiple times with delay
```bash
python main/main_program.py --mode direct --count 5 --delay 3
```

#### 5. Run with different browser
```bash
python main/main_program.py --mode direct --browser firefox
```

#### 6. Display detail information
```bash
python main/main_program.py --mode direct --verbose
```

### See all options
```bash
python main/main_program.py --help
```

## Test result

After running the test, you might able to view:

1. **Console output**: Real-time result in terminal
2. **CSV log**: File `reports/test_submission_log.csv` contains test submissions.
3. **Screenshots**: Screenshots successful submission in `screenshots/`

## Troubleshooting

### Common errors

1. **ModuleNotFoundError: No module named 'playwright'**
   ```bash
   pip install playwright
   playwright install
   ```

2. **Browser not found**
   ```bash
   playwright install chromium
   ```

3. **Permission denied**
   - Windows: Run cmd as Administrator
   - macOS/Linux: Use `sudo` if needed

4. **Test fail**
   - Run `--delay 2` to increase delay time between test
   - Check internet connection

### Debug

For debugging when test fail:
```bash
# Run with verbose for detail
python main/main_program.py --mode direct --verbose

# Run headed to see browser
python main/main_program.py --mode direct 
```

## Further developments

### More functions
1. Fork project
2. Create new branch: `git checkout -b utils/new_features`
3. Code and test
4. Commit: `git commit -m "Add: feature description"`
5. Push and create Pull Request

### Run test development
```bash
# Test data generator
python utils/data_generator.py

# Test CLI parser
python utils/cli_parser.py

# Run pytest directly
pytest tests/test_form_submission.py -v -s 
```
