import pytest
from demostore_automation.src.pages.MyAccountSignedOutPage import MyAccountSignedOutPage
from demostore_automation.src.pages.MyAccountSignedInPage import MyAccountSignedInPage
from demostore_automation.src.utilities.genericUtilities import generate_random_email_and_password


pytestmark = [pytest.mark.feregression, pytest.mark.fesmoke, pytest.mark.my_account]

@pytest.mark.usefixtures("init_driver")

class TestLeftNavBarSignedIn:

    @pytest.mark.tcid19
    def test_left_nav_has_six_elements (self):
        """
        Verify Navigation Bar has 6 elements
        Parameters:
        None
        Returns:
        None
        """
        # create objects
        myacct = MyAccountSignedOutPage(self.driver)
        myacct_sin = MyAccountSignedInPage(self.driver)

        # go to my account page
        myacct.go_to_my_account()

        random_info = generate_random_email_and_password()
        # fill in the username for registration
        myacct.input_register_email(random_info['email'])

        # fill in the password for registration
        myacct.input_register_password(random_info['password'])

        # click on 'register'
        myacct.click_register_button()

        # verify user is registered
        myacct_sin.verify_user_is_signed_in()

        #get left navigation bar
        nav_bar = myacct_sin.get_left_nav_bar()

        #split into individual options
        list_nav_bar = nav_bar.split("\n")

        assert len(list_nav_bar) == 6, "Navigation Bar does not have 6 elements!"

        myacct_sin.verify_user_is_signed_out()

    @pytest.mark.tcid191
    def test_left_nav_has_download_label (self):
        """
        Verify Navigation Bar has "Downloads" elements
        Parameters:
        None
        Returns:
        None
        """
        # create objects
        myacct = MyAccountSignedOutPage(self.driver)
        myacct_sin = MyAccountSignedInPage(self.driver)

        # go to my account page
        myacct.go_to_my_account()

        random_info = generate_random_email_and_password()
        # fill in the username for registration
        myacct.input_register_email(random_info['email'])

        # fill in the password for registration
        myacct.input_register_password(random_info['password'])

        # click on 'register'
        myacct.click_register_button()

        # verify user is registered
        myacct_sin.verify_user_is_signed_in()

        #get left navigation bar
        nav_bar = myacct_sin.get_left_nav_bar()

        #split into individual options
        list_nav_bar = nav_bar.split("\n")

        assert "Downloads" in list_nav_bar, "Navigation Bar does not have Downloads label"

        myacct_sin.verify_user_is_signed_out()

    @pytest.mark.tcid192
    def test_left_nav_has_order_label (self):
        """
        Verify Navigation Bar has "order" element
        Parameters:
        None
        Returns:
        None
        """
        # create objects
        myacct = MyAccountSignedOutPage(self.driver)
        myacct_sin = MyAccountSignedInPage(self.driver)

        # go to my account page
        myacct.go_to_my_account()

        random_info = generate_random_email_and_password()
        # fill in the username for registration
        myacct.input_register_email(random_info['email'])

        # fill in the password for registration
        myacct.input_register_password(random_info['password'])

        # click on 'register'
        myacct.click_register_button()

        # verify user is registered
        myacct_sin.verify_user_is_signed_in()

        #get left navigation bar
        nav_bar = myacct_sin.get_left_nav_bar()

        #split into individual options
        list_nav_bar = nav_bar.split("\n")

        assert "Orders" in list_nav_bar, "Navigation Bar does not have orders label!"

        myacct_sin.verify_user_is_signed_out()

    @pytest.mark.tcid193
    def test_left_nav_has_address_label (self):
        """
        Verify Navigation Bar has "address" element
        Parameters:
        None
        Returns:
        None
        """
        # create objects
        myacct = MyAccountSignedOutPage(self.driver)
        myacct_sin = MyAccountSignedInPage(self.driver)

        # go to my account page
        myacct.go_to_my_account()

        random_info = generate_random_email_and_password()
        # fill in the username for registration
        myacct.input_register_email(random_info['email'])

        # fill in the password for registration
        myacct.input_register_password(random_info['password'])

        # click on 'register'
        myacct.click_register_button()

        # verify user is registered
        myacct_sin.verify_user_is_signed_in()

        #get left navigation bar
        nav_bar = myacct_sin.get_left_nav_bar()

        #split into individual options
        list_nav_bar = nav_bar.split("\n")

        assert "Addresses" in list_nav_bar, "Navigation Bar does not have Addresses label!"

        myacct_sin.verify_user_is_signed_out()

    @pytest.mark.tcid194
    def test_left_nav_has_account_detail_label (self):
        """
        Verify Navigation Bar has "Account detail" element
        Parameters:
        None
        Returns:
        None
        """
        # create objects
        myacct = MyAccountSignedOutPage(self.driver)
        myacct_sin = MyAccountSignedInPage(self.driver)

        # go to my account page
        myacct.go_to_my_account()

        random_info = generate_random_email_and_password()
        # fill in the username for registration
        myacct.input_register_email(random_info['email'])

        # fill in the password for registration
        myacct.input_register_password(random_info['password'])

        # click on 'register'
        myacct.click_register_button()

        # verify user is registered
        myacct_sin.verify_user_is_signed_in()

        #get left navigation bar
        nav_bar = myacct_sin.get_left_nav_bar()

        #split into individual options
        list_nav_bar = nav_bar.split("\n")

        assert "Account details" in list_nav_bar, "Navigation Bar does not have account details label!"

        myacct_sin.verify_user_is_signed_out()

    @pytest.mark.tcid195
    def test_left_nav_has_dashboard_label (self):
        """
        Verify Navigation Bar has "Dashboard" elements
        Parameters:
        None
        Returns:
        None
        """
        # create objects
        myacct = MyAccountSignedOutPage(self.driver)
        myacct_sin = MyAccountSignedInPage(self.driver)

        # go to my account page
        myacct.go_to_my_account()

        random_info = generate_random_email_and_password()
        # fill in the username for registration
        myacct.input_register_email(random_info['email'])

        # fill in the password for registration
        myacct.input_register_password(random_info['password'])

        # click on 'register'
        myacct.click_register_button()

        # verify user is registered
        myacct_sin.verify_user_is_signed_in()

        #get left navigation bar
        nav_bar = myacct_sin.get_left_nav_bar()

        #split into individual options
        list_nav_bar = nav_bar.split("\n")

        assert "Dashboard" in list_nav_bar, "Navigation Bar does not have Dashboard label!"

        myacct_sin.verify_user_is_signed_out()







