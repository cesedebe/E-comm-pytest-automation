import pytest
import random
from demostore_automation.src.dao.products_dao import ProductsDAO
from demostore_automation.src.dao.products_variation_dao import ProductsVariationDAO
from demostore_automation.src.utilities.wooAPIUtility import WooAPIUtility
from demostore_automation.src.utilities.genericUtilities import generate_random_string
import logging as logger

pytestmark = [pytest.mark.beregression, pytest.mark.besmoke, pytest.mark.products_api]

@pytest.mark.tcid913
def test_create_product_variation():
    """
        Test case to create a product variation.
        Parameters:
        None
        Returns:
        None
    """
    #get random product from database
    product_helper = ProductsDAO()
    db_info = product_helper.get_random_product_from_db()
    random_parent_product_id = str(db_info[0]['ID'])

    # get random price
    price = ''.join(random.choices('0123456789', k=2))

    # create payload for API request
    woo_helper = WooAPIUtility()
    payload = {
        "regular_price": price,
        "downloadable": True,
        "weight": "34",
        "description": "This a product variation of parent product ID "+ random_parent_product_id,

    }

    # make the API call
    rs_body = woo_helper.post("products/"+ random_parent_product_id +"/variations",params=payload, expected_status_code=201)

    # verify response is good
    assert rs_body, f"Response of create product variation call should not be empty."
    assert rs_body['type'] == "variation", f"Create product variation api call response has" \
       f"unexpected type. Expected: variation, Actual: {rs_body['type']}"
    assert rs_body['price'] == price, f"Create product variation api call response has" \
       f"unexpected price. Expected: {price}, Actual: {rs_body['price']}"


    # verify the product variation exists in db
    product_variation_id = rs_body['id']
    db_product_variation = ProductsVariationDAO().get_product_variation_by_id(product_variation_id)
    assert len(db_product_variation) == 1, f"Expected 1 product variation in database but found {len(db_product_variation)}"
    assert db_product_variation[0]['post_type'] == 'product_variation', f"Create product, type in db does not match " \
     f"type in api. Expected: product_variation, Actual: {db_product_variation[0]['post_type']}"
    assert db_product_variation[0]['post_parent'] == db_info[0]['ID'], f"Create product variation, parent_id in db does not match " \
     f"id in api. Expected: {db_info[0]['ID']}, Actual: {db_product_variation[0]['post_parent']}"


@pytest.mark.tcid914
def test_create_product_variation_with_invalid_pid():
    """
        Test case to create a product variation with invalid parent product id.
        Parameters:
        None
        Returns:
        None
    """
    #get random product ID
    random_string = ''.join(random.choices('0123456789', k=4))

    # make sure id is non-existent in db
    c_helper = ProductsDAO()
    db_info = c_helper.get_product_by_id(random_string)
    while len(db_info) != 0:
        random_string = ''.join(random.choices('0123456789', k=4))
        db_info = c_helper.get_product_by_id(random_string)

    # create payload for API request
    woo_helper = WooAPIUtility()
    payload = {
        "regular_price": "14",
        "downloadable": True,
        "weight": "34",
        "description": "This a product variation of parent product ID "+ random_string
    }

    # make the API call
    rs_body = woo_helper.post("products/"+ random_string +"/variations",params=payload, expected_status_code=500)

    # verify response is good
    assert rs_body, f"Response of create product variation call should not be empty."
    assert rs_body['code'] == "internal_server_error", f"Expected: internal_server_error, Actual: {rs_body['code']}"

