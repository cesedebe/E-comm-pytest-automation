import pytest
import logging as logger
from demostore_automation.src.api_helpers.TaxRatesAPIHelper import TaxHelper
from demostore_automation.src.dao.tax_rate_dao import TaxDAO

pytestmark = [pytest.mark.beregression, pytest.mark.besmoke, pytest.mark.customers_api]

@pytest.mark.tcid791
def test_create_tax_rate():
    """
        Test case to verify the functionality of creating a tax rate.
    """

    tax_obj = TaxHelper()
    tax_dao = TaxDAO()

    data = {
          "country": "US",
          "state": "AL",
          "cities": ["Alpine", "Thornhill", "Cardiff"],
          "postcodes": ["35714", "35736", "35841"],
          "rate": "4",
          "name": "State Tax",
          "shipping": False
        }
    payload = dict(data)
    new_tax = tax_obj.call_create_tax_rate(payload)
    tax_id = new_tax['id']

    #get tax_rate from database
    tax_info = tax_dao.get_tax_by_id(tax_id)
    id_in_db = tax_info[0]['tax_rate_id']

    assert tax_id == id_in_db, f'Create tax_rate response "id" not same as "ID" in database.' \
                                  f'id: {tax_id}'