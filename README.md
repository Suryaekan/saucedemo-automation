# Sauce Demo automation

End-to-end UI tests for [Sauce Demo](https://www.saucedemo.com/) using [Playwright](https://playwright.dev/python/) and [pytest](https://pytest.org/). The suite follows a page object pattern: locators live under `src/locators/`, page actions under `src/pages/`, and scenarios under `tests/`.

## Requirements

- Python **3.12** (matches CI)
- pip

## Setup

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
python -m playwright install chromium
```

## Run tests

From the repository root (so `src` is importable as in CI):

```bash
pytest -v
```

Default options (see `pytest.ini`) generate a self-contained HTML report at `artifacts/reports/report.html`. Open that file in a browser after a run.

Useful variants:

```bash
pytest tests/test_login_page.py -v          # single file
pytest -k login -v                          # tests matching a name fragment
pytest -n auto                              # parallel workers (pytest-xdist)
```

## Project layout

| Path | Role |
|------|------|
| `conftest.py` | Session-scoped Playwright browser, context, and page; opens Sauce Demo once per session |
| `src/locators/` | XPath (and other) selectors |
| `src/pages/` | Page objects (`LoginPage`, `InventoryPage`, `SauceDemo` facade) |
| `tests/` | Pytest modules |
| `artifacts/reports/` | HTML report output (gitignored) |

## CI

GitHub Actions (`.github/workflows/ci.yml`) runs on pushes and pull requests to `main`: installs dependencies, installs Chromium for Playwright, runs `pytest -v`, and uploads the HTML report as a workflow artifact.

## Notes

- Tests run **headless** with a 1 second slow motion delay (`conftest.py`), which helps stability when debugging locally; adjust `slow_mo` or `headless` there if you need a visible browser or faster runs.
