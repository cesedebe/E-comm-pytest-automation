import random
import pytest
from demostore_automation.src.utilities.wooAPIUtility import WooAPIUtility
from demostore_automation.src.dao.products_dao import ProductsDAO

pytestmark = [pytest.mark.beregression, pytest.mark.besmoke, pytest.mark.customers_api]

@pytest.mark.tcid434
def test_delete_a_product_with_force_flag():
    #get random product from database
    product_helper = ProductsDAO()
    db_info = product_helper.get_random_product_from_db()

    # create payload for delete request
    woo_helper = WooAPIUtility()
    payload = {
        "force": True
    }

    #send HTTP delete product API request
    rs_body = woo_helper.delete("products/"+ str(db_info[0]['ID']),params=payload, expected_status_code=200)

    # verify response is good
    assert rs_body, f"Response of delete product call should not be empty."
    assert rs_body['id'] == db_info[0]['ID'], f"Delete product endpoint ID in response does not match in request." \
                                      f"Expected: {db_info[0]['ID']}, Actual: {rs_body['id']}"

    # make sure product is removed from database
    product_helper = ProductsDAO()
    db_info_2 = product_helper.get_product_by_id(db_info[0]['ID'])
    assert len(db_info_2) == 0, f"Expected 0 record for product in 'users' table. But found: {len(db_info_2)}"

@pytest.mark.tcid435
def test_delete_a_product_without_force_flag():
    #get random product from database
    product_helper = ProductsDAO()
    db_info = product_helper.get_random_product_from_db()

    # create payload for delete request
    woo_helper = WooAPIUtility()

    payload = {
        "force": True
    }
    #send HTTP delete product API request
    rs_body = woo_helper.delete("products/"+ str(db_info[0]['ID']),params=payload,  expected_status_code=200)

    # verify response is good
    assert rs_body, f"Response of delete product call should not be empty."
    assert rs_body['id'] == db_info[0]['ID'], f"Delete product endpoint ID in response does not match in request." \
                                      f"Expected: {db_info[0]['ID']}, Actual: {rs_body['id']}"

    # check if product is removed from database
    product_helper = ProductsDAO()
    db_info_2 = product_helper.get_product_by_id(db_info[0]['ID'])
    assert len(db_info_2) == 0, f"Expected 0 record for product in 'users' table. But found: {len(db_info_2)}"

@pytest.mark.tcid572
def test_delete_a_none_existing_product():
    #get random product ID
    random_string = ''.join(random.choices('0123456789', k=4))

    # check if id is non-existent
    c_helper = ProductsDAO()
    db_info = c_helper.get_product_by_id(random_string)
    while len(db_info) != 0:
        random_string = ''.join(random.choices('0123456789', k=4))
        db_info = c_helper.get_product_by_id(random_string)

    # create payload for delete request
    woo_helper = WooAPIUtility()
    payload = {
        "force": True
    }
    print(random_string)

    #send HTTP delete product API request
    rs_body = woo_helper.delete("products/"+ random_string,params=payload, expected_status_code=404)

    # verify response is good
    assert rs_body, f"Response of delete product call should not be empty."
    assert rs_body['code'] == "woocommerce_rest_product_invalid_id", f"Expected: woocommerce_rest_product_invalid_id, Actual: {rs_body['code']}"
    assert rs_body['message'] == 'Invalid ID.', f"Delete non existent product, message should be 'Invalid id.' but " \
                                          f"it was '{rs_body['message']}'"
