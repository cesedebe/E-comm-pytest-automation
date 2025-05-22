
import pytest
import random
from demostore_automation.src.utilities.wooAPIUtility import WooAPIUtility
from demostore_automation.src.dao.coupons_dao import CouponsDAO

pytestmark = [pytest.mark.beregression, pytest.mark.besmoke, pytest.mark.customers_api]

@pytest.mark.tcid82
def test_get_all_coupons():
    # create woo_helper instance
    woo_helper = WooAPIUtility()

    #send HTTP GET coupon request
    rs_body = woo_helper.get("coupons",expected_status_code=200)

    # verify response is good
    assert rs_body, f"Response of get all coupons call should not be empty."
    for i in rs_body:
        assert i['discount_type'] in ["percent", "fixed_cart", "fixed_product"],f"get coupons did not return list of coupons! Actual: {i['discount_type']}"

@pytest.mark.tcid877
def test_get_coupon_by_id():
    #get random coupon from database
    coupon_helper = CouponsDAO()
    db_info = coupon_helper.get_random_coupon_from_db()
    print(db_info)

    # create woo_helper instance
    woo_helper = WooAPIUtility()

    #send HTTP GET coupon request
    rs_body = woo_helper.get("coupons/"+ str(db_info[0]['ID']), expected_status_code=200)

    # verify response is good
    assert rs_body, f"Response of get coupon by ID call should not be empty."
    assert db_info[0]['ID'] == rs_body['id'], f"Get coupon endpoint ID in response does not match in request." \
                                      f"Expected: {db_info[0]['ID']}, Actual: {rs_body['id']}"

    # get same coupon from database and compare coupon codes
    coupon_helper = CouponsDAO()
    db_info_2 = coupon_helper.get_coupon_by_id(db_info[0]['ID'])

    assert len(db_info_2) == 1, f"Expected 1 record for coupon in 'users' table. But found: {len(db_info_2)}"
    assert rs_body['code'] == db_info_2[0]['post_title'], f"Get coupon code from API does not match the database coupon code." \
                                      f"Expected: {rs_body['code']}, Actual: {db_info_2[0]['post_title']}"

@pytest.mark.tcid876
def test_get_coupon_by_invalid_id():
    #get random coupon ID
    random_string = ''.join(random.choices('0123456789', k=4))

    # create payload for delete request
    woo_helper = WooAPIUtility()
    print(random_string)

    #send HTTP GET coupon request
    rs_body = woo_helper.get("coupons/"+ random_string, expected_status_code=404)

    # verify response is good
    assert rs_body, f"Response of get coupon call should not be empty."
    assert "woocommerce_rest_shop_coupon_invalid_id" == rs_body['code'], f"Expected: woocommerce_rest_shop_coupon_invalid_id, Actual: {rs_body['code']}"
    assert rs_body['message'] == 'Invalid ID.', f"Retrieving a non existent coupon, message should be 'Invalid ID.' but " \
                                          f"it was '{rs_body['message']}'"