
from demostore_automation.src.utilities.wooAPIUtility import WooAPIUtility


class CouponsAPIHelper:

    def __init__(self):
        self.woo_api_utility = WooAPIUtility()

    def call_create_coupon(self, payload, expected_status_code=201):
        return self.woo_api_utility.post("coupons", params= payload, expected_status_code=expected_status_code)

    def call_retrieve_coupon(self, coupon_id):
        return self.woo_api_utility.get(f"coupons/{coupon_id}")