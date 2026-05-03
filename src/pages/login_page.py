"""Page object for the Sauce Demo login screen."""

from __future__ import annotations

import logging

from playwright.sync_api import Page

from src.locators.login_page_locators import LoginLocators
from src.logutil import get_logger

logger: logging.Logger = get_logger(__name__)


class LoginPage:
    """Encapsulates actions and checks on https://www.saucedemo.com/ login UI."""

    def __init__(self, page: Page) -> None:
        """
        Args:
            page: Playwright page already on (or navigating to) Sauce Demo.

        Returns:
            None
        """
        self.page = page
        self.login_locators = LoginLocators()

    def wait_for_login_page_to_load(self) -> None:
        """Wait until the login container is visible.

        Returns:
            None
        """
        logger.debug("Waiting for login page container")
        self.page.locator(
            self.login_locators.login_page_container_xpath
        ).wait_for(state="visible")
        logger.info("Login page is visible")

    def is_login_page_loaded(self) -> bool:
        """Check whether the login container is visible.

        Returns:
            ``True`` if the login container locator is visible.
        """
        return self.page.locator(
            self.login_locators.login_page_container_xpath
        ).is_visible()

    def enter_text_in_username_field(self, username: str) -> None:
        """Fill the username field.

        Args:
            username: Sauce Demo username. Logged at DEBUG only, not at INFO.

        Returns:
            None
        """
        logger.info("Entering username")
        logger.debug("Username value: %s", username)
        self.page.locator(
            self.login_locators.username_text_field_xpath
        ).fill(username)

    def enter_text_in_password_field(self, password: str) -> None:
        """Fill the password field (value is never written to logs).

        Args:
            password: Sauce Demo password.

        Returns:
            None
        """
        logger.info("Entering password (value not logged)")
        self.page.locator(
            self.login_locators.password_text_field_xpath
        ).fill(password)

    def click_login_button(self) -> None:
        """Click the login submit control.

        Returns:
            None
        """
        logger.info("Clicking login button")
        self.page.locator(self.login_locators.login_button_xpath).click()

    def get_error_text_msg(self) -> str:
        """Read the login error banner text.

        Returns:
            Inner text of the error container element.
        """
        return self.page.locator(self.login_locators.error_message_xpath).inner_text()
