from Utilities import ExcelUtils
from pageObjects.HomePage import HomePage
from Tests.BaseTest import BaseTest


class TestRegister(BaseTest):
    def test_register_with_mandatory_fields(self):
        homepage = HomePage(self.driver)
        registerpage = homepage.navigate_to_regiser_page()
        accountSuccess = registerpage.enter_registration_details(
            ExcelUtils.get_cell_data("..//ExcelFile//TestData.xlsx", "RegisterTest", 2, 1),
            ExcelUtils.get_cell_data("..//ExcelFile//TestData.xlsx", "RegisterTest", 2, 2),
            self.generate_email_with_timestamp(),
            "4561329875", "098765", "098765", "no", "select")
        assert accountSuccess.verify_user_logged_In()

    def test_register_with_all_fields(self):
        homepage = HomePage(self.driver)
        registerpage = homepage.navigate_to_regiser_page()
        accountSuccess = registerpage.enter_registration_details("davy", "jones", self.generate_email_with_timestamp(),
                                                                 "4561329875", "098765", "098765", "yes", "select")
        assert accountSuccess.verify_user_logged_In()

    def test_register_with_duplicate_account(self):
        homepage = HomePage(self.driver)
        registerpage = homepage.navigate_to_regiser_page()
        registerpage.enter_registration_details("davy", "jones", "john234d@gmail.com",
                                                "4561329875", "098765", "098765", "yes", "select")
        assert registerpage.verify_warning_message()

    def test_without_data(self):
        homepage = HomePage(self.driver)
        registerpage = homepage.navigate_to_regiser_page()
        registerpage.enter_registration_details("", "", "", "", "", "", "no", "no")
        registerpage.verify_all_errors()
