# Sauce Demo Automation Framework

End-to-end UI automation framework for [Sauce Demo](https://www.saucedemo.com/) built with **Playwright**, **Python**, and **Pytest**.

This project follows a clean Page Object Model structure with separate locator, page action, fixture, and test layers. The current test coverage focuses on validating inventory dashboard sorting behavior after login.

## Tech Stack

- Python 3.12
- Pytest
- Playwright
- pytest-check
- pytest-html
- pytest-xdist
- GitHub Actions

## Project Structure

```text
saucedemo-automation/
├── .github/workflows/
│   └── ci.yml
├── src/
│   ├── locators/
│   │   ├── login_page_locators.py
│   │   └── inventory_page_locators.py
│   ├── pages/
│   │   ├── login_page.py
│   │   ├── inventory_page.py
│   │   └── sauce_demo.py
│   └── logutil.py
├── tests/
│   └── test_inventory_dashboard.py
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md