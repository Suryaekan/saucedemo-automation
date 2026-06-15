from playwright.sync_api import Page

from src.locators.inventory_page_locators import DashboardLocators, SidebarMenuLocators, InventoryItemLocators


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.dashboard_locators = DashboardLocators()
        self.inventory_item_locators = InventoryItemLocators()

    def wait_for_dashboard_to_be_visible(self) -> None:
        self.page.locator(self.dashboard_locators.dashboard_header_xpath).wait_for(
            state="visible", timeout=10000
        )

    def is_dashboard_visible(self) -> bool:
        return self.page.locator(
            self.dashboard_locators.dashboard_header_xpath
        ).is_visible(timeout=10000)

    def click_on_menu_button(self) -> None:
        self.page.locator(self.dashboard_locators.dashboard_menu_button_xpath).click(timeout=10000)

    def click_on_product_sort_container(self):
        self.page.locator(self.dashboard_locators.product_sort_container_xpath).click(timeout=10000)

    def get_price_of_all_listed_items(self) -> list[float]:
        float_prices = []
        prices = (self.page.locator(self.inventory_item_locators.inventory_item_price_xpath)).all_text_contents()
        for price in prices:
            float_prices.append(price.lstrip('$'))
        return float_prices

    def get_name_of_all_listed_items(self) -> list[str]:
        return (self.page.locator(self.inventory_item_locators.inventory_item_name_xpath)).all_text_contents()

    def select_sort_by_name_ascending_order(self):
        self.page.locator(self.dashboard_locators.product_sort_container_xpath).select_option(label="Name (A to Z)", timeout=10000)

    def select_sort_by_name_descending_order(self):
        self.page.locator(self.dashboard_locators.product_sort_container_xpath).select_option(label="Name (Z to A)", timeout=10000)

    def select_sort_by_price_ascending_order(self):
        self.page.locator(self.dashboard_locators.product_sort_container_xpath).select_option(label="Price (low to high)", timeout=10000)

    def select_sort_by_price_descending_order(self):
        self.page.locator(self.dashboard_locators.product_sort_container_xpath).select_option(label="Price (high to low)]", timeout=10000)

class InventorySidebarPage:
    def __init__(self, page: Page):
        self.page = page
        self.menu_locators = SidebarMenuLocators()

    def click_on_logout_link_button(self):
        self.page.locator(self.menu_locators.logout_link_button_xpath).click(timeout=10000)
