from bdd_test1.src.locators.dynamic_home_locators import DynamicHomeLocators
from bdd_test1.src.pages.dynamic_home import DynamicHome
import time
from selenium.webdriver.common.by import By


class TestDynamic:

    def test_dynamic_id(self, webdriver_handler):
        dynamic = DynamicHome(webdriver_handler)
        dynamic.open_site()
        time.sleep(6)
        selector = (By.XPATH, DynamicHomeLocators.DYNAMIC_BTN)
        id_before = id(webdriver_handler.find_element(*selector))
        webdriver_handler.refresh()
        id_after = id(webdriver_handler.find_element(*selector))
        assert id_before != id_after, f"{id_after} is not {id_before}"









