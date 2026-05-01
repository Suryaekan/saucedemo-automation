import pytest
from playwright.sync_api import sync_playwright, Browser, BrowserContext

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        b = p.chromium.launch(headless=False, slow_mo=1000)
        yield b
        b.close()

@pytest.fixture(scope="session")
def context(browser: Browser):
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture(scope="session")
def page(context: BrowserContext):
    page = context.new_page()
    page.goto("https://www.saucedemo.com/")
    yield page
    page.close()


