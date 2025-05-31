from demostore_automation.src.selenium_extended.SeleniumExtended import SeleniumExtended
from demostore_automation.src.pages.locators.LostPasswordPageLocators import LostPasswordPageLocators
from demostore_automation.src.configs.MainConfigs import MainConfigs

class LostPasswordPage(LostPasswordPageLocators):

    endpoint = '/my-account/lost-password/'

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_lost_password_page(self):
        base_url = MainConfigs.get_base_url()
        my_account_url = base_url + self.endpoint
        self.driver.get(my_account_url)

    def input_username_or_email(self, username):
        self.sl.wait_and_input_text(self.LOSTPASSWORD_USER_NAME, username)

    def click_reset_password(self):
        self.sl.wait_and_click(self.RESET_PASSWORD_BUTTON)

    def wait_until_message_is_displayed(self, exp_err):
        self.sl.wait_until_element_contains_text(self.MESSAGE_UL, exp_err)

    def wait_until_error_is_displayed(self, exp_err):
        self.sl.wait_until_element_contains_text(self.ERROR_UL, exp_err)

    def get_breadcrumb(self):
        return self.sl.wait_and_get_text(self.BREADCRUMB)

    def get_lost_password_page_title(self):
        return self.sl.wait_and_get_text(self.PAGE_TITLE)

    def get_username_label(self):
        return self.sl.wait_and_get_text(self.USERNAME_LABEL)