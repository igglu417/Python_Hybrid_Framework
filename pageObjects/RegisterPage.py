from selenium.webdriver.common.by import By
from pageObjects.AccountSuccessPage import AccountSuccessPage
from pageObjects.BasePage import BasePage


class RegisterPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    first_name_field_xpath = "//input[@id='input-firstname']"
    last_name_field_id = "input-lastname"
    email_field_id = "input-email"
    contact_number_field_id = "input-telephone"
    set_password_field_id = "input-password"
    confirm_set_password_field_id = "input-confirm"
    click_on_checkbox_field_xpath = "//input[@type='checkbox']"
    click_on_submit_xpath = "//input[@type='submit']"
    subscribe_button_xpath = "//label[@class='radio-inline'][1]"
    warning_mesage_css = ".alert-danger"
    warning_text = "Warning: E-Mail Address is already registered!"
    first_name_warning_locator_xpath = "//input[@id='input-firstname']/following-sibling::div"
    first_name_error = "First Name must be between 1 and 32 characters!"
    privacy_policy_warning_text = "Warning: You must agree to the Privacy Policy!"
    privacy_polocy_css = ".alert-danger"


    def enter_first_name(self, fname):
        self.type("first_name_field_xpath", self.first_name_field_xpath, fname)
        # self.driver.find_element(By.XPATH, self.first_name_field_xpath).click()
        # self.driver.find_element(By.XPATH, self.first_name_field_xpath).clear()
        # self.driver.find_element(By.XPATH, self.first_name_field_xpath).send_keys(fname)

    def enter_last_name(self, lname):
        self.type("last_name_field_id", self.last_name_field_id, lname)
        # self.driver.find_element(By.NAME, self.last_name_field_id).click()
        # self.driver.find_element(By.NAME, self.last_name_field_id).clear()
        # self.driver.find_element(By.NAME, self.last_name_field_id).send_keys(lname)

    def enter_email_address(self, mail):
        self.type("email_field_id", self.email_field_id, mail)
        # self.driver.find_element(By.NAME, self.email_field_id).click()
        # self.driver.find_element(By.NAME, self.email_field_id).clear()
        # self.driver.find_element(By.NAME, self.email_field_id).send_keys(mail)

    def enter_telephone_details(self, phone):
        self.type("contact_number_field_id", self.contact_number_field_id, phone)
        # self.driver.find_element(By.NAME, self.contact_number_field_id).click()
        # self.driver.find_element(By.NAME, self.contact_number_field_id).clear()
        # self.driver.find_element(By.NAME, self.contact_number_field_id).send_keys(phone)

    def enter_password(self, password):
        self.type("set_password_field_id", self.set_password_field_id, password)
        # self.driver.find_element(By.NAME, self.set_password_field_id).click()
        # self.driver.find_element(By.NAME, self.set_password_field_id).clear()
        # self.driver.find_element(By.NAME, self.set_password_field_id).send_keys(password)

    def enter_to_confirm_password(self, confirm):
        self.type("confirm_set_password_field_id", self.confirm_set_password_field_id, confirm)
        # self.driver.find_element(By.NAME, self.confirm_set_password_field_id).click()
        # self.driver.find_element(By.NAME, self.confirm_set_password_field_id).clear()
        # self.driver.find_element(By.NAME, self.confirm_set_password_field_id).send_keys(confirm)

    def click_on_checkbox(self):
        self.click_on_element("click_on_checkbox_field_xpath", self.click_on_checkbox_field_xpath)
        # self.driver.find_element(By.XPATH, self.click_on_checkbox_field_xpath).click()

    def click_on_submit_button(self):
        self.click_on_element("click_on_submit_xpath", self.click_on_submit_xpath)
        # self.driver.find_element(By.XPATH, self.click_on_submit_xpath).click()
        return AccountSuccessPage(self.driver)

    def click_radio_button_to_subscribe(self):
        self.click_on_element("subscribe_button_xpath", self.subscribe_button_xpath)
        # self.driver.find_element(By.XPATH, self.subscribe_button_xpath).click()

    def verify_warning_message(self):
        return self.retrieve_element_text("warning_mesage_css", self.warning_mesage_css).__eq__(self.warning_text)
        # return self.driver.find_element(By.CSS_SELECTOR, self.warning_mesage_css).text.__eq__(self.warning_text)

    def retrieve_privacy_policiy_warning(self):
        return self.retrieve_element_text("privacy_polocy_css", self.privacy_polocy_css).__eq__(self.warning_text)
        # return self.driver.find_element(By.CSS_SELECTOR, self.privacy_polocy_css).text.__eq__(self.privacy_policy_warning_text)

    def first_name_warning(self):
        return self.retrieve_element_text("first_name_warning_locator_xpath", self.first_name_warning_locator_xpath).__eq__(self.warning_text)
        # return self.driver.find_element(By.XPATH, self.first_name_warning_locator_xpath).text.__eq__(self.first_name_error)

    def verify_all_errors(self):
        self.retrieve_privacy_policiy_warning()
        self.first_name_warning()

    # def verify_all_warnings(self, expected_privacy_policy_warning, expected_first_name_warning_message,
    #                         expected_last_name_warning_message, expected_email_warning_message,
    #                         expected_telephone_warning_message, expected_password_warning_message):
    #     actual_privacy_policy_warning = self.retrieve_privacy_policy_warning()
    #     actual_first_name_warning_message = self.retrieve_first_name_warning()
    #     actual_last_name_warning_message = self.retrieve_last_name_warning()
    #     actual_email_warning_message = self.retrieve_email_warning()
    #     actual_telephone_warning_message = self.retrieve_telephone_warning()
    #     actual_password_warning_message = self.retrieve_password_warning()
    #
    #     status = False
    #
    #     if expected_privacy_policy_warning.__contains__(actual_privacy_policy_warning):
    #         if expected_first_name_warning_message.__eq__(actual_first_name_warning_message):
    #             if expected_last_name_warning_message.__eq__(actual_last_name_warning_message):
    #                 if expected_email_warning_message.__eq__(actual_email_warning_message):
    #                     if expected_telephone_warning_message.__eq__(actual_telephone_warning_message):
    #                         if expected_password_warning_message.__eq__(actual_password_warning_message):
    #                             status = True
    #
    #     return status


    def enter_registration_details(self, fname, lname, mail, phone, password, confirm, yes_or_no, privacy_policy):
        self.enter_first_name(fname)
        self.enter_last_name(lname)
        self.enter_email_address(mail)
        self.enter_telephone_details(phone)
        self.enter_password(password)
        self.enter_to_confirm_password(confirm)
        if yes_or_no.__eq__("yes"):
            self.click_radio_button_to_subscribe()
        if privacy_policy.__eq__("select"):
            self.click_on_checkbox()
        return self.click_on_submit_button()
