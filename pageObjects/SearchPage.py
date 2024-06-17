from selenium.webdriver.common.by import By

from pageObjects.BasePage import BasePage


class SearchPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    validate_product_link_text = "HP LP3065"
    no_product_message_xpath = "//p[contains(text(),'There is no product')]"


    def display_status_of_product(self):
        return self.check_display_status_of_element("validate_product_link_text", self.validate_product_link_text)
        # return self.driver.find_element(By.LINK_TEXT, self.validate_product_link_text).is_displayed()

    def retrieve_no_product_message(self):
        return self.retrieve_element_text("no_product_message_xpath", self.no_product_message_xpath)
        # return self.driver.find_element(By.XPATH, self.no_product_message_xpath).is_displayed()

