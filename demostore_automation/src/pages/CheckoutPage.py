import time
import logging as logger

from demostore_automation.src.pages.locators.CheckoutPageLocators import CheckoutPageLocators

from demostore_automation.src.selenium_extended.SeleniumExtended import SeleniumExtended
from demostore_automation.src.utilities.genericUtilities import generate_random_email_and_password
from demostore_automation.src.configs.MainConfigs import MainConfigs

class CheckoutPage(CheckoutPageLocators):
    """
    A class representing the checkout page.
    Attributes:
    driver : Instance of Selenium WebDriver
    sl (SeleniumExtended) : Instance of SeleniumExtended
    """
    endpoint = '/checkout'

    def __init__(self, driver):
        """
        Initializes a CheckoutPage object with driver and sl.
        """
        self.driver = driver
        self.sl = SeleniumExtended(driver)

    def go_to_checkout_page(self):
        """
        Goes to checkout page.
        Parameters:
        None
        Returns:
        None
        """
        base_url = MainConfigs.get_base_url()
        checkout_url = base_url + self.endpoint
        self.driver.get(checkout_url)

    def input_billing_first_name(self, first_name=None):
        """
        Inputs billing first name.
        Parameters:
        first_name(str): Billing firstname
        Returns:
        None
        """
        first_name = first_name if first_name else 'AutomationFname'
        self.sl.wait_and_input_text(self.BILLING_FIRST_NAME_FIELD, first_name)

    def input_billing_last_name(self, last_name=None):
        """
        Inputs billing last name.
        Parameters:
        last_name(str): Billing lastname
        Returns:
        None
        """
        last_name = last_name if last_name else 'AutomationLname'
        self.sl.wait_and_input_text(self.BILLING_LAST_NAME_FIELD, last_name)

    def input_billing_street_address_1(self, address1=None):
        """
        Inputs billing Street Address.
        Parameters:
        address_1(str): Billing Address
        Returns:
        None
        """
        address1 = address1 if address1 else "123 Main st."
        self.sl.wait_and_input_text(self.BILLING_ADDRESS_1_FIELD, address1)

    def input_billing_city(self, city=None):
        """
        Inputs billing city.
        Parameters:
        city(str): Billing city
        Returns:
        None
        """
        city = 'San Francisco' if not city else city
        self.sl.wait_and_input_text(self.BILLING_CITY_FIELD, city)

    def input_billing_zip(self,  zip_code=None):
        """
        Inputs billing zipcode.
        Parameters:
        zip_code(str): Billing zipcode
        Returns:
        None
        """
        zip_code = 94016 if not zip_code else zip_code
        self.sl.wait_and_input_text(self.BILLING_ZIP_FIELD, zip_code)

    def input_billing_phone_number(self, phone=None):
        """
        Inputs billing phone number.
        Parameters:
        phone(str): Billing phone number
        Returns:
        None
        """
        phone = '4151111111' if not phone else phone
        self.sl.wait_and_input_text(self.BILLING_PHONE_FIELD, phone)

    def input_billing_email(self, email=None):
        """
        Inputs billing email.
        Parameters:
        email(str): Billing email
        Returns:
        None
        """
        if not email:
            rand_email = generate_random_email_and_password()
            email = rand_email['email']
        self.sl.wait_and_input_text(self.BILLING_EMAIL_FIELD, email)

    def select_billing_country(self, country=None):
        """
        Inputs billing country.
        Parameters:
        country(str): Billing country
        Returns:
        None
        """
        country = 'United States (US)' if not country else country
        self.sl.wait_and_select_dropdown(self.BILLING_COUNTRY_DROPDOWN, to_select=country, select_by="visible_text")

    def select_billing_state(self, state=None):
        """
        Inputs billing state.
        Parameters:
        state(str): Billing state
        Returns:
        None
        """
        state = 'California' if not state else state
        self.sl.wait_and_select_dropdown(self.BILLING_STATE_DROPDOWN, to_select=state, select_by="visible_text")

    def fill_in_billing_info(self, f_name=None, l_name=None, street1=None, city=None, zip_code=None, phone=None, email=None, state=None, country=None):
        """
        Inputs billing info
        Parameters:
        f_name(str): Billing firstname
        l_name(str): Billing lastname
        street_1(str): Billing street
        city(str): Billing city
        zip_code(str): Billing zipcode
        phone(str): Billing phone number
        email(str): Billing email
        state(str): Billing state
        country(str): Billing country
        Returns:
        None
        """
        self.input_billing_first_name(first_name=f_name)
        self.input_billing_last_name(last_name=l_name)
        self.input_billing_street_address_1(address1=street1)
        self.input_billing_city(city=city)
        self.input_billing_zip(zip_code=zip_code)
        self.input_billing_phone_number(phone=phone)
        self.input_billing_email(email=email)
        self.select_billing_country(country)
        self.select_billing_state(state=state)

    def click_place_order(self):
        """
        Clicks Place Order button.
        Parameters:
        None
        Returns:
        None
        """
        for i in range(3):
            logger.info(f"Clicking the 'Place Order' button. Attempt No: {i}")
            self.sl.wait_and_click(self.PLACE_ORDER_BTN)
            try:
                self.sl.wait_until_element_is_not_visible(self.PLACE_ORDER_BTN)
                break
            except Exception as e:
                logger.error(f"Clicked the 'Place Order' button but it is still displayed. Trying after 1 second")
                time.sleep(1)
        else:
            raise Exception(f"Clicked the 'Place Order' button 3 times and still displayed.")

