class LoginLocators:
    def __init__(self):
        self.login_page_container_xpath = "//div[@data-test='login-container']"
        self.username_text_field_xpath = "//input[@data-test='username']"
        self.password_text_field_xpath = "//input[@data-test='password']"
        self.login_button_xpath = "//input[@data-test='login-button']"
        self.error_message_xpath = "//div[@class='error-message-container error']"
        
