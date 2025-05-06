
from demostore_automation.src.selenium_extended.SeleniumExtended import SeleniumExtended
from demostore_automation.src.pages.locators.MyAccountSignedInPageLocators import MyAccountSignedInPageLocators


class MyAccountSignedInPage(MyAccountSignedInPageLocators):

    def __init__(self, driver):
        self.sl = SeleniumExtended(driver)

    def verify_user_is_signed_in(self):
        """
        Verifies user is signed in by checking the 'Log Out' button is visible
        on the left navigation bar.
        :return:
        """
        self.sl.wait_until_element_is_visible(self.LEFT_NAV_LOGOUT_BTN)

    def get_left_nav_bar(self):
        return self.sl.wait_and_get_text(self.LEFT_NAV)

    def verify_user_is_signed_out(self):
        self.sl.wait_until_element_is_visible(self.LEFT_NAV_LOGOUT_BTN)
        self.sl.wait_and_click(self.LEFT_NAV_LOGOUT_BTN)

    def get_breadcrumb(self):
        return self.sl.wait_and_get_text(self.BREADCRUMB)

    def get_my_account_page_title(self):
        return self.sl.wait_and_get_text(self.PAGE_TITLE)

    def get_user_display_name(self):
        return self.sl.wait_and_get_text(self.DISPLAY_NAME)
