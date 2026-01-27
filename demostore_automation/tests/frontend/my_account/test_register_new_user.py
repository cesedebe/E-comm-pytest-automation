

import pytest
from demostore_automation.src.pages.MyAccountSignedOutPage import MyAccountSignedOutPage
from demostore_automation.src.pages.MyAccountSignedInPage import MyAccountSignedInPage
# from demostore_automation.src.utilities import genericUtilities
from demostore_automation.src.utilities.genericUtilities import generate_random_email_and_password
from demostore_automation.src.utilities.genericUtilities   import generate_random_string


pytestmark = [pytest.mark.feregression, pytest.mark.fesmoke, pytest.mark.my_account]



@pytest.mark.usefixtures("init_driver")
class TestRegisterNewUser:


    @pytest.mark.tcid13
    @pytest.mark.pioneertcid2
    def test_register_valid_new_user(self):
        """
        Test to verify a valid user can register to the site.
        It generates a random email and password, then registers the user.
        :return:
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

        myacct_sin.verify_user_is_signed_out()


    @pytest.mark.tcid1385
    @pytest.mark.pioneertcid22
    def test_register_invalid_email(self):
        """
        Test to verify invalid email address is rejected by site.
        It generates a random email, then attempts to register the user.
        :return:
        """
        # create objects
        myacct = MyAccountSignedOutPage(self.driver)
        
        # go to my account page
        myacct.go_to_my_account()

        random_email = generate_random_string()

        # fill in email address  without @ for registration
        myacct.input_register_email(random_email)

        # click on 'register'
        myacct.click_register_button()

        myacct.check_validation_message_email_address("Please include an '@' in the email address.")


