import pytest
from demostore_automation.src.dao.customers_dao import CustomersDAO
from demostore_automation.src.pages.MyAccountSignedOutPage import MyAccountSignedOutPage
from demostore_automation.src.pages.LostPasswordPage import LostPasswordPage
from demostore_automation.src.utilities.genericUtilities import generate_random_string

pytestmark = [pytest.mark.feregression, pytest.mark.fesmoke, pytest.mark.my_account]

@pytest.mark.usefixtures("init_driver")

class TestLostPassword:

    @pytest.mark.tcid692
    def test_lost_password (self):
        """
        Verify Lost Password Page
        Parameters:
        None
        Returns:
        None
        """
        # get random customer from database
        customer_helper = CustomersDAO()
        db_info = customer_helper.get_random_customer_from_db()
        full_db_info = customer_helper.get_customer_by_email(db_info[0]['user_email'])
        lost_password = LostPasswordPage(self.driver)

        myacct = MyAccountSignedOutPage(self.driver)

        # go to my account page
        myacct.go_to_my_account()

        # input login username or email address
        myacct.input_login_username(full_db_info[0]["user_login"])

        #input incorrect password
        myacct.input_login_password("8sjdsj434vfd")

        #click login button
        myacct.click_login_button()

        #wait until error is seen on my account page
        myacct.wait_until_error_is_displayed(f"Error: The password you entered for the username {full_db_info[0]["user_login"]} is incorrect.")

        #click lost your password
        myacct.click_lost_your_password()

        #input username or email
        lost_password.input_username_or_email(full_db_info[0]["user_login"])

        #click reset password button
        lost_password.click_reset_password()

        lost_password.wait_until_message_is_displayed("Password reset email has been sent")

    @pytest.mark.tcid695
    def test_lost_password_invalid_username (self):
        """
        Verify Lost Password Page with invalid username
        Parameters:
        None
        Returns:
        None
        """
        lost_password = LostPasswordPage(self.driver)

        #go to the page
        lost_password.go_lost_password_page()

        #enter random string as username
        lost_password.input_username_or_email(generate_random_string())

        #click reset password
        lost_password.click_reset_password()

        #check the error message
        lost_password.wait_until_error_is_displayed("Invalid username or email.")

    @pytest.mark.tcid697
    def test_lost_password_breadcrumb (self):
        """
        Verify Lost Password Page Breadcrumb
        Parameters:
        None
        Returns:
        None
        """
        lost_password = LostPasswordPage(self.driver)

        #go to the page
        lost_password.go_lost_password_page()

        #get breadcrumb and check if its correct
        bc = lost_password.get_breadcrumb()

        assert bc == "Home / My account / Lost password", "Invalid breadcrumb detected on lost password page"


    @pytest.mark.tcid699
    def test_lost_password_title (self):
        """
        Verify Lost Password Page Title
        Parameters:
        None
        Returns:
        None
        """
        lost_password = LostPasswordPage(self.driver)

        #go to the page
        lost_password.go_lost_password_page()

        #get title and verify it
        title = lost_password.get_lost_password_page_title()

        assert title == "Lost password", "Invalid title detected on lost password page"


    @pytest.mark.tcid691
    def test_lost_password_username_label (self):
        """
        Verify Lost Password Page username label
        Parameters:
        None
        Returns:
        None
        """
        lost_password = LostPasswordPage(self.driver)

        #go to the page
        lost_password.go_lost_password_page()

        #get title and verify it
        ul = lost_password.get_username_label()

        assert ul == "Username or email *\nRequired", "Invalid Username or email label detected on lost password page"