import pytest
import random
from demostore_automation.src.dao.products_dao import ProductsDAO
from demostore_automation.src.utilities.wooAPIUtility import WooAPIUtility
from demostore_automation.src.utilities.genericUtilities import generate_random_string
import logging as logger

pytestmark = [pytest.mark.beregression, pytest.mark.besmoke, pytest.mark.products_api]

@pytest.mark.tcid481
def test_create_product_review():
    """
        Test case to create a product review.
        Parameters:
        None
        Returns:
        None
    """
    #get random product from database
    product_helper = ProductsDAO()
    db_info = product_helper.get_random_product_from_db()
    random_parent_product_id = str(db_info[0]['ID'])


    # create payload for API request
    woo_helper = WooAPIUtility()
    payload = {
        "product_id": db_info[0]['ID'],
        "review": "Nice Product! Good Quality!",
        "reviewer": "Jane Doe",
        "reviewer_email": "jane.doe@example.com",
        "rating": 5,
    }

    # make the API call
    rs_body = woo_helper.post("products/reviews",params=payload, expected_status_code=201)
    logger.info(rs_body)

    # verify response is good
    assert rs_body, f"Response of create product variation call should not be empty."
    assert rs_body['reviewer'] == "Jane Doe", f"Create product review api call response has" \
       f"unexpected reviewer. Expected: Jane Doe, Actual: {rs_body['reviewer']}"
    assert rs_body['reviewer_email'] == "jane.doe@example.com", f"Create product review api call response has" \
       f"unexpected reviewer email. Expected: jane.doe@example.com, Actual: {rs_body['reviewer_email']}"
