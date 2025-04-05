import pytest
from demostore_automation.src.api_helpers.CouponsAPIHelper import CouponsAPIHelper
from demostore_automation.src.utilities.genericUtilities import generate_random_coupon_code
from demostore_automation.src.utilities.genericUtilities import generate_random_string

import logging as logger
import random

@pytest.mark.parametrize("discount_type",
                         [
                             pytest.param('percent', marks=[pytest.mark.ecom260, pytest.mark.smoke,pytest.mark.regression]),
                             pytest.param('fixed_product', marks=[pytest.mark.ecom261,pytest.mark.regression]),
                             pytest.param('fixed_cart', marks=[pytest.mark.ecom262,pytest.mark.regression]),
                         ])
def test_create_coupon_discount_type(discount_type):
    """
    Verifies coupons can be created with different discount types
    Parameters:
    discount_type (str): Discount Type
    Returns:
    None
    """
    #Generate random coupon code for payload
    coupon_code  = generate_random_coupon_code()
    payload = {
            "code": coupon_code,
            "discount_type": discount_type,
            "amount": "10"
        }

    #Create helper object and make API call
    coupon_api_helper = CouponsAPIHelper()
    response = coupon_api_helper.call_create_coupon(payload)

    #Verify the response
    code_in_response = response["code"]
    assert code_in_response.upper() == coupon_code, f"The coupon code in the request does not match coupon code in response"

    discount_type_rs = response["discount_type"]
    assert discount_type_rs == discount_type , f"The discount type in request does not match the discount type in response"

    #Verify coupon is created by making a get call
    response_get = coupon_api_helper.call_retrieve_coupon(response["id"])

    #Verify response matches the expected
    code_in_response = response_get["code"]
    assert code_in_response.upper() == coupon_code, f"The coupon code in the request does not match coupon code in response"

    discount_type_rs = response_get["discount_type"]
    assert discount_type_rs == discount_type , f"The discount type in request does not match the discount type in response"

@pytest.mark.ecom263
def test_create_coupon_with_invalid_discount_type():
    """
    Verifies using a random string in 'discount_type' of create order will fail with correct error message.
    Parameters:
    None
    Returns:
    None
    """

    logger.info("Testing create coupon api for with invalid 'discount_type'.")

    # prepare data and call api
    payload = dict()
    payload['code'] = generate_random_coupon_code(sufix="tcid40", length=5)
    payload['amount'] = str(random.randint(50, 90)) + ".00"
    payload['discount_type'] = generate_random_string()

    coupon_api_helper = CouponsAPIHelper()
    rs_coupon = coupon_api_helper.call_create_coupon(payload, expected_status_code=400)

    assert rs_coupon['code'] == 'rest_invalid_param', f"Create coupon with invalid 'discount_type' " \
            f"returned 'code={rs_coupon['code']}', Expected code = 'rest_invalid_param' "
    assert rs_coupon['message'] == 'Invalid parameter(s): discount_type', f"Create coupon with invalid 'discount_type' " \
            f"returned 'message={rs_coupon['message']}', Expected message = 'Invalid parameter(s): discount_type',"