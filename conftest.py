"""Pytest fixtures: session Playwright browser, context, and Sauce Demo landing page."""

from __future__ import annotations

import os

# Must run before ``from src.logutil import ...`` (key must match ``_ENV_UNDER_PYTEST`` there)
# so ``configure_logging`` skips the root StreamHandler and pytest-html avoids duplicate log blocks.
os.environ["SAUCE_DEMO_UNDER_PYTEST"] = "1"

from collections.abc import Generator
import logging
import pytest
from playwright.sync_api import (
    Browser,
    BrowserContext,
    Page,
    Playwright,
    sync_playwright,
)

from src.logutil import configure_logging, get_logger

SAUCE_DEMO_URL = "https://www.saucedemo.com/"

logger: logging.Logger = get_logger(__name__)


def pytest_configure(config: pytest.Config) -> None:
    """Enable logging before collection so page objects and tests share the same setup.

    Args:
        config: Pytest session config (unused; required by the hook specification).

    Returns:
        None
    """
    _ = config
    configure_logging()


@pytest.fixture(scope="session")
def playwright_session() -> Generator[Playwright, None, None]:
    """Keep the Playwright driver alive for the whole test session.

    Yields:
        The synchronous ``Playwright`` instance from ``sync_playwright()``.
    """
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser(playwright_session: Playwright) -> Generator[Browser, None, None]:
    """Launch Chromium once per session (headless, slow motion for stability).

    Args:
        playwright_session: Session-scoped Playwright instance.

    Yields:
        A launched Chromium ``Browser``.
    """
    logger.info("Launching Chromium (headless, slow_mo=1000ms)")
    b = playwright_session.chromium.launch(headless=True, slow_mo=1000)
    yield b
    b.close()
    logger.info("Browser closed")


@pytest.fixture(scope="session")
def context(browser: Browser) -> Generator[BrowserContext, None, None]:
    """Create one browser context shared by all tests.

    Args:
        browser: Session-scoped browser from ``browser``.

    Yields:
        A new ``BrowserContext``.
    """
    ctx = browser.new_context()
    yield ctx
    ctx.close()
    logger.info("Browser context closed")


@pytest.fixture(scope="session")
def page(context: BrowserContext) -> Generator[Page, None, None]:
    """Open a single tab on Sauce Demo for the session.
    page = context.new_page()

    Args:
        context: Session-scoped browser context.

    Yields:
        A ``Page`` navigated to ``SAUCE_DEMO_URL``.
    """
    username = os.getenv("username")
    password = os.getenv("password")
    page.goto("https://www.saucedemo.com/")
    page.locator("//input[@data-test='username']").fill(username)
    page.locator("//input[@data-test='password']").fill(password)
    page.locator("//input[@data-test='login-button']").click()
    page.wait_for_url("https://www.saucedemo.com/inventory.html")
    yield page
    page.close()
    logger.info("Page closed")
