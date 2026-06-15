class DashboardLocators:
    def __init__(self):
        self.dashboard_header_xpath = "//div[@data-test='primary-header']"
        self.dashboard_menu_button_xpath = "//div[@class='bm-burger-button']"
        self.product_sort_container_xpath = "//select[@data-test='product-sort-container']"

class InventoryItemLocators:
    def __init__(self):
        self.inventory_item_price_xpath = "//div[@data-test='inventory-item-price']"
        self.inventory_item_name_xpath = "//div[@data-test='inventory-item-name']"


class SidebarMenuLocators:
    def __init__(self):
        self.logout_link_button_xpath = "//a[@data-test='logout-sidebar-link']"
