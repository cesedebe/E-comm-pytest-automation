
from selenium.webdriver.common.by import By

class MyAccountSignedInPageLocators:

    LEFT_NAV_LOGOUT_BTN = (By.CSS_SELECTOR, 'li.woocommerce-MyAccount-navigation-link--customer-logout a')

    LEFT_NAV = (By.CLASS_NAME, 'woocommerce-MyAccount-navigation')

    DISPLAY_NAME = (By.CSS_SELECTOR, "#post-9 > div > div > div > p:nth-child(2) > strong:nth-child(1)")

    PAGE_TITLE = (By.CLASS_NAME, "entry-title" )

    BREADCRUMB = (By.CLASS_NAME, "woocommerce-breadcrumb")
