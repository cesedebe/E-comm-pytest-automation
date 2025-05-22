import pytest
from demostore_automation.src.pages.MyAccountSignedOutPage import MyAccountSignedOutPage
from demostore_automation.src.pages.MyAccountSignedInPage import MyAccountSignedInPage
from demostore_automation.src.utilities.genericUtilities import generate_random_email_and_password


pytestmark = [pytest.mark.feregression, pytest.mark.fesmoke, pytest.mark.my_account]

@pytest.mark.usefixtures("init_driver")

class TestSignedInPage:

    @pytest.mark.tcid20
    def test_signed_in_page_has_breadcrumb (self):
        """
        Verify Sign in Page has correct Breadcrumb
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

        #get actual breadcrumb
        actual_breadcrumb = myacct_sin.get_breadcrumb().strip()

        expected_bc = "Home / My account"

        # compare actual to expected breadcrumb
        assert ( actual_breadcrumb == expected_bc), f"Breadcrumb mismatch! Found: {actual_breadcrumb} Expected: {expected_bc}"

        myacct_sin.verify_user_is_signed_out()

    @pytest.mark.tcid201
    def test_signed_in_page_has_title(self):
        """
        Verify Sign in Page has correct Title
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

        # get actual title
        actual_title = myacct_sin.get_my_account_page_title().strip()

        expected_title = "My account"

        # compare actual to expected title
        assert (actual_title == expected_title), f"Title mismatch! Found: {actual_title} Expected: {expected_title}"

        myacct_sin.verify_user_is_signed_out()

    @pytest.mark.tcid202
    def test_signed_in_page_has_display_name(self):
        """
        Verify Sign in Page has display name
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

        # get actual display name
        actual_name = myacct_sin.get_user_display_name().strip()

        expected_name= random_info['email'].split("@")[0]

        # compare actual to expected title
        assert (actual_name == expected_name), f"Display Name Mismatch! Found: {actual_name} Expected: {expected_name}"

        myacct_sin.verify_user_is_signed_out()