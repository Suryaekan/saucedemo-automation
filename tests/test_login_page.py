"""Tests for Sauce Demo login Page."""

from __future__ import annotations

from collections.abc import Generator
import logging

import pytest
import pytest_check as check
from playwright.sync_api import Page

from src.logutil import get_logger
from src.pages.sauce_demo import SauceDemo

logger: logging.Logger = get_logger(__name__)


class TestLoginPage:
    """Login scenarios against the shared session ``page`` fixture."""

    @pytest.fixture(scope="function")
    def get_test_instance(self, page: Page) -> Generator[SauceDemo, None, None]:
        """Build ``SauceDemo`` on the session page and reset to login after the test.

        Args:
            page: Session-scoped Playwright page (from ``conftest``).

        Yields:
            Configured ``SauceDemo`` instance with login screen ready.
        """
        logger.info("Step: Arrange — load SauceDemo and wait for login page")
        sauce_demo = SauceDemo(page=page)
        sauce_demo.login_page.wait_for_login_page_to_load()
        yield sauce_demo
        # Teardown: return to a clean login state for other tests sharing the session page.
        if sauce_demo.inventory_page.is_dashboard_visible():
            logger.info("Step: Teardown — logging out to reset session page")
            sauce_demo.inventory_page.click_on_menu_button()
            sauce_demo.sidebar_page.click_on_logout_link_button()
            sauce_demo.login_page.wait_for_login_page_to_load()
            sauce_demo.login_page.is_login_page_loaded()

    @pytest.mark.parametrize("username", ["standard_user"])
    @pytest.mark.parametrize("password", ["secret_sauce"])
    def test_login_successful(
        self, get_test_instance: SauceDemo, username: str, password: str
    ) -> None:
        """Valid credentials should land on the inventory dashboard.

        Args:
            get_test_instance: Function-scoped ``SauceDemo`` fixture.
            username: Parametrized Sauce Demo username.
            password: Parametrized Sauce Demo password.

        Returns:
            None
        """
        login_page = get_test_instance.login_page
        inventory_page = get_test_instance.inventory_page

        logger.info("Step: Act — submit valid username and password")
        login_page.enter_text_in_username_field(username=username)
        login_page.enter_text_in_password_field(password=password)
        login_page.click_login_button()

        logger.info("Step: Assert — inventory dashboard is visible")
        check.is_true(
            inventory_page.is_dashboard_visible(),
            "Expected Inventory page to be loaded for valid login creds but login failed ",
        )

    @pytest.mark.parametrize("username", ["locked_out_user"])
    @pytest.mark.parametrize("password", ["secret_sauce"])
    def test_login_locked_out_user(
        self, get_test_instance: SauceDemo, username: str, password: str
    ) -> None:
        """Locked-out user should see an error and not reach inventory.

        Args:
            get_test_instance: Function-scoped ``SauceDemo`` fixture.
            username: Parametrized username (expected ``locked_out_user``).
            password: Parametrized password.

        Returns:
            None
        """
        if not username:
            pytest.fail("username not provided, please enter a valid username")
        if not password:
            pytest.fail("password not provided, please enter a valid username")

        login_page = get_test_instance.login_page
        inventory_page = get_test_instance.inventory_page

        login_page.enter_text_in_username_field(username=username)
        login_page.enter_text_in_password_field(password=password)
        login_page.click_login_button()
        check.is_false(
            inventory_page.is_dashboard_visible(),
            "Expected Inventory page to not be loaded for locked out user, but login succeeded ",
        )
        check.equal(
            login_page.get_error_text_msg(),
            "Epic sadface: Sorry, this user has been locked out.",
            f"Expected error message to contain user locked out message, got: {login_page.get_error_text_msg()} instead ",
        )
