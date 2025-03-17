
from selenium.webdriver.common.by import By

class ProductPageLocators:
    """
    A class representing the cart page locators.
    Attributes:
    None
    """
    PRODUCT_TITLE = (By.CSS_SELECTOR, 'div.summary.entry-summary h1.product_title')
    PRODUCT_IMAGE_MAIN = (By.CSS_SELECTOR, 'div.woocommerce-product-gallery__image img.wp-post-image')