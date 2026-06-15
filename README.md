# Sauce Demo Automation Framework

A UI automation framework built using **Playwright**, **Python**, and **Pytest** to validate core user workflows on the Sauce Demo web application.

The framework follows the **Page Object Model (POM)** design pattern, separating locators, page actions, test logic, and fixtures to ensure maintainability, scalability, and clean test architecture.

---

## 🎯 Framework Highlights

### Page Object Model

The framework follows POM principles:

- Locators stored separately from page actions
- Test cases remain readable and maintainable
- Easier locator updates when UI changes
- Reusable page methods across test suites

### Reusable Fixtures

Pytest fixtures are used for:

- Browser lifecycle management
- Context creation
- Page initialization
- Login setup

### Logging

Centralized logging utility provides:

- Structured execution logs
- Easier debugging
- Cleaner test output

### Reporting

The framework generates:

- HTML execution reports
- Test result summaries
- Failure details

### CI/CD Ready

GitHub Actions automatically:

- Installs dependencies
- Installs Playwright browsers
- Executes test suite
- Uploads generated reports

---

## ✅ Current Test Coverage

### Inventory Dashboard

#### Product Sorting Validation

- Sort products by Name (A → Z)
- Sort products by Name (Z → A)
- Sort products by Price (Low → High)
- Sort products by Price (High → Low)

Each test validates actual product ordering rather than only verifying UI interactions.

---

## 🛠 Setup

### Clone Repository

```bash
git clone https://github.com/Suryaekan/saucedemo-automation.git
cd saucedemo-automation
```

### Create Virtual Environment

Linux / Mac:

```bash
python -m venv .venv
source .venv/bin/activate
```

Windows:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Install Playwright Browser

```bash
python -m playwright install chromium
```

---

## 🔐 Environment Variables

Credentials are read from environment variables.

Linux / Mac:

```bash
export username=standard_user
export password=secret_sauce
```

Windows PowerShell:

```powershell
$env:username="standard_user"
$env:password="secret_sauce"
```

---

## ▶ Running Tests

Run complete test suite:

```bash
pytest -v
```

Run inventory tests:

```bash
pytest -m inventory_page -v
```

Run tests in parallel:

```bash
pytest -n auto
```

Generate HTML report:

```bash
pytest -v
```

---

## 📊 Reports

HTML reports are generated automatically after execution.

Default report location:

```text
artifacts/reports/report.html
```

The report contains:

- Pass/Fail status
- Execution duration
- Assertion failures
- Environment information

---

## ⚙ GitHub Actions CI Pipeline

The project includes a GitHub Actions workflow that:

1. Checks out the repository
2. Sets up Python 3.12
3. Installs dependencies
4. Installs Playwright Chromium
5. Executes the test suite
6. Uploads generated reports as workflow artifacts

Workflow file:

```text
.github/workflows/ci.yml
```

---

## 🧪 Sample Execution

Run all tests:

```bash
pytest -v
```

Example output:

```text
tests/test_inventory_dashboard.py::test_sort_items_by_name_in_ascending_order PASSED
tests/test_inventory_dashboard.py::test_sort_items_by_name_in_descending_order PASSED
tests/test_inventory_dashboard.py::test_sort_items_by_price_in_ascending_order PASSED
tests/test_inventory_dashboard.py::test_sort_items_by_price_in_descending_order PASSED
```

---

## 📈 Future Enhancements

Planned improvements:

- Login validation scenarios
- Invalid credential validation
- Cart functionality tests
- Checkout workflow tests
- Screenshot capture on failures
- Playwright traces on failures
- Function-scoped browser contexts for improved test isolation
- Migration from XPath selectors to Playwright-friendly `data-test` selectors
- Integration with Allure Reporting

---

## 💡 Why This Project?

This project was created to demonstrate:

- Playwright automation skills
- Pytest framework development
- Page Object Model implementation
- CI/CD integration using GitHub Actions
- Clean automation architecture and best practices

The framework is intentionally structured to resemble real-world automation projects used in modern QA and SDET teams.

---

## 👨‍💻 Author

**Surya Vijay**

Automation Test Engineer

- Python
- Playwright
- Pytest
- REST API Testing
- MongoDB Validation
- CI/CD Automation

GitHub: https://github.com/Suryaekan

LinkedIn: https://linkedin.com/in/surya-vijay-962125313