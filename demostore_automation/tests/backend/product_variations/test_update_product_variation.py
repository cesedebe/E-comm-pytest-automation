import pytest
import random
from datetime import date
import logging as logger
from demostore_automation.src.dao.products_dao import ProductsDAO
from demostore_automation.src.dao.products_variation_dao import ProductsVariationDAO
from demostore_automation.src.utilities.wooAPIUtility import WooAPIUtility
from demostore_automation.src.utilities.genericUtilities import generate_random_string


pytestmark = [pytest.mark.beregression, pytest.mark.besmoke, pytest.mark.products_api]

@pytest.mark.tcid918
def test_update_product_variation():
    """
        Test case to update a valid product variation
        Parameters:
        None
        Returns:
        None
    """
    #get random product variation from database along with its parent id
    db_info = ProductsVariationDAO().get_random_product_variation_from_db()

    while (db_info[0]['post_parent'] == 0) :
        db_info = ProductsVariationDAO().get_random_product_variation_from_db()

    logger.info(f"Get random product variation from db: {db_info}")
    variation_id = str(db_info[0]["ID"])
    parent_product_id = str(db_info[0]["post_parent"])

    #get random price
    random_price = ''.join(random.choices('0123456789', k=4))

    payload = {
        "regular_price": random_price,
        "description": f"This product variation was updated on {date.today()}"
    }

    # make the API call
    woo_helper = WooAPIUtility()
    rs_body = woo_helper.put("products/"+ parent_product_id +"/variations/" + variation_id, params=payload, expected_status_code=200)

    # verify response is good
    assert rs_body, f"Response of put product variation call should not be empty."
    assert rs_body['regular_price'] == payload["regular_price"], f"Update product variation api call response has" \
                f"unexpected regular price. Expected: {payload["regular_price"]}, Actual: {rs_body['regular_price']}"
    assert rs_body['description'].strip("<p>").strip("</p>\n") == payload["description"], f"Update product variation api call response has" \
                f"unexpected description. Expected: {payload["description"]}, Actual: {rs_body['description']}"