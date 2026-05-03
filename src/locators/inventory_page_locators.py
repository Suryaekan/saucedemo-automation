"""Locators for the inventory UI and sidebar."""


class DashboardLocators:
    """Locators for the inventory page"""

    def __init__(self) -> None:
        self.dashboard_header_xpath = "//div[@data-test='primary-header']"
        self.dashboard_menu_button_xpath = "//div[@class='bm-burger-button']"


class SidebarMenuLocators:
    """Locators for the slide-out sidebar menu."""

    def __init__(self) -> None:
        self.logout_link_button_xpath = "//a[@data-test='logout-sidebar-link']"
