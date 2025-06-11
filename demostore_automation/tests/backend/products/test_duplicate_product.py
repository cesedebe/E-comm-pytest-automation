import pytest
import random
from demostore_automation.src.utilities.wooAPIUtility import WooAPIUtility
from demostore_automation.src.dao.products_dao import ProductsDAO


pytestmark = [pytest.mark.beregression, pytest.mark.besmoke, pytest.mark.customers_api]

@pytest.mark.tcid658
def test_duplicate_product_data():

    #get random product from database
    product_helper = ProductsDAO()
    db_info = product_helper.get_random_product_from_db()

    product_id = db_info[0]['ID']
    product_name = db_info[0]['post_name']

    # create woo_helper instance
    woo_helper = WooAPIUtility()

    #send HTTP duplicate product request
    rs_body = woo_helper.post("products/" + str(product_id) + "/duplicate", expected_status_code=200)

    # verify response is good and info is updated
    assert rs_body, f"Response of duplicate product call should not be empty."
    new_product_id = rs_body["id"]
    new_product_name = rs_body["name"]

    #check database contains duplicate product
    db_info_2 = product_helper.get_product_by_id(new_product_id)
    assert len(db_info_2) == 1, f"Expected 1 record for duplicate product in 'users' table. But found: {len(db_info_2)}"
    assert db_info_2[0]["post_title"] == new_product_name

@pytest.mark.tcid659
def test_duplicate_non_existent_product():

    # get random product ID
    random_string = ''.join(random.choices('0123456789', k=5))

    # Ensure product_id is non-existent
    c_helper = ProductsDAO()
    db_info = c_helper.get_product_by_id(random_string)
    while len(db_info) != 0:
        random_string = ''.join(random.choices('0123456789', k=5))
        db_info = c_helper.get_product_by_id(random_string)

   # create payload for post request
    woo_helper = WooAPIUtility()

    # send HTTP duplicate product API request
    rs_body = woo_helper.post("products/" + random_string + "/duplicate", expected_status_code=404)

    # verify response is good
    assert rs_body, f"Response of duplicate product call should not be empty."
    assert rs_body['code'] == "woocommerce_rest_product_invalid_id", f"Expected: woocommerce_rest_product_invalid_id, Actual: {rs_body['code']}"
    assert rs_body['message'] == 'Invalid product ID.', f"Duplicate non existent product, message should be 'Invalid product id.' but " \
                                          f"it was '{rs_body['message']}'"