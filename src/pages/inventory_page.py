from playwright.sync_api import Page

from src.locators.inventory_page_locators import DashboardLocators, SidebarMenuLocators


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.dashboard_locators = DashboardLocators()

    def wait_for_dashboard_to_be_visible(self) -> None:
        self.page.locator(self.dashboard_locators.dashboard_header_xpath).wait_for(
            state="visible"
        )

    def is_dashboard_visible(self) -> bool:
        return self.page.locator(
            self.dashboard_locators.dashboard_header_xpath
        ).is_visible()

    def click_on_menu_button(self) -> None:
        self.page.locator(self.dashboard_locators.dashboard_menu_button_xpath).click()


class InventorySidebarPage:
    def __init__(self, page: Page):
        self.page = page
        self.menu_locators = SidebarMenuLocators()

    def click_on_logout_link_button(self):
        self.page.locator(self.menu_locators.logout_link_button_xpath).click()
