
import pytest
from demostore_automation.src.utilities.genericUtilities import generate_random_string
from demostore_automation.src.utilities.wooAPIUtility import WooAPIUtility
from demostore_automation.src.dao.customers_dao import CustomersDAO

pytestmark = [pytest.mark.beregression, pytest.mark.besmoke, pytest.mark.customers_api]

@pytest.mark.tcid727
def test_update_customer_data():

    #get random names
    random_first_name = generate_random_string(4)
    random_last_name = generate_random_string(7)
    print(random_first_name)
    print(random_last_name)

    #get random customer from database
    customer_helper = CustomersDAO()
    db_info = customer_helper.get_random_customer_from_db()
    full_db_info = customer_helper.get_customer_by_email(db_info[0]['user_email'])
    print(full_db_info)

    # create payload for update request
    woo_helper = WooAPIUtility()

    payload = {
        "first_name": random_first_name,
        "last_name": random_last_name,
        "billing": {
            "first_name": random_first_name,
            "last_name": random_last_name
        },
        "shipping": {
            "first_name": random_first_name,
            "last_name": random_last_name
        }
    }

    #send HTTP update customer API request
    rs_body = woo_helper.put("customers/"+ str(full_db_info[0]['ID']),params=payload, expected_status_code=200)

    # verify response is good and info is updated
    assert rs_body, f"Response of Update customer call should not be empty."
    assert db_info[0]['user_email'] == rs_body['email'], f"Update customer endpoint email in response does not match in request." \
                                      f"Expected: {db_info[0]['user_email']}, Actual: {rs_body['email']}"
    assert rs_body['role'] == 'customer', f"Update customer API, customer role should be 'customer' but " \
                                          f"it was '{rs_body['role']}'"
    assert rs_body['first_name'] == random_first_name, f"Expected updated customer first name: {random_first_name}, Actual: {rs_body['first_name']}"
    assert rs_body['last_name'] == random_last_name, f"Expected updated customer last name: {random_last_name}, Actual: {rs_body['last_name']}"
    assert rs_body['shipping']['first_name'] == random_first_name, f"Expected updated customer shipping first name: {random_first_name}, Actual: {rs_body['shipping']['first_name']}"
    assert rs_body['shipping']['last_name'] == random_last_name, f"Expected updated customer shipping last name: {random_last_name}, Actual: {rs_body['shipping']['last_name']}"
    assert rs_body['billing']['first_name'] == random_first_name, f"Expected updated customer billing first name: {random_first_name}, Actual: {rs_body['billing']['first_name']}"
    assert rs_body['billing']['last_name'] == random_last_name, f"Expected updated customer billing last name: {random_last_name}, Actual: {rs_body['billing']['last_name']}"

@pytest.mark.tcid728
def test_update_customer_invalid_data():

    #get random email address
    random_email = generate_random_string(7)

    #get random customer from database
    customer_helper = CustomersDAO()
    db_info = customer_helper.get_random_customer_from_db()
    full_db_info = customer_helper.get_customer_by_email(db_info[0]['user_email'])
    print(full_db_info)

    # create payload for update request
    woo_helper = WooAPIUtility()

    payload = {
        "email": random_email
    }

    #send HTTP update customer API request
    rs_body = woo_helper.put("customers/"+ str(full_db_info[0]['ID']),params=payload, expected_status_code=400)

    # verify response is good and info is updated
    assert rs_body, f"Response of Update customer call should not be empty."
    assert rs_body['code'] == "rest_invalid_param" , f"Expected: rest_invalid_param, Actual: {rs_body['code']}"
    assert rs_body['message'] == 'Invalid parameter(s): email', f"Update customer without invalid email, message should be 'Invalid parameter(s): email' but " \
                                          f"it was '{rs_body['message']}'"





