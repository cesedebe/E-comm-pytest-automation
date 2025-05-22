
import pytest
import random
from demostore_automation.src.utilities.wooAPIUtility import WooAPIUtility
from demostore_automation.src.dao.orders_dao import OrdersDAO

pytestmark = [pytest.mark.beregression, pytest.mark.besmoke, pytest.mark.customers_api]

@pytest.mark.tcid300
def test_delete_an_order_with_force_flag():
    #get random customer from database
    order_helper = OrdersDAO()
    db_info = order_helper.get_random_order_from_db()

    # create payload for delete request
    woo_helper = WooAPIUtility()
    payload = {
        "force": True
    }

    #send HTTP delete customer API request
    rs_body = woo_helper.delete("orders/"+ str(db_info[0]['order_id']),params=payload, expected_status_code=200)

    # verify response is good
    assert rs_body, f"Response of delete order call should not be empty."
    assert rs_body['id'] == db_info[0]['order_id'] , f"Delete order endpoint email in response does not match in request." \
                                      f"Expected: {db_info[0]['order_id']}, Actual: {rs_body['id']}"
    assert rs_body['total'] == "{:.2f}".format(db_info[0]['net_total']), f"Delete order API, total should be {db_info[0]['net_total']} but " \
                                          f"it was '{rs_body['total']}'"

    # make sure customer is removed from database
    order_helper = OrdersDAO()
    db_info_2 = order_helper.get_order_lines_by_order_id(db_info[0]['order_id'])
    assert len(db_info_2) == 0, f"Expected 0 record for orders in woocommerce_order_items table. But found: {len(db_info_2)}"

@pytest.mark.tcid301
def test_delete_a_none_existing_order():
    #get random order ID
    random_string = ''.join(random.choices('0123456789', k=4))
    print(random_string)

    # create payload for delete request
    woo_helper = WooAPIUtility()
    payload = {
        "force": True
    }
    #send HTTP delete order API request
    rs_body = woo_helper.delete("orders/"+ random_string,params=payload, expected_status_code=404)

    # verify response is good
    assert rs_body, f"Response of delete order call should not be empty."
    assert rs_body['code'] == 'woocommerce_rest_shop_order_invalid_id', f"Expected: woocommerce_rest_shop_order_invalid_id, Actual: {rs_body['code']}"
    assert rs_body['message'] == 'Invalid ID.', f"Delete non existent order, message should be 'Invalid ID.' but " \
                                          f"it was '{rs_body['message']}'"