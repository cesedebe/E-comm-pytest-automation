import pytest
import random
from demostore_automation.src.dao.products_dao import ProductsDAO
from demostore_automation.src.dao.products_variation_dao import ProductsVariationDAO
from demostore_automation.src.utilities.wooAPIUtility import WooAPIUtility
from demostore_automation.src.utilities.genericUtilities import generate_random_string
import logging as logger

pytestmark = [pytest.mark.beregression, pytest.mark.besmoke, pytest.mark.products_api]

@pytest.mark.tcid915
def test_get_product_variation():
    """
        Test case to get a specific product variation.
        Parameters:
        None
        Returns:
        None
    """
    #get random product variation from database along with its parent id
    db_info = ProductsVariationDAO().get_random_product_variation_from_db()
    logger.info( db_info)
    variation_id = str(db_info[0]["ID"])
    parent_product_id = str(db_info[0]["post_parent"])

    if parent_product_id != "0":

        # make the API call
        woo_helper = WooAPIUtility()
        rs_body = woo_helper.get("products/"+ parent_product_id +"/variations/" + variation_id, expected_status_code=200)

        # verify response is good
        assert rs_body, f"Response of get product variation call should not be empty."
        assert rs_body['type'] == "variation", f"Get product variation api call response has" \
         f"unexpected type. Expected: variation, Actual: {rs_body['type']}"
        assert rs_body['id'] == db_info[0]["ID"], f"Get product variation api call response has" \
         f"unexpected id. Expected: {db_info[0]["ID"]}, Actual: {rs_body['id']}"
        assert rs_body['parent_id'] == db_info[0]["post_parent"], f"Get product variation api call response has" \
        f"unexpected parent product id. Expected: {db_info[0]["post_parent"]}, Actual: {rs_body['parent_id']}"


@pytest.mark.tcid916
def test_get_product_variation_with_invalid_id():
    """
        Test case to get a specific product variation but with invalid id.
        Parameters:
        None
        Returns:
        None
    """
    #get random product variation from database along with its parent id
    db_info = ProductsVariationDAO().get_random_product_variation_from_db()
    variation_id = str(db_info[0]["ID"])
    parent_product_id = str(db_info[0]["post_parent"])

    #get random product variation ID
    random_string = ''.join(random.choices('0123456789', k=4))

    # make the API call
    woo_helper = WooAPIUtility()
    rs_body = woo_helper.get("products/"+ parent_product_id +"/variations/" + random_string, expected_status_code=404)

    # verify response is good
    assert rs_body, f"Response of get product variation call should not be empty."
    assert rs_body['code'] == "woocommerce_rest_product_variation_invalid_id", f"Expected: woocommerce_rest_product_variation_invalid_id, Actual: {rs_body['code']}"
    assert rs_body['message'] == 'Invalid ID.', f"Retrieve non existent product variation, message should be 'Invalid id.' but " \
                                          f"it was '{rs_body['message']}'"


@pytest.mark.tcid917
def test_get_all_product_variations():
    """
        Test case to get all variations for a product.
        Parameters:
        None
        Returns:
        None
    """
    #get random product that has variation from database
    db_info = ProductsVariationDAO().get_random_product_with_variation()
    random_product_id = str(db_info[0]["product_id"])

    # make the API call
    woo_helper = WooAPIUtility()
    rs_body = woo_helper.get("products/"+ random_product_id +"/variations" , expected_status_code=200)

    # verify response is good
    if rs_body:
        for d in rs_body:
            assert d["parent_id"] == db_info[0]["product_id"], f"Get all product variation api call response has" \
                    f"unexpected parent product id. Expected: {db_info[0]["product_id"]}, Actual: {rs_body['parent_id']}"
            assert d["type"] == "variation" , f"Get all product variation api call response has" \
                    f"unexpected type. Expected: 'variation', Actual: {rs_body['type']}"
            db_product_variation = ProductsVariationDAO().get_product_variation_by_id(d["id"])
            assert len(db_product_variation) == 1, f"Expected 1 product variation in database but found {len(db_product_variation)}"
