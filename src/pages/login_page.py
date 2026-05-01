from playwright.sync_api import Page

from src.locators.login_page_locators import LoginLocators


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.login_locators = LoginLocators()

    def wait_for_login_page_to_load(self):
        self.page.locator(
            self.login_locators.login_page_container_xpath
        ).wait_for(state="visible")

    def is_login_page_loaded(self) -> bool:
        """
        TBD
        """
        return self.page.locator(
            self.login_locators.login_page_container_xpath
        ).is_visible()

    def enter_text_in_username_field(self, username: str) -> None:
        """
        TBD
        """
        self.page.locator(
            self.login_locators.username_text_field_xpath
        ).fill(username)

    def enter_text_in_password_field(self, password: str) -> None:
        """
        TBD
        """
        self.page.locator(
            self.login_locators.password_text_field_xpath
        ).fill(password)

    def click_login_button(self) -> None:
        """
        TBD
        """
        self.page.locator(self.login_locators.login_button_xpath).click()

    def get_error_text_msg(self) -> str:
        return self.page.locator(self.login_locators.error_message_xpath).inner_text()
