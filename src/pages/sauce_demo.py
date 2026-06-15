"""Facade wiring login, inventory, and sidebar page objects."""

from __future__ import annotations

from playwright.sync_api import Page

from src.pages.inventory_page import InventoryPage, InventorySidebarPage
from src.pages.login_page import LoginPage


class SauceDemo:
    """Single entry point for Sauce Demo flows built on one Playwright ``Page``."""

    def __init__(self, page: Page) -> None:
        self.login_page = LoginPage(page)
        self.inventory_page = InventoryPage(page)
        self.sidebar_page = InventorySidebarPage(page)
