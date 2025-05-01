import pytest
from demostore_automation.src.pages.MyAccountSignedOutPage import MyAccountSignedOutPage

pytestmark = [pytest.mark.feregression, pytest.mark.fesmoke, pytest.mark.my_account]

@pytest.mark.usefixtures("init_driver")
class TestMyAccountPage:

    @pytest.mark.tcid15
    def test_login_username_label (self):
        """
        Verify label on username field.
        Parameters:
        None
        Returns:
        None
        """
        myacct = MyAccountSignedOutPage(self.driver)

        # go to my account page
        myacct.go_to_my_account()

        # verify username label
        assert (myacct.get_username_label().split("\n")[0] == "Username or email address *"), "Label of the username field is Incorrect!"

    @pytest.mark.tcid16
    def test_login_password_label (self):
        """
        Verify label on password field.
        Parameters:
        None
        Returns:
        None
        """
        myacct = MyAccountSignedOutPage(self.driver)

        # go to my account page
        myacct.go_to_my_account()

        # verify password label
        assert (myacct.get_password_label().split("\n")[0] == "Password *"), "Label of the password field is Incorrect!"

    @pytest.mark.tcid14
    def test_my_account_page_has_login_form(self):
        """
        Verify Login form exists
        Parameters:
        None
        Returns:
        None
        """
        myacct = MyAccountSignedOutPage(self.driver)

        # go to my account page
        myacct.go_to_my_account()

        #verify form login form exists
        assert (myacct.get_login_form_heading() == "Login"), "My account page does not have a login form"

    @pytest.mark.tcid17
    def test_my_account_page_has_register_form(self):
        """
        Verify Registration form exists
        Parameters:
        None
        Returns:
        None
        """
        myacct = MyAccountSignedOutPage(self.driver)

        # go to my account page
        myacct.go_to_my_account()

        #verify form login form exists
        assert (myacct.get_registration_form_heading() == "Register"), "My account page does not have a registration form"


    @pytest.mark.tcid18
    def test_register_email_address_label(self):
        """
        Verify label on email field.
        Parameters:
        None
        Returns:
        None
        """
        myacct = MyAccountSignedOutPage(self.driver)

        # go to my account page
        myacct.go_to_my_account()

        # verify email label
        assert (myacct.get_reg_email_label().split("\n")[0] == "Email address *"), "Label of the email field is Incorrect!"

    @pytest.mark.tcid181
    def test_register_email_address_label(self):
        """
        Verify label on email field.
        Parameters:
        None
        Returns:
        None
        """
        myacct = MyAccountSignedOutPage(self.driver)

        # go to my account page
        myacct.go_to_my_account()

        # verify password label
        assert (myacct.get_reg_password_label().split("\n")[0] == "Password *"), "Label of the password field is Incorrect!"

    @pytest.mark.tcid102
    def test_breadcrumb_display(self):
        """
        Verify Breadcrumb is displayed correctly on my_account page
        Parameters:
        None
        Returns:
        None
        """
        myacct = MyAccountSignedOutPage(self.driver)

        # go to my account page
        myacct.go_to_my_account()
        expected_bc = "Home / My account"

        #get actual breadcrumb
        actual_breadcrumb = myacct.get_breadcrumb().strip()

        # compare actual to expected breadcrumb
        assert ( actual_breadcrumb == expected_bc), f"Breadcrumb mismatch! Found: {actual_breadcrumb} Expected: {expected_bc}"

    @pytest.mark.tcid103
    def test_my_account_page_title(self):
        """
        Verify "My account" is displayed on the page
        Parameters:
        None
        Returns:
        None
        """
        myacct = MyAccountSignedOutPage(self.driver)

        # go to my account page
        myacct.go_to_my_account()
        expected_title = "My account"

        #get actual breadcrumb
        actual_title = myacct.get_my_account_page_title().strip()

        # compare actual to expected breadcrumb
        assert ( actual_title == expected_title), f"Breadcrumb mismatch! Found: {actual_title} Expected: {expected_title}"