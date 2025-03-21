
from selenium.webdriver.common.by import By

class CartPageLocators:
    """
    A class representing the cart page locators.
    Attributes:
    None
    """
    PRODUCT_NAMES_IN_CART = (By.CSS_SELECTOR, 'a.wc-block-components-product-name')

    COUPON_FIELD = (By.ID, 'wc-block-components-totals-coupon__input-0')
    APPLY_COUPON_BTN = (By.CSS_SELECTOR, '#wc-block-components-totals-coupon__form > button')

    PROCEED_TO_CHECKOUT_BTN = (By.CSS_SELECTOR, 'span.wc-block-components-button__text')
    APPLY_COUPON_TEXT_BTN = (By.CSS_SELECTOR, 'svg.wc-block-components-panel__button-icon')
    COUPON_CONFIRMED = (By.CSS_SELECTOR, 'span.wc-block-components-chip__text')