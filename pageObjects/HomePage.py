from selenium.webdriver.common.by import By

from pageObjects.BasePage import BasePage
from pageObjects.LoginPage import LoginPage
from pageObjects.RegisterPage import RegisterPage
from pageObjects.SearchPage import SearchPage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    search_box_field_name = "search"
    search_button_xpath = "//button[@class='btn btn-default btn-lg']"
    my_account_drop_menu_xpath = "//a[@title='My Account']"
    login_option_xpath = "//a[normalize-space()='Login']"
    register_xpath = "//a[normalize-space()='Register']"


    def enter_product_into_search_field(self, product_name):
        self.type("search_box_field_name", self.search_box_field_name, product_name)
        # self.driver.find_element(*HomePage.search_box_field_name).click()
        # self.driver.find_element(*HomePage.search_box_field_name).clear()
        # self.driver.find_element(*HomePage.search_box_field_name).send_keys(product_name)

    def click_on_search_option(self):
        self.click_on_element("search_button_xpath", self.search_button_xpath)
        # self.driver.find_element(By.XPATH, self.search_button_xpath).click()
        return SearchPage(self.driver)

    def click_my_account_drop_menu(self):
        self.click_on_element("my_account_drop_menu_xpath", self.my_account_drop_menu_xpath)
        # return self.driver.find_element(By.XPATH, self.my_account_drop_menu_xpath).click()

    def click_on_login_option(self):
        self.click_on_element("login_option_xpath", self.login_option_xpath)
        # self.driver.find_element(By.XPATH, self.login_option_link_text).click()
        return LoginPage(self.driver)

    def click_on_Register_page(self):
        self.click_on_element("register_xpath", self.register_xpath)
        # self.driver.find_element(By.XPATH, self.register_xpath).click()
        return RegisterPage(self.driver)

    def search_for_product(self, product_name):
        self.enter_product_into_search_field(product_name)
        return self.click_on_search_option()

    def navigate_to_login_page(self):
        self.click_my_account_drop_menu()
        return self.click_on_login_option()

    def navigate_to_regiser_page(self):
        self.click_my_account_drop_menu()
        return self.click_on_Register_page()
