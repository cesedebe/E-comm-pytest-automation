
from demostore_automation.src.utilities.wooAPIUtility import WooAPIUtility


class ProductsAPIHelper:
    """A simple class representing ProductAPIHelper."""

    def __init__(self):
        """Initializes ProductAPIHelper  with an instance of WooAPIUtility."""
        self.woo_api_utility = WooAPIUtility()

    def call_get_product_by_id(self, product_id):
        """Returns response to GET product by ID command."""
        return self.woo_api_utility.get(f"products/{product_id}", expected_status_code=200)

    def call_create_product(self, payload, expected_status_code=201):
        """Returns response to POST command that creates a product."""
        return self.woo_api_utility.post('products', params=payload, expected_status_code=expected_status_code)