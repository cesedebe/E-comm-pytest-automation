from demostore_automation.src.configs.MainConfigs import MainConfigs
from demostore_automation.src.selenium_extended.SeleniumExtended import SeleniumExtended
from demostore_automation.src.pages.locators.ProductPageLocators import ProductPageLocators

import logging as logger


class ProductPage(ProductPageLocators):
    """
    A class representing the product page.
    Attributes:
    driver : Instance of Selenium WebDriver
    sl (SeleniumExtended) : Instance of SeleniumExtended
    """
    endpoint = '/product'

    def __init__(self, driver):
        """
        Initializes a ProductPage object with driver and sl.
        """
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_product_page(self, product_name):
        """
        Takes browser to product page.
        Parameters:
        product_name(str): Name of the product
        Returns:
        None
        """
        base_url = MainConfigs.get_base_url()
        url = base_url + self.endpoint + '/' + product_name.replace(' ', '-').lower()
        # url = f"{base_url}{self.endpoint}/{product_name.replace(' ', '-').lower()}"
        logger.info(f"Navigatign to product page at url: {url}")
        self.sl.go_to_url(url)

    def get_displayed_product_name(self):
        """
        Gets displayed product name
        Parameters:
        None
        Returns:
        displayed_name(str): Displayed product name
        """
        logger.info("Getting product name")
        displayed_name = self.sl.wait_and_get_text(self.PRODUCT_TITLE)
        logger.debug(f"Displayed product name: {displayed_name}")

        return displayed_name

    def get_url_of_displayed_main_image(self):
        """
        Gets URL of the displayed main image.
        Parameters:
        None
        Returns:
        image_url(str): Url of the product image
        """
        # first get the image element
        image_element = self.sl.wait_until_element_is_visible(self.PRODUCT_IMAGE_MAIN)

        # then get the src attribute of the element
        image_url = image_element.get_attribute("src")

        return image_url