import pytest
from demostore_automation.src.utilities.genericUtilities import generate_random_string
from demostore_automation.src.utilities.wooAPIUtility import WooAPIUtility
from demostore_automation.src.dao.orders_dao import OrdersDAO

pytestmark = [pytest.mark.beregression, pytest.mark.besmoke, pytest.mark.customers_api]

@pytest.mark.tcid818
def test_update_order_data():

    #get random order from database
    order_helper = OrdersDAO()
    db_info = order_helper.get_random_order_from_db()
    print(db_info)

    # create payload for update request
    woo_helper = WooAPIUtility()

    payload = {
        "status": "cancelled",
        "currency": "CAD",
        "billing": {
            "first_name": "Mary",
            "last_name": "Stewart",
            "company": "SuperSQA",
            "address_1": "34 Market Avenue",
            "address_2": "",
            "city": "San Antonio",
            "state": "CA",
            "postcode": "55104",
            "country": "US",
            "email": "mary.stewart@sympatico.com",
            "phone": "(515) 304-5151"
        }
    }

    #send HTTP update customer API request
    rs_body = woo_helper.put("orders/"+ str(db_info[0]['order_id']),params=payload, expected_status_code=200)

    # verify response is good and info is updated
    assert rs_body, f"Response of Update order customer call should not be empty."
    assert rs_body['id'] == db_info[0]['order_id'] , f"Update order endpoint email in response does not match in request." \
                                      f"Expected: {db_info[0]['order_id']}, Actual: {rs_body['id']}"
    assert rs_body['status'] == 'cancelled', f"Update order API, order status should be 'cancelled' but " \
                                          f"it was '{rs_body['status']}'"
    assert rs_body['currency'] == 'CAD', f"Update order API, order currency should be 'CAD' but " \
                                          f"it was '{rs_body['currency']}'"
    assert rs_body['billing']['email'] == "mary.stewart@sympatico.com", f"Expected updated order billing email: mary.stewart@sympatico.com Actual: {rs_body['billing']['email']}"


