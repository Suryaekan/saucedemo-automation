from src.pages.inventory_page import InventoryPage, InventorySidebarPage
from src.pages.login_page import LoginPage
from playwright.sync_api import Page


class SauceDemo:
    def __init__(self, page: Page):
        self.login_page = LoginPage(page)
        self.inventory_page = InventoryPage(page)
        self.sidebar_page = InventorySidebarPage(page)
