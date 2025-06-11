import pytest
import logging as logger
from demostore_automation.src.api_helpers.TaxRatesAPIHelper import TaxHelper
from demostore_automation.src.dao.tax_rate_dao import TaxDAO

pytestmark = [pytest.mark.beregression, pytest.mark.besmoke, pytest.mark.customers_api]

@pytest.mark.tcid793
def test_delete_tax_rate():
    """
        Test case to verify the functionality of deleting a tax rate.
    """

    logger.info("TEST: delete a tax rate")
    tax_obj = TaxHelper()
    tax_dao = TaxDAO()

    rand_tax = tax_dao.get_random_tax_rate_from_db()
    id_in_db = rand_tax[0]['tax_rate_id']

    tax_api_info = tax_obj.delete_tax_rate(id_in_db)
    assert tax_api_info['id'] == id_in_db, f"tax rate  not deleted"