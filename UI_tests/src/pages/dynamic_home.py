from UI_test.UI_Test_3.MY_python_pytest.src.config import Config
from UI_test.UI_Test_3.MY_python_pytest.src.common.web_page_template import WebPageTemplate
from UI_test.UI_Test_3.MY_python_pytest.src.locators.dynamic_home_locators import DynamicHomeLocators
from selenium.webdriver.common.by import By


class DynamicHome(WebPageTemplate):

    def open_site(self):
        self.visit(url=Config.app_host+DynamicHomeLocators.url)

    def find_element(self):
        selector=(By.XPATH, DynamicHomeLocators.DYNAMIC_BTN)
        self.web_driver_handler.find_element(*selector)

    def refresh(self):
        self.refresh()







