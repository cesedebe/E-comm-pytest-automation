import random

from demostore_automation.src.api_helpers.TaxRatesAPIHelper import TaxHelper
from demostore_automation.src.utilities.wooAPIUtility import WooAPIUtility

import pytest

pytestmark = [pytest.mark.beregression, pytest.mark.besmoke, pytest.mark.customers_api]

@pytest.mark.tcid794
def test_get_all_tax_rates():
    """
      Test to verify that the 'get all tax rates' endpoint returns all tax rates.
    """
    req_helper = WooAPIUtility()
    rs_api = req_helper.get(woo_endpoint='taxes')
    assert rs_api, f"Get all tax rates end point returned nothing."


@pytest.mark.tcid795
def test_get_tax_rate_by_id():
    """
        Test to verify the functionality of 'get tax rate by ID'.
    """

    tax_obj = TaxHelper()

    data = {
          "country": "US",
          "state": "AL",
          "cities": ["dc", "newyork", "Cardiff"],
          "postcodes": ["35014", "35036", "35041"],
          "rate": "10",
          "name": "State Tax",
          "shipping": False
        }
    payload = dict(data)
    new_tax = tax_obj.call_create_tax_rate(payload)
    tax_id = new_tax['id']

    rs_api = tax_obj.get_tax_rate_by_id(tax_id)

    assert rs_api['id'] == tax_id, f'retrieve tax rate by id failed'


@pytest.mark.tcid796
def test_get_tax_rate_by_invalid_id():
    """
       Test to verify the handling of 'get tax rate by invalid ID'.
    """
    tax_obj = TaxHelper()
    tax_id = random.randint(1000, 2000)

    rs_api = tax_obj.get_tax_rate_by_id(tax_id, expected_status_code=404)

    assert rs_api['message'] == 'Invalid resource ID.', f"Retrieve tax rate by invalid id returned wrong 'message'. Expected: 'Invalid resource ID.', Actual: '{rs_api['message']}'"
    assert rs_api['code'] == 'woocommerce_rest_invalid_id', f"Retrieve tax rate by invalid id returned wrong code. Expected: 'woocommerce_rest_invalid_id', Actual: '{rs_api['code']}'"
    assert rs_api['data']['status'] == 404, f"Retrieve tax rate by invalid id returned wrong 'status' in 'data' field.. Expected: 404, Actual: '{rs_api['data']['status']}'"