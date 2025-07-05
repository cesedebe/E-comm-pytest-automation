import pytest
from random import randint
import random
from demostore_automation.src.dao.products_dao import ProductsDAO
from demostore_automation.src.utilities.wooAPIUtility import WooAPIUtility
from demostore_automation.src.utilities.genericUtilities import generate_random_string
import logging as logger

pytestmark = [pytest.mark.beregression, pytest.mark.besmoke, pytest.mark.products_api]

@pytest.mark.tcid482
def test_list_product_reviews():
    """
        Test case to list all product reviews.
        Parameters:
        None
        Returns:
        product review id
    """

    # create object for API request
    woo_helper = WooAPIUtility()

    # make the API call
    rs_body = woo_helper.get("products/reviews", expected_status_code=200)
    logger.info(rs_body)

    #return random product review id
    if len(rs_body)  > 0 :
        return str(rs_body[(randint(0, len(rs_body) - 1 ))]["id"])
    else:
        logger.info("THERE ARE NO PRODUCT REVIEWS TO LIST")
        return str()


@pytest.mark.tcid483
def test_get_product_review():
    """
        Test case to get a product review.
        Parameters:
        None
        Returns:
        None
    """
    #get a product review id
    review_id = test_list_product_reviews()
    if len(review_id) > 0:
        # create payload for API request
        woo_helper = WooAPIUtility()

        # make the API call
        rs_body = woo_helper.get("products/reviews/" + review_id, expected_status_code=200)
        logger.info(rs_body)
        assert rs_body["rating"] in [1,2,3,4,5] , f"Retrieve product review api call response has" \
        f"unexpected rating. Expected: 1 to 5, Actual: {rs_body['rating']}"
    else:
        logger.info("THERE ARE NO PRODUCT REVIEWS TO RETRIEVE")


@pytest.mark.tcid484
def test_update_product_review():
    """
        Test case to update a product review.
        Parameters:
        None
        Returns:
        None
    """
    #get a product review id
    review_id = test_list_product_reviews()
    if len(review_id) > 0:
        # create payload for API request
        woo_helper = WooAPIUtility()
        payload = {
            "review": "Disappointed with Product Quality!",
            "rating": 1,
        }
        # make the API call
        rs_body = woo_helper.put("products/reviews/" + review_id, params=payload,  expected_status_code=200)
        logger.info(rs_body)

        assert rs_body["rating"] == 1 , f"Retrieve product review api call response has" \
       f"unexpected rating. Expected: 1 , Actual: {rs_body['rating']}"
    else:
        logger.info("THERE ARE NO PRODUCT REVIEWS TO UPDATE")



@pytest.mark.tcid485
def test_get_product_review_invalid_id():
    """
        Test case to get a product review using invalid review id.
        Parameters:
        None
        Returns:
        None
    """
    #get a random product review id
    review_id = ''.join(random.choices('0123456789', k=3))

    # create object for API request
    woo_helper = WooAPIUtility()

    # make the API call
    rs_body = woo_helper.get("products/reviews/" + review_id, expected_status_code=404)
    logger.info(rs_body)

    #check response
    assert rs_body["code"] ==  "woocommerce_rest_review_invalid_id" , f"Retrieve product review api call response has" \
        f"unexpected code. Expected: woocommerce_rest_review_invalid_id, Actual: {rs_body['code']}"
    assert rs_body["message"] ==  "Invalid review ID." , f"Retrieve product review api call response has" \
        f"unexpected message. Expected: Invalid review ID., Actual: {rs_body['message']}"

@pytest.mark.tcid486
def test_update_product_review_invalid_id():
    """
        Test case to update a product review with invalid id
        Parameters:
        None
        Returns:
        None
    """
    #get a random product review id
    review_id = ''.join(random.choices('0123456789', k=3))

    # create object for API request
    woo_helper = WooAPIUtility()
    payload = {
            "review": "Disappointed with Product Quality!",
            "rating": 1,
    }

    # make the API call
    rs_body = woo_helper.put("products/reviews/" + review_id, params=payload,  expected_status_code=404)
    logger.info(rs_body)

    #validate response
    assert rs_body["code"] ==  "woocommerce_rest_review_invalid_id" , f"Retrieve product review api call response has" \
        f"unexpected code. Expected: woocommerce_rest_review_invalid_id, Actual: {rs_body['code']}"
    assert rs_body["message"] ==  "Invalid review ID." , f"Retrieve product review api call response has" \
        f"unexpected message. Expected: Invalid review ID., Actual: {rs_body['message']}"


@pytest.mark.tcid487
def test_delete_product_review():
    """
        Test case to delete a product review.
        Parameters:
        None
        Returns:
        None
    """
    #get a product review id
    review_id = test_list_product_reviews()
    if len(review_id) > 0:

        # create payload for API request
        woo_helper = WooAPIUtility()
        payload = {
            "force": True
        }
        # make the API call
        rs_body = woo_helper.delete("products/reviews/" + review_id, params=payload,  expected_status_code=200)
        logger.info(rs_body)

        assert rs_body["deleted"] == True , f"Delete product review api call response has" \
       f"unexpected value for deleted. Expected: True , Actual: {rs_body['deleted']}"
    else:
        logger.info("THERE ARE NO PRODUCT REVIEWS TO DELETE")


@pytest.mark.tcid488
def test_delete_product_review_invalid_id():
    """
        Test case to delete a product review using invalid id
        Parameters:
        None
        Returns:
        None
    """
    #get a random product review id
    review_id = ''.join(random.choices('0123456789', k=3))

    # create payload for API request
    woo_helper = WooAPIUtility()
    payload = {
         "force": True
    }

    # make the API call
    rs_body = woo_helper.delete("products/reviews/" + review_id, params=payload,  expected_status_code=404)
    logger.info(rs_body)

   #validate response
    assert rs_body["code"] ==  "woocommerce_rest_review_invalid_id" , f"Retrieve product review api call response has" \
        f"unexpected code. Expected: woocommerce_rest_review_invalid_id, Actual: {rs_body['code']}"
    assert rs_body["message"] ==  "Invalid review ID." , f"Retrieve product review api call response has" \
        f"unexpected message. Expected: Invalid review ID., Actual: {rs_body['message']}"