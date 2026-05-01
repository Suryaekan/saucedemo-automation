class DashboardLocators:
    def __init__(self):
        self.dashboard_header_xpath = "//div[@data-test='primary-header']"
        self.dashboard_menu_button_xpath = "//div[@class='bm-burger-button']"


class SidebarMenuLocators:
    def __init__(self):
        self.logout_link_button_xpath = "//a[@data-test='logout-sidebar-link']"
