import pytest
from demostore_automation.src.dao.products_dao import ProductsDAO
from demostore_automation.src.api_helpers.ProductsAPIHelper import ProductsAPIHelper
from demostore_automation.src.utilities.genericUtilities import generate_random_string
import logging as logger

pytestmark = [pytest.mark.beregression, pytest.mark.besmoke, pytest.mark.products_api]

@pytest.mark.ecom188
def test_create_1_simple_product():
    """
        Test case to create a simple product.
        Parameters:
        None
        Returns:
        None
    """
    # prepare payload for simple product
    product_name = generate_random_string(20)
    payload = dict()
    payload['name'] = product_name
    payload['type'] = "simple"
    payload['regular_price'] = "44.99"

    # make the API call
    product_rs = ProductsAPIHelper().call_create_product(payload)

    # verify the response is not empty
    assert product_rs, f"Create product api response is empty. Payload: {payload}"
    assert product_rs['name'] == payload['name'], f"Create product api call response has" \
       f"unexpected name. Expected: {payload['name']}, Actual: {product_rs['name']}"
    assert product_rs['type'] == payload['type'], f"Create product api call response has" \
       f"unexpected type. Expected: {payload['type']}, Actual: {product_rs['type']}"

    # verify the product exists in db
    product_id = product_rs['id']
    db_product = ProductsDAO().get_product_by_id(product_id)

    assert payload['name'] == db_product[0]['post_title'], f"Create product, title in db does not match " \
     f"title in api. DB: {db_product['post_title']}, API: {payload['name']}"
