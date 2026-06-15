import logging
from typing import Generator

import pytest
import pytest_check
from playwright.sync_api import Page

from src.logutil import get_logger
from src.pages.sauce_demo import SauceDemo

logger: logging.Logger = get_logger(__name__)

class TestInventory:

    @pytest.fixture(scope="function")
    def get_test_instance(self, page: Page) -> Generator[SauceDemo, None, None]:
        sauce_demo = SauceDemo(page=page)
        sauce_demo.inventory_page.wait_for_dashboard_to_be_visible()
        yield sauce_demo

    @pytest.mark.inventory_page
    def test_sort_items_by_name_in_ascending_order(
        self, get_test_instance: SauceDemo
    )-> None:
        get_test_instance.inventory_page.select_sort_by_name_ascending_order()
        listed_items = (
            get_test_instance.inventory_page.get_name_of_all_listed_items()
        )
        pytest_check.equal(
            sorted(listed_items),
            listed_items,
            "The items are not sorted in ascending order according to their names",
        )
        logger.info("Successfully verified sorting of items based Ascending order of item names ")

    @pytest.mark.inventory_page
    def test_sort_items_by_name_in_descending_order(
        self, get_test_instance: SauceDemo
    ) -> None:
        get_test_instance.inventory_page.select_sort_by_name_descending_order()
        listed_items = (
            get_test_instance.inventory_page.get_name_of_all_listed_items()
        )
        pytest_check.equal(
            sorted(listed_items, reverse=True),
            listed_items,
            "The items are not sorted in descending order according to their names",
        )
        logger.info("Successfully verified sorting of items based Descending order of item names ")

    @pytest.mark.inventory_page
    def test_sort_items_by_price_in_ascending_order(
        self, get_test_instance: SauceDemo
    )-> None:
        get_test_instance.inventory_page.select_sort_by_price_ascending_order()
        item_prices = (
            get_test_instance.inventory_page.get_price_of_all_listed_items()
        )
        pytest_check.equal(
            sorted(item_prices),
            item_prices,
            "The items are not sorted in ascending order according to their prices",
        )
        logger.info("Successfully verified sorting of items based on low price to high price ")

    @pytest.mark.inventory_page
    def test_sort_items_by_price_in_descending_order(
        self, get_test_instance: SauceDemo
    )->  None:
        get_test_instance.inventory_page.select_sort_by_price_descending_order()
        item_prices = (
            get_test_instance.inventory_page.get_price_of_all_listed_items()
        )
        pytest_check.equal(
            sorted(item_prices, reverse=True),
            item_prices,
            "The items are not sorted in descending order according to their prices",
        )
        logger.info("Successfully verified sorting of items based on high price to high price")

