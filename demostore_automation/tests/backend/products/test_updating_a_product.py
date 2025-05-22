import pytest
import random
from demostore_automation.src.utilities.wooAPIUtility import WooAPIUtility
from demostore_automation.src.dao.products_dao import ProductsDAO


pytestmark = [pytest.mark.beregression, pytest.mark.besmoke, pytest.mark.customers_api]

@pytest.mark.tcid511
def test_update_product_data():

    #get random product from database
    product_helper = ProductsDAO()
    db_info = product_helper.get_random_product_from_db()
    print(db_info)

    # create woo_helper instance
    woo_helper = WooAPIUtility()
    payload = {
        "reviews_allowed": False,
        "description": "Updated product description",
        "featured": True,
        "stock_status": "outofstock"
    }

    #send HTTP update product request
    rs_body = woo_helper.put("products/"+ str(db_info[0]['ID']),params=payload, expected_status_code=200)

    # verify response is good and info is updated
    assert rs_body, f"Response of Update product call should not be empty."
    assert rs_body["reviews_allowed"] == False, f"Update product endpoint reviews_allowed response does not match in request." \
                                      f"Expected: False, Actual: {rs_body["reviews_allowed"]}"
    assert rs_body["description"] == "Updated product description", f"Updated product description should be 'Updated product description' but " \
                                          f"it was '{rs_body['description']}'"
    assert rs_body["featured"] == True, f"Updated product featured flag should be 'True' but " \
                                          f"it was '{rs_body['featured']}'"
    assert rs_body["stock_status"] == "outofstock", f"Updated product stock status flag should be 'outofstock' but " \
                                          f"it was '{rs_body['stock_status']}'"

    #check database
    db_info_2 = product_helper.get_product_by_id(db_info[0]['ID'])
    assert len(db_info_2) == 1, f"Expected 1 record for product in 'users' table. But found: {len(db_info_2)}"
    assert db_info_2[0]["post_content"] == "Updated product description"
