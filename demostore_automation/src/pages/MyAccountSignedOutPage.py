
from demostore_automation.src.pages.locators.MyAccountSignedOutPageLocators import MyAccountSignedOutPageLocators

from demostore_automation.src.selenium_extended.SeleniumExtended import SeleniumExtended

from demostore_automation.src.configs.MainConfigs import MainConfigs

class MyAccountSignedOutPage(MyAccountSignedOutPageLocators):

    endpoint = '/my-account/'


    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_my_account(self):
        base_url = MainConfigs.get_base_url()
        my_account_url = base_url + self.endpoint
        self.driver.get(my_account_url)

    def input_login_username(self, username):
        self.sl.wait_and_input_text(self.LOGIN_USER_NAME, username)

    def input_login_password(self, password):
        self.sl.wait_and_input_text(self.LOGIN_USER_PASSWORD, password)

    def click_login_button(self):
        self.sl.wait_and_click(self.LOGIN_BTN)

    def wait_until_error_is_displayed(self, exp_err):
        self.sl.wait_until_element_contains_text(self.ERRORS_UL, exp_err)

    def input_register_email(self, email):
        self.sl.wait_and_input_text(self.REGISTER_EMAIL, email)

    def input_register_password(self, password):
        self.sl.wait_and_input_text(self.REGISTER_PASSWORD, password)

    def click_register_button(self):
        self.sl.wait_and_click(self.REGISTER_BTN)

    def get_username_label(self):
        return self.sl.wait_and_get_text(self.USERNAME_LABEL)

    def get_password_label(self):
        return self.sl.wait_and_get_text(self.PASSWORD_LABEL)

    def get_login_form_heading(self):
        return self.sl.wait_and_get_text(self.LOGIN_FORM_LABEL)

    def get_registration_form_heading(self):
        return self.sl.wait_and_get_text(self.REG_FORM_LABEL)

    def get_reg_email_label(self):
        return self.sl.wait_and_get_text(self.EMAIL_REG_LABEL)

    def get_reg_password_label(self):
        return self.sl.wait_and_get_text(self.PASSWORD_REG_LABEL)

    def get_breadcrumb(self):
        return self.sl.wait_and_get_text(self.BREADCRUMB)

    def get_my_account_page_title(self):
        return self.sl.wait_and_get_text(self.PAGE_TITLE)

    def click_lost_your_password(self):
        return self.sl.wait_and_click(self.LOST_YOUR_PASSWORD)

