from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from bdd_test1.src.config import Config
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class WebDriverHandler:

    # def setup(self):
    #     browser_to_use = Config.browser
    #     print(f"starting driver for browser: {browser_to_use}")
    #     if browser_to_use is None:
    #         raise Exception(
    #             "Unable to identify test browser. Set the environment variable {TEST_BROWSER} with one of the values: chrome,firefox")
    #     if browser_to_use == "chrome":
    #         chrome_options = webdriver.ChromeOptions()
    #         # chrome_options.add_argument("--headless") # comment if you want to use headless mode
    #         chrome_options.add_argument("--disable-extensions")
    #         chrome_options.add_argument("--window-size=1420,1080")
    #         chrome_options.add_argument("--incognito")
    #         chrome_options.add_argument("--disable-popup-blocking")
    #         chrome_options.add_argument("--disable-default-apps")
    #         chrome_options.add_argument("--disable-infobars")
    #         chrome_options.add_argument("--disable-gpu")
    #         chrome_options.add_argument("--no-sandbox")
    #         chrome_options.add_argument(
    #             '--user-agent=secret')  # just to ilustrate how to set chrome options that have value assigned
    #         self.web_driver_instance = webdriver.Chrome(desired_capabilities=chrome_options.to_capabilities())
    #         self.web_driver_instance.delete_all_cookies()  # we want to start fresh
    driver = webdriver.Chrome()

    def find_element(self, selector):
        element = self.driver.find_element(By.XPATH, selector)
        return element

    def drag_drop(self, selector_source, selector_target):
        action = ActionChains(self.driver)
        source = self.find_element(selector_source)
        target = self.find_element(selector_target)
        action.drag_and_drop(source, target).perform()

    def drag_drop_offset(self, selector_source, xoff, yoff):
        action = ActionChains(self.driver)
        source = self.find_element(selector_source)
        action.drag_and_drop_by_offset(source, xoff, yoff).perform()

    def visit(self, url):
        self.driver.get(url)

    def refresh(self):
        self.driver.refresh()

    def do_click(self, by_locator):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator)).click

    def do_send_keys(self, by_locator, text):
        return WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(by_locator)).send_keys(text)

    def check_if_visible(self, by_locator):
        button_check = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator))
        return bool(button_check)

    def find_element_with_explicit_wait(self, selector, timeout=15):
        element = WebDriverWait(self.driver, timeout).until(
            lambda x: x.find_element(selector))
        return element

    def quit(self):
        self.driver.quit()

    def close(self):
        self.driver.close()


