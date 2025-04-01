
from demostore_automation.src.utilities.wooAPIUtility import WooAPIUtility


class CouponsAPIHelper:
    """A simple class representing CouponsAPIHelper."""

    def __init__(self):
        """Initializes CouponsAPIHelper  with an instance of WooAPIUtility."""
        self.woo_api_utility = WooAPIUtility()

    def call_create_coupon(self, payload, expected_status_code=201):
        """Returns response to POST command that creates a coupon"""
        return self.woo_api_utility.post("coupons", params= payload, expected_status_code=expected_status_code)

    def call_retrieve_coupon(self, coupon_id):
        """Returns response to GET command to retrieve a coupon."""
        return self.woo_api_utility.get(f"coupons/{coupon_id}")