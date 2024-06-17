from selenium.webdriver.common.by import By

from pageObjects.AccountPage import AccountPage
from pageObjects.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    email_address_field_id = "input-email"
    password_field_id = "input-password"
    login_button_xpath = "//input[@value='Login']"
    expected_message = "Warning: No match for E-Mail Address and/or Password."
    login_warning_message_xpath = "//div[@id='account-login']/div[1]"

    def enter_username_of_user(self, uname):
        self.type("email_address_field_id", self.email_address_field_id, uname)
        # self.driver.find_element(By.ID, self.email_address_field_id).click()
        # self.driver.find_element(By.ID, self.email_address_field_id).clear()
        # return self.driver.find_element(By.ID, self.email_address_field_id).send_keys(uname)

    def enter_password_of_user(self, password):
        self.type("password_field_id", self.password_field_id, password)
        # self.driver.find_element(By.NAME, self.password_field_id).click()
        # self.driver.find_element(By.NAME, self.password_field_id).clear()
        # return self.driver.find_element(By.NAME, self.password_field_id).send_keys(password)


    def click_on_login_button(self):
        self.click_on_element("login_button_xpath", self.login_button_xpath)
        # self.driver.find_element(By.XPATH, self.login_button_xpath).click()
        return AccountPage(self.driver)

    def verify_user_has_not_logged_in(self):
        return self.retrieve_element_text("login_warning_message_xpath", self.login_warning_message_xpath).__contains__(self.expected_message)
        # return self.driver.find_element(By.XPATH, self.login_warning_message_xpath).text.__contains__(self.expected_message)

    def Login_to_UI(self, uname, password):
        self.enter_username_of_user(uname)
        self.enter_password_of_user(password)
        return self.click_on_login_button()

