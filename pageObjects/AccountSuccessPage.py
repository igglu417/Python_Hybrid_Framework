from selenium.webdriver.common.by import By

from pageObjects.BasePage import BasePage


class AccountSuccessPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    verify_successful_acount_creation_xpath = "//div[@id='content']/h1"
    exp_text = "Your Account Has Been Created!"

    def verify_user_logged_In(self):
        return self.retrieve_element_text("verify_successful_acount_creation_xpath", self.verify_successful_acount_creation_xpath).__eq__(self.exp_text)
        # return self.driver.find_element(By.XPATH, self.verify_successful_acount_creation).text.__eq__(self.exp_text)

