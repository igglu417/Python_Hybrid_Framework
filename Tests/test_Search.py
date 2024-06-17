import pytest
from pageObjects.HomePage import HomePage
from Tests.BaseTest import BaseTest



class TestSearch(BaseTest):
    def test_search_for_valid_product(self):
        homepage = HomePage(self.driver)
        searchPage = homepage.search_for_product("HP")
        assert searchPage.display_status_of_product()

    def test_search_for_invalid_product(self):
        homepage = HomePage(self.driver)
        searchPage = homepage.search_for_product("Burger King")
        assert searchPage.retrieve_no_product_message()

    def test_search_without_entering_any_product(self):
        homepage = HomePage(self.driver)
        searchPage = homepage.search_for_product("")
        assert searchPage.retrieve_no_product_message()
