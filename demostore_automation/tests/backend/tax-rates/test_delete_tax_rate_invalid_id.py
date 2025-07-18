import random

import pytest
import logging as logger
from demostore_automation.src.api_helpers.TaxRatesAPIHelper import TaxHelper
from demostore_automation.src.dao.tax_rate_dao import TaxDAO

pytestmark = [pytest.mark.beregression, pytest.mark.besmoke, pytest.mark.customers_api]

@pytest.mark.tcid792
def test_delete_tax_rate_invalid_id():
    """
      Test to verify the handling of deleting a tax rate with an invalid ID.
    """
    tax_obj = TaxHelper()
    tax_dao = TaxDAO()
    random_tax_id = random.randint(100,800)

    #ensure tax_id is invalid
    db_info = tax_dao.get_tax_by_id(random_tax_id)
    while len(db_info) != 0:
        random_tax_id = random.randint(100,800)
        db_info = tax_dao.get_tax_by_id(random_tax_id)

    tax_api_info = tax_obj.delete_tax_rate(random_tax_id,expected_status_code=400)
    assert tax_api_info['code'] == 'woocommerce_rest_invalid_id', f"tax rate delete invalid id return wrong code"