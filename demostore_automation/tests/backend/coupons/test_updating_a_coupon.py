import pytest
import random
from demostore_automation.src.utilities.wooAPIUtility import WooAPIUtility
from demostore_automation.src.dao.coupons_dao import CouponsDAO
from demostore_automation.src.utilities.genericUtilities import generate_random_email_and_password
from demostore_automation.src.utilities.genericUtilities import generate_random_coupon_code

pytestmark = [pytest.mark.beregression, pytest.mark.besmoke, pytest.mark.customers_api]

@pytest.mark.tcid911
def test_update_coupon_data():
    #get random coupon from database
    coupon_helper = CouponsDAO()
    db_info = coupon_helper.get_random_coupon_from_db()
    print(db_info)

    rand_ep = generate_random_email_and_password()
    random_email = rand_ep["email"]

    random_code = generate_random_coupon_code().lower()

    # create woo_helper instance
    woo_helper = WooAPIUtility()
    payload = {
        "code": random_code,
        "description": "Updated coupon description",
        "email_restrictions": [random_email]
    }

    #send HTTP update coupon request
    rs_body = woo_helper.put("coupons/"+ str(db_info[0]['ID']),params=payload, expected_status_code=200)

    # verify response is good and info is updated
    assert rs_body, f"Response of Update coupon call should not be empty."
    assert rs_body['email_restrictions'][0] == random_email, f"Update coupon endpoint email_restrictions in response does not match in request." \
                                      f"Expected: {random_email}, Actual: {rs_body['email_restrictions'][0]}"
    assert rs_body['code'] == random_code, f"Update coupon API, code should be {random_code} but " \
                                          f"it was '{rs_body['code']}'"
    assert rs_body['description'] == "Updated coupon description", f"Update coupon API response mismatch Expected: 'Updated coupon description', Actual: {rs_body['description']}"
