
import time

from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

class SeleniumExtended:
    """
    A class representing Selenium Extended.
    Attributes:
    driver : Instance of Selenium WebDriver
    default_timeout (int) : Default timeout value
    """
    def __init__(self, driver):
        """
        Initializes a SeleniumExtended object with driver and default_timeout.
        """
        self.driver = driver
        self.default_timeout = 5

    def go_to_url(self, url):
        """
        Go to URL
        Parameters:
        url(str): URL
        Returns:
        None
        """
        self.driver.get(url)

    def wait_and_input_text(self, locator, text, timeout=None):
        """
        Wait until visibility of element then input text
        Parameters:
        locator(str): Locator
        text(str): Text to input
        timeout(int): Timeout
        Returns:
        None
        """
        timeout = timeout if timeout else self.default_timeout

        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        ).send_keys(text)

    def wait_and_click(self, locator, timeout=None):
        """
        Wait until clickability of element then click
        Parameters:
        locator(str): Locator
        timeout(int): Timeout
        Returns:
        None
        """
        timeout = timeout if timeout else self.default_timeout
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            ).click()
        except StaleElementReferenceException:
            time.sleep(2)
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator),
                message=f"Element with locator {locator}, is not clickable."
            ).click()

    def wait_until_element_contains_text(self, locator, text, timeout=None):
        """
        Wait until element contains text then
        Parameters:
        locator(str): Locator
        text(str): Text to check
        timeout(int): Timeout
        Returns:
        None
        """
        timeout = timeout if timeout else self.default_timeout

        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(locator, text),
            message=f'Element with locator = {locator}, does not contain text: "{text}", after waiting {timeout} seconds.'
        )

    def wait_until_element_is_visible(self, locator_or_element, timeout=None):
        """
        Wait until visibility of element then return element
        Parameters:
        locator_or_element(str): Locator
        timeout(int): Timeout
        Returns:
        elem(WebElement): Web Element
        """
        timeout = timeout if timeout else self.default_timeout

        if isinstance(locator_or_element, tuple):
            elem = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator_or_element),
                message=f"Element with locator {locator_or_element} not found after timeout of {timeout}"
            )
        else:
            import selenium.webdriver.remote.webelement
            if isinstance(locator_or_element, selenium.webdriver.remote.webelement.WebElement):
                elem = WebDriverWait(self.driver, timeout).until(
                    EC.visibility_of(locator_or_element),
                    message=f"Element {locator_or_element} not found after timeout of {timeout}"
                )
            else:
                raise TypeError(f"The locator to check visibility must be a 'tuple' or a 'WebElement'. It was {type(locator_or_element)}")

        return elem

    def wait_and_get_elements(self, locator, timeout=None, err=None):
        """
        Wait until element(s) is visible then return element(s)
        Parameters:
        locator(str): Locator
        timeout(int): Timeout
        err(str): Error Message
        Returns:
        elements(WebElement): Web Elements
        """
        timeout = timeout if timeout else self.default_timeout
        err = err if err else f"Unable to find elements located by '{locator}'," \
                              f"after timeout of {timeout}"
        try:
            elements = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located(locator)
            )
        except TimeoutException:
            raise TimeoutException(err)

        return elements

    def wait_and_select_dropdown(self, locator, to_select, select_by='visible_text'):
        """
        Wait until visibility of element then select dropdown
        Parameters:
        locator(str): Locator
        to_select(str): What to select
        select_by(str): How to select
        Returns:
        None
        """
        select_element = self.wait_until_element_is_visible(locator)
        select = Select(select_element)
        if select_by.lower() == 'visible_text':
            select.select_by_visible_text(to_select)
        elif select_by.lower() == 'index':
            select.select_by_index(to_select)
        elif select_by.lower() == 'value':
            select.select_by_value(to_select)
        else:
            raise Exception(f"Invalid option for 'to_select' parameter. Valid values are 'visible_text', 'index', or value 'value'.")

    def wait_and_get_text(self, locator, timeout=None):
        """
        Wait until visibility of element then get text
        Parameters:
        locator(str): Locator
        timeout(str): Timeout
        Returns:
        element_text(str): Text to get
        """
        timeout = timeout if timeout else self.default_timeout
        elm = self.wait_until_element_is_visible(locator, timeout)
        element_text = elm.text

        return element_text

    def wait_until_element_is_not_visible(self, locator, timeout=None):
        """
        Wait until element is not visible
        Parameters:
        locator(str): Locator
        timeout(int): Timeout
        Returns:
        None
        """
        timeout = timeout if timeout else self.default_timeout
        WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(locator),
                message=f"The element is still visible after timeout of {timeout}, with locator: {locator}"
            )