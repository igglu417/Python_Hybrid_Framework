from selenium.webdriver.common.by import By

from pageObjects.BasePage import BasePage


class AccountPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    edit_account_information_option_xpath = "//div[@id='account-account']/div/div/h2[1]"

    def confirm_login_is_success(self):
        return self.check_display_status_of_element("edit_account_information_option_xpath", self.edit_account_information_option_xpath)
        # return self.driver.find_element(By.XPATH, self.edit_account_information_option).is_displayed()


