"""Locators for the inventory UI and sidebar."""


class DashboardLocators:
    """Locators for the inventory page"""

    def __init__(self) -> None:
        self.dashboard_header_xpath = "//div[@data-test='primary-header']"
        self.dashboard_menu_button_xpath = "//div[@class='bm-burger-button']"
        self.product_sort_container_xpath = "//select[@data-test='product-sort-container']"

class InventoryItemLocators:
    def __init__(self):
        self.inventory_item_price_xpath = "//div[@data-test='inventory-item-price']"
        self.inventory_item_name_xpath = "//div[@data-test='inventory-item-name']"


class SidebarMenuLocators:
    """Locators for the slide-out sidebar menu."""

    def __init__(self) -> None:
        self.logout_link_button_xpath = "//a[@data-test='logout-sidebar-link']"
