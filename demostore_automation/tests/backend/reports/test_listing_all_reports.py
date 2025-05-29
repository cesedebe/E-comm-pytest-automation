import pytest
import logging as logger
from demostore_automation.src.utilities.wooAPIUtility import WooAPIUtility


pytestmark = [pytest.mark.beregression, pytest.mark.besmoke, pytest.mark.customers_api]

@pytest.mark.tcid771
def test_get_all_reports():
    # create woo_helper instance
    woo_helper = WooAPIUtility()

    #send HTTP GET all reports request
    rs_body = woo_helper.get("reports",expected_status_code=200)

    # verify response is good
    assert rs_body, f"Response of get all reports call should not be empty."
    logger.info(rs_body)

@pytest.mark.tcid772
def test_get_sales_reports():
    #create payload for API message
    payload = {
        "date_min": "2016-05-05",
        "date_max": "2025-05-04"
    }

    # create woo_helper instance
    woo_helper = WooAPIUtility()

    #send HTTP GET sales reports request
    rs_body = woo_helper.get("reports/sales",params=payload,expected_status_code=200)

    # verify response is good
    assert rs_body, f"Response of get all sales reports call should not be empty."
    logger.info(rs_body)

@pytest.mark.tcid773
def test_get_coupon_totals():

    # create woo_helper instance
    woo_helper = WooAPIUtility()

    #send HTTP GET coupon totals request
    rs_body = woo_helper.get("reports/coupons/totals",expected_status_code=200)

    # verify response is good
    assert rs_body, f"Response of get all coupons total call should not be empty."
    for i in rs_body:
        assert i['slug'] in ["percent", "fixed_cart", "fixed_product"],f"get coupons total did not return list of coupons! Actual: {i}"
    logger.info(rs_body)

@pytest.mark.tcid774
def test_get_customers_totals():

    # create woo_helper instance
    woo_helper = WooAPIUtility()

    #send HTTP GET customers total request
    rs_body = woo_helper.get("reports/customers/totals",expected_status_code=200)

    # verify response is good
    assert rs_body, f"Response of get all customers total call should not be empty."
    for i in rs_body:
        assert i['slug'] in ["paying", "non_paying"],f"get customers total did not return list of customers! Actual: {i}"
    logger.info(rs_body)

@pytest.mark.tcid775
def test_get_orders_totals():

    # create woo_helper instance
    woo_helper = WooAPIUtility()

    #send HTTP GET orders total request
    rs_body = woo_helper.get("reports/orders/totals",expected_status_code=200)

    # verify response is good
    assert rs_body, f"Response of get all orders total call should not be empty."
    logger.info(rs_body)


@pytest.mark.tcid776
def test_get_products_totals():

    # create woo_helper instance
    woo_helper = WooAPIUtility()

    #send HTTP GET products total request
    rs_body = woo_helper.get("reports/products/totals",expected_status_code=200)

    # verify response is good
    assert rs_body, f"Response of get all products total call should not be empty."
    logger.info(rs_body)

@pytest.mark.tcid777
def test_get_reviews_totals():

    # create woo_helper instance
    woo_helper = WooAPIUtility()

    #send HTTP GET review totals request
    rs_body = woo_helper.get("reports/reviews/totals",expected_status_code=200)

    # verify response is good
    assert rs_body, f"Response of get all reviews total call should not be empty."
    for i in rs_body:
        assert i['slug'] in ["rated_1_out_of_5", "rated_2_out_of_5", "rated_3_out_of_5", "rated_4_out_of_5", "rated_5_out_of_5"],f"get customers total did not return list of customers! Actual: {i}"
    logger.info(rs_body)