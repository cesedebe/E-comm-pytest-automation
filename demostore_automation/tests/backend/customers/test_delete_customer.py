
import pytest
import random
from demostore_automation.src.utilities.wooAPIUtility import WooAPIUtility
from demostore_automation.src.dao.customers_dao import CustomersDAO

pytestmark = [pytest.mark.beregression, pytest.mark.besmoke, pytest.mark.customers_api]

@pytest.mark.tcid5
def test_delete_a_customer_with_force_flag():
    #get random customer from database
    customer_helper = CustomersDAO()
    db_info = customer_helper.get_random_customer_from_db()
    full_db_info = customer_helper.get_customer_by_email(db_info[0]['user_email'])

    # create payload for delete request
    woo_helper = WooAPIUtility()
    payload = {
        "force": True
    }
    print(full_db_info)

    #send HTTP delete customer API request
    rs_body = woo_helper.delete("customers/"+ str(full_db_info[0]['ID']),params=payload, expected_status_code=200)

    # verify response is good
    assert rs_body, f"Response of delete customer call should not be empty."
    assert db_info[0]['user_email'] == rs_body['email'], f"Delete customer endpoint email in response does not match in request." \
                                      f"Expected: {db_info[0]['user_email']}, Actual: {rs_body['email']}"
    assert rs_body['role'] == 'customer', f"Delete customer API, customer role should be 'customer' but " \
                                          f"it was '{rs_body['role']}'"

    # make sure customer is removed from database
    customer_helper = CustomersDAO()
    db_info_2 = customer_helper.get_customer_by_email(db_info[0]['user_email'])
    assert len(db_info_2) == 0, f"Expected 0 record for customer in 'users' table. But found: {len(db_info_2)}"

@pytest.mark.tcid6
def test_delete_a_customer_without_force_flag():
    #get random customer from database
    customer_helper = CustomersDAO()
    db_info = customer_helper.get_random_customer_from_db()
    full_db_info = customer_helper.get_customer_by_email(db_info[0]['user_email'])
    print(full_db_info)

    # create WooAPI utility object
    woo_helper = WooAPIUtility()

    #send HTTP delete customer API request
    rs_body = woo_helper.delete("customers/"+ str(full_db_info[0]['ID']), expected_status_code=501)

    # verify response is good
    assert rs_body, f"Response of delete customer call should not be empty."
    assert "woocommerce_rest_trash_not_supported" == rs_body['code'], f"Expected: woocommerce_rest_trash_not_supported, Actual: {rs_body['code']}"
    assert rs_body['message'] == 'Customers do not support trashing.', f"Delete customer without force, message should be 'Customers do not support trashing.' but " \
                                          f"it was '{rs_body['message']}'"

@pytest.mark.tcid7
def test_delete_a_none_existing_customer():
    #get random customer ID
    random_string = ''.join(random.choices('0123456789', k=4))

    # create payload for delete request
    woo_helper = WooAPIUtility()
    payload = {
        "force": True
    }
    print(random_string)

    #send HTTP delete customer API request
    rs_body = woo_helper.delete("customers/"+ random_string,params=payload, expected_status_code=400)

    # verify response is good
    assert rs_body, f"Response of delete customer call should not be empty."
    assert "woocommerce_rest_invalid_id" == rs_body['code'], f"Expected: woocommerce_rest_invalid_id, Actual: {rs_body['code']}"
    assert rs_body['message'] == 'Invalid resource id.', f"Delete non existent customer, message should be 'Invalid resource id.' but " \
                                          f"it was '{rs_body['message']}'"





