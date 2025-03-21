
import pytest
import logging as logger

from demostore_automation.src.pages.ProductPage import ProductPage

pytestmark = [pytest.mark.fe, pytest.mark.regression, pytest.mark.smoke, pytest.mark.pdp, pytest.mark.pdp_variable]


@pytest.mark.usefixtures("init_driver")
class TestProductDetailPageVariableProduct:
    """
    A class representing Product Page test for variable product.
    Attributes:
    driver : Selenium WebDriver
    expected_name(str): Name of variable product
    expected_main_image_url(str): URL of product
    product_page(ProductPage): Instance of ProductPage
    """
    @pytest.fixture(scope='class')
    def setup(self, request):
        """
        Initializes a class variables with expected_name,expected_main_image_url and product_page and go to product page
        """
        # go a variable product page. get a random variable product from database
        # TODO: for now hard code a product page, later update the code so that a random product is fetched from db
        request.cls.expected_name = "Hoodie"
        request.cls.expected_main_image_url = "http://dev.bootcamp.store.supersqa.com/wp-content/uploads/2024/10/hoodie-2-416x416.jpg"
        request.cls.product_page = ProductPage(self.driver)

        request.cls.product_page.go_to_product_page(request.cls.expected_name)


    @pytest.mark.ecom124
    def test_variable_product_page_verify_product_name(self, setup):
        """
        Verifies product name on variable product page.
        Parameters:
        setup
        Returns:
        None
        """

        logger.info("Testing variable product: 'product name'.")

        # verify the page contains the product name and is visible
        displayed_name = self.product_page.get_displayed_product_name()

        assert displayed_name == self.expected_name, \
                            f"For a variable product the displayed name and expected name do not match. \
                            Expected: {self.expected_name}, Actual: {displayed_name}"

    @pytest.mark.ecom125
    def test_variable_product_page_verify_main_image(self, setup):
        """
        Verifies main image on variable product page.
        Parameters:
        setup
        Returns:
        None
        """
        # get the displayed image url
        displayed_image_url = self.product_page.get_url_of_displayed_main_image()

        # compare the image url to the expected
        assert displayed_image_url == self.expected_main_image_url, "The displayed and expected main image url do not match. "