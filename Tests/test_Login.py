from Tests.BaseTest import BaseTest
from Utilities import ExcelUtils
from pageObjects.HomePage import HomePage
import pytest



class TestLogin(BaseTest):

    def test_with_Valid_Credentials(self):
        homepage = HomePage(self.driver)
        loginpage = homepage.navigate_to_login_page()
        accountpage = loginpage.Login_to_UI("john234d@gmail.com", "123456789")
        assert accountpage.confirm_login_is_success()

    def test_with_invalid_credentials(self):
        homepage = HomePage(self.driver)
        loginpage = homepage.navigate_to_login_page()
        loginpage.Login_to_UI(self.generate_email_with_timestamp(), "12789")
        assert loginpage.verify_user_has_not_logged_in()


    def test_empty_credentials(self):
        homepage = HomePage(self.driver)
        loginpage = homepage.navigate_to_login_page()
        loginpage.Login_to_UI("", "")
        assert loginpage.verify_user_has_not_logged_in()


    @pytest.mark.parametrize("email, password", ExcelUtils.get_data_from_excel("..//ExcelFile//TestData.xlsx", "LoginTest"))
    def test_with_Valid_Credentials_with_excel(self, email, password):
        homepage = HomePage(self.driver)
        loginpage = homepage.navigate_to_login_page()
        accountpage = loginpage.Login_to_UI(email, password)
        assert accountpage.confirm_login_is_success()

