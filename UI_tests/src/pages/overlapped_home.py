from UI_test.UI_Playground.src.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class OverlappedHome(BasePage):
    def open(self):
        url="http://uitestingplayground.com/overlapped"
        return url


locators = {"button": (By.ID, "name")}


