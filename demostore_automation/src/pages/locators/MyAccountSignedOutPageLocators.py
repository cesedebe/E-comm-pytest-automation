
from selenium.webdriver.common.by import By

class MyAccountSignedOutPageLocators:

    LOGIN_USER_NAME = (By.ID, 'username')
    LOGIN_USER_PASSWORD = (By.ID, 'password')
    LOGIN_BTN = (By.CSS_SELECTOR, 'button.woocommerce-button[name="login"]')

    ERRORS_UL = (By.CSS_SELECTOR, 'ul.woocommerce-error')

    REGISTER_EMAIL = (By.ID, 'reg_email')
    REGISTER_PASSWORD = (By.ID, 'reg_password')
    REGISTER_BTN = (By.CSS_SELECTOR, 'button[name="register"][value="Register"]')

    USERNAME_LABEL = (By.CSS_SELECTOR, 'label[for="username"]')
    PASSWORD_LABEL = (By.CSS_SELECTOR, 'label[for="password"]')
    EMAIL_REG_LABEL = (By.CSS_SELECTOR, 'label[for="reg_email"]')
    PASSWORD_REG_LABEL = (By.CSS_SELECTOR, 'label[for="reg_password"]')

    LOGIN_FORM_LABEL = (By.CSS_SELECTOR, 'div.u-column1.col-1 h2')
    REG_FORM_LABEL = (By.CSS_SELECTOR, 'div.u-column2.col-2 h2')

    BREADCRUMB = (By.CLASS_NAME, 'woocommerce-breadcrumb')
    PAGE_TITLE = (By.CLASS_NAME, 'entry-title')