import os
from typing import Any, Generator

import pytest
import pytest_check as check
from src.pages.sauce_demo import SauceDemo
from playwright.sync_api import Page


class TestLoginPage:

    @pytest.fixture(scope="function")
    def get_test_instance(self, page: Page) -> Generator[SauceDemo, None, None]:
        sauce_demo = SauceDemo(page=page)
        sauce_demo.login_page.wait_for_login_page_to_load()
        yield sauce_demo
        if sauce_demo.inventory_page.is_dashboard_visible():
            sauce_demo.inventory_page.click_on_menu_button()
            sauce_demo.sidebar_page.click_on_logout_link_button()
            sauce_demo.login_page.wait_for_login_page_to_load()
            sauce_demo.login_page.is_login_page_loaded()

    # @pytest.mark.parametrize("username", ["standard_user"])
    # @pytest.mark.parametrize("password", ["secret_sauce"])
    # def test_login_successful(
    #     self, get_test_instance, username: str, password: str
    # ) -> None:
    #     login_page = get_test_instance.login_page
    #     inventory_page = get_test_instance.inventory_page
    #
    #     login_page.enter_text_in_username_field(username=username)
    #     login_page.enter_text_in_password_field(password=password)
    #     login_page.click_login_button()
    #     check.is_true(
    #         inventory_page.is_dashboard_visible(),
    #         "Expected Inventory page to be loaded for valid login creds but login failed ",
    #     )

    @pytest.mark.parametrize("username", [os.getenv("username")])
    @pytest.mark.parametrize("password", [os.getenv("password")])
    def test_login_locked_out_user(
        self, get_test_instance, username: str, password: str
    ) -> None:
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
