import pytest
from UI_test.UI_Playground.src.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HiddenHome(BasePage):


    @pytest.fixture
    def open_url(self):
        url="http://uitestingplayground.com/hiddenlayers"
        return url


locators = {"button": (By.ID, "greenButton")}


