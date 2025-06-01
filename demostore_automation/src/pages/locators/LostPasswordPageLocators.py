
from selenium.webdriver.common.by import By

class LostPasswordPageLocators:

    LOSTPASSWORD_USER_NAME = (By.CLASS_NAME, 'woocommerce-Input')
    RESET_PASSWORD_BUTTON = (By.CLASS_NAME, 'woocommerce-Button')
    MESSAGE_UL  = (By.CLASS_NAME, "woocommerce-message")
    ERROR_UL  = (By.CLASS_NAME, "woocommerce-error")
    BREADCRUMB = (By.CLASS_NAME, "woocommerce-breadcrumb")
    PAGE_TITLE = (By.CLASS_NAME, "entry-title")
    USERNAME_LABEL  = (By.CSS_SELECTOR, 'label[for="user_login"]')
