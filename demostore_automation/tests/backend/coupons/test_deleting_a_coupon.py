
import pytest
import random
from demostore_automation.src.utilities.wooAPIUtility import WooAPIUtility
from demostore_automation.src.dao.coupons_dao import CouponsDAO

pytestmark = [pytest.mark.beregression, pytest.mark.besmoke, pytest.mark.customers_api]

@pytest.mark.tcid77
def test_delete_a_coupon_with_force_flag():
    #get random coupon from database
    coupon_helper = CouponsDAO()
    db_info = coupon_helper.get_random_coupon_from_db()

    # create payload for delete request
    woo_helper = WooAPIUtility()
    payload = {
        "force": True
    }
    print(db_info)

    #send HTTP delete customer API request
    rs_body = woo_helper.delete("coupons/"+ str(db_info[0]['ID']),params=payload, expected_status_code=200)

    # verify response is good
    assert rs_body, f"Response of delete customer call should not be empty."
    assert db_info[0]['ID'] == rs_body['id'], f"Delete customer endpoint ID in response does not match in request." \
                                      f"Expected: {db_info[0]['ID']}, Actual: {rs_body['id']}"

    # make sure coupon is removed from database
    coupon_helper = CouponsDAO()
    db_info_2 = coupon_helper.get_coupon_by_id(db_info[0]['ID'])
    assert len(db_info_2) == 0, f"Expected 0 record for coupon in 'users' table. But found: {len(db_info_2)}"

@pytest.mark.tcid78
def test_delete_a_none_existing_coupon():
    #get random coupon ID
    random_string = ''.join(random.choices('0123456789', k=4))

    # create payload for delete request
    woo_helper = WooAPIUtility()
    payload = {
        "force": True
    }
    print(random_string)

    #send HTTP delete customer API request
    rs_body = woo_helper.delete("coupons/"+ random_string,params=payload, expected_status_code=404)

    # verify response is good
    assert rs_body, f"Response of delete coupon call should not be empty."
    assert "woocommerce_rest_shop_coupon_invalid_id" == rs_body['code'], f"Expected: woocommerce_rest_shop_coupon_invalid_id, Actual: {rs_body['code']}"
    assert rs_body['message'] == 'Invalid ID.', f"Delete non existent coupon, message should be 'Invalid ID.' but " \
                                          f"it was '{rs_body['message']}'"