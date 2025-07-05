import pytest
import random
from demostore_automation.src.utilities.wooAPIUtility import WooAPIUtility
from demostore_automation.src.utilities.genericUtilities import generate_random_string
import logging as logger

pytestmark = [pytest.mark.beregression, pytest.mark.besmoke, pytest.mark.products_api]

@pytest.mark.tcid2703
def test_list_all_data():
    """
        Test case to list all available data endpoints.
        Parameters:
        None
        Returns:
        None
    """

    # create payload for API request
    woo_helper = WooAPIUtility()

    # make the API call
    rs_body = woo_helper.get("data", expected_status_code=200)
    logger.info(rs_body)

    #validate response
    assert rs_body, f"Response of list all data call should not be empty."
    for i in rs_body:
        assert len(i["slug"]) > 0, "Response of list all data call should not have empty slug value"
        assert len(i["description"]) > 0, "Response of list all data call should not have empty description value"



@pytest.mark.tcid2704
def test_list_all_continents():
    """
        Test case to list all available continents.
        Parameters:
        None
        Returns:
        None
    """

    # create payload for API request
    woo_helper = WooAPIUtility()

    # make the API call
    rs_body = woo_helper.get("data/continents", expected_status_code=200)

    #validate response
    assert rs_body, f"Response of list continents call should not be empty."

    #return random continent code
    if len(rs_body)  > 0 :
        return str(rs_body[(random.randint(0, len(rs_body) - 1 ))]["code"])
    else:
        logger.info("THERE ARE NO CONTINENTS TO LIST")
        return str()

@pytest.mark.tcid2705
def test_retrieve_continent_data():
    """
        Test case to get continent data.
        Parameters:
        None
        Returns:
        None
    """

    #get random continent code
    code = test_list_all_continents()
    if len(code) > 0:
         # create payload for API request
         woo_helper = WooAPIUtility()

         # make the API call
         rs_body = woo_helper.get("data/continents/" + code, expected_status_code=200)
         logger.info(rs_body)

         #validate response
         assert rs_body["code"] ==  code , f"Retrieve continents data api call response has" \
         f"unexpected continent code. Expected: {code}, Actual: {rs_body['code']}"
    else:
         logger.info("THERE ARE NO CONTINENTS TO RETRIEVE")


@pytest.mark.tcid2706
def test_list_all_countries():
    """
        Test case to list all available countries.
        Parameters:
        None
        Returns:
        random country code
    """

    # create payload for API request
    woo_helper = WooAPIUtility()

    # make the API call
    rs_body = woo_helper.get("data/countries", expected_status_code=200)

    #validate response
    assert rs_body, f"Response of list countries  should not be empty."

    #return random country code
    if len(rs_body)  > 0 :
        return str(rs_body[(random.randint(0, len(rs_body) - 1 ))]["code"])
    else:
        logger.info("THERE ARE NO CONTINENTS TO LIST")
        return str()

@pytest.mark.tcid2707
def test_retrieve_country_data():
    """
        Test case to get countries data.
        Parameters:
        None
        Returns:
        None
    """

    #get random continent code
    code = test_list_all_countries()
    if len(code) > 0:
         # create payload for API request
         woo_helper = WooAPIUtility()

         # make the API call
         rs_body = woo_helper.get("data/countries/" + code, expected_status_code=200)

         #validate response
         assert rs_body["code"] ==  code , f"Retrieve country data api call response has" \
         f"unexpected country code. Expected: {code}, Actual: {rs_body['code']}"
    else:
         logger.info("THERE ARE NO COUNTRIES TO RETRIEVE")


@pytest.mark.tcid2708
def test_list_all_currencies():
    """
        Test case to list all available currencies.
        Parameters:
        None
        Returns:
        random currency code
    """

    # create payload for API request
    woo_helper = WooAPIUtility()

    # make the API call
    rs_body = woo_helper.get("data/currencies", expected_status_code=200)

    #validate response
    assert rs_body, f"Response of list currencies should not be empty."

    #return random country code
    if len(rs_body)  > 0 :
        return str(rs_body[(random.randint(0, len(rs_body) - 1 ))]["code"])
    else:
        logger.info("THERE ARE NO CURRENCIES TO LIST")
        return str()


@pytest.mark.tcid2709
def test_retrieve_currency_data():
    """
        Test case to get currency data.
        Parameters:
        None
        Returns:
        None
    """

    #get random continent code
    code = test_list_all_currencies()
    if len(code) > 0:
         # create object for API request
         woo_helper = WooAPIUtility()

         # make the API call
         rs_body = woo_helper.get("data/currencies/" + code, expected_status_code=200)

         #validate response
         assert rs_body["code"] ==  code , f"Retrieve currency data api call response has" \
         f"unexpected currency code. Expected: {code}, Actual: {rs_body['code']}"
    else:
         logger.info("THERE ARE NO COUNTRIES TO RETRIEVE")

@pytest.mark.tcid2800
def test_current_currency():
    """
        Test case to get current currency.
        Parameters:
        None
        Returns:
        None
    """

    # create object for API request
    woo_helper = WooAPIUtility()

    # make the API call
    rs_body = woo_helper.get("data/currencies/current", expected_status_code=200)

    #validate response
    assert rs_body, f"Response of get current currency should not be empty."

