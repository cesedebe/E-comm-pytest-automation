

from demostore_automation.src.selenium_extended.SeleniumExtended import SeleniumExtended
from demostore_automation.src.pages.locators.CartPageLocators import CartPageLocators
from demostore_automation.src.configs.MainConfigs import MainConfigs


class CartPage(CartPageLocators):
    """
    A class representing the cart page.
    Attributes:
    driver : Instance of Selenium WebDriver
    sl (SeleniumExtended) : Instance of SeleniumExtended
    """
    endpoint = '/cart'

    def __init__(self, driver):
        """
        Initializes a CartPage object with driver and sl.
        """
        self.driver = driver
        self.sl = SeleniumExtended(driver)

    def go_to_cart_page(self):
        """
        Goes to cart page.
        Parameters:
        None
        Returns:
        None
        """
        base_url = MainConfigs.get_base_url()
        cart_url = base_url + self.endpoint
        self.driver.get(cart_url)

    def get_all_product_names_in_cart(self):
        """
        Get all products in cart.
        Parameters:
        None
        Returns:
        product_name(str): Names of all products in cart
        """
        product_name_elements = self.sl.wait_and_get_elements(self.PRODUCT_NAMES_IN_CART)
        product_names = [i.text for i in product_name_elements]
        # product_names = []
        # for i in product_name_elements:
        #     product_names.append(i.text)
        return product_names

    def input_coupon(self, coupon_code):
        """
        Inputs the coupon code.
        Parameters:
        coupon_code(str): Coupon code
        Returns:
        None
        """
        self.sl.wait_and_click(self.APPLY_COUPON_TEXT_BTN)
        self.sl.wait_and_input_text(self.COUPON_FIELD, str(coupon_code))

    def click_apply_coupon(self):
        """
        Clicks apply coupon button.
        Parameters:
        None
        Returns:
        None
        """
        self.sl.wait_and_click(self.APPLY_COUPON_BTN)

    def apply_coupon(self, coupon_code):
        """
        Inputs coupon code and clicks apply coupon button.
        Parameters:
        coupon_code(str): Coupon code
        Returns:
        None
        """
        self.input_coupon(coupon_code)
        self.click_apply_coupon()

    def click_on_proceed_to_checkout(self):
        """
        Clicks on proceed to checkout button.
        Parameters:
        None
        Returns:
        None
        """
        self.sl.wait_and_click(self.PROCEED_TO_CHECKOUT_BTN)

    def check_coupon_applied(self):
        """
        Checks if coupon has been applied successfully.
        Parameters:
        None
        Returns:
        None
        """
        self.sl.wait_until_element_is_visible(self.COUPON_CONFIRMED)