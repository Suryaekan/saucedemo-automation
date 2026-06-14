# Sauce Demo Automation Framework

End-to-end UI test automation for [Sauce Demo](https://www.saucedemo.com/) built with **Playwright** and **Pytest**. Follows a clean Page Object Model pattern with locators, page actions, and test scenarios separated into distinct layers. Tests run automatically on every push via GitHub Actions CI.

## Tech Stack

- **Language:** Python 3.12
- **Test Framework:** Pytest
- **Browser Automation:** Playwright
- **Design Pattern:** Page Object Model — locators decoupled from page actions
- **Assertions:** pytest-check (soft assertions)
- **Reporting:** pytest-html (self-contained HTML report)
- **CI/CD:** GitHub Actions (headless Chromium on Ubuntu)
- **Parallel Execution:** pytest-xdist

## Project Structure

```
saucedemo-automation/
├── .github/workflows/
│   └── ci.yml                  # GitHub Actions pipeline
├── src/
│   ├── locators/               # XPath selectors only
│   │   ├── login_page_locators.py
│   │   └── inventory_page_locators.py
│   └── pages/                  # Page actions
│       ├── login_page.py
│       ├── inventory_page.py
│       └── sauce_demo.py       # Facade combining all pages
├── tests/
│   └── test_login_page.py
├── conftest.py                 # Session-scoped browser, context, page fixtures
├── pytest.ini                  # Default options and report path
└── requirements.txt
```

## Key Features

- **Locators separated from page objects** — selectors in `src/locators/`, actions in `src/pages/`, keeping maintenance clean
- **Session-scoped fixtures** — browser and context initialised once per session for faster runs
- **Soft assertions** — `pytest-check` allows multiple checks per test without stopping on first failure
- **Parametrized tests** — login scenarios driven by parameters for easy data-driven expansion
- **Auto teardown** — fixture handles logout after each test, keeping state clean between runs
- **CI pipeline** — GitHub Actions runs full suite headlessly on every push to main and uploads HTML report as artifact

## Setup

```bash
# Clone the repo
git clone https://github.com/Suryaekan/saucedemo-automation.git
cd saucedemo-automation

# Create virtual environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
python -m playwright install chromium
```

## Running Tests

```bash
# Run all tests
pytest -v

# Run a specific file
pytest tests/test_login_page.py -v

# Run tests matching a keyword
pytest -k login -v

# Run in parallel
pytest -n auto
```

HTML report is auto-generated at `artifacts/reports/report.html` after each run.

## CI

GitHub Actions runs on every push and pull request to `main`:
- Sets up Python 3.12
- Installs dependencies and Playwright Chromium
- Runs full test suite headlessly
- Uploads HTML report as a workflow artifact

## Test Coverage

| Module | Scenarios |
|---|---|
| Login | Valid credentials — successful login and dashboard load |
| Login | Locked out user — error message validation (parametrized, env-var driven) |
| Logout | Auto teardown via fixture after each test |
