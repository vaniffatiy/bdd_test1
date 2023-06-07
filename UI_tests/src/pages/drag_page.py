from bdd_test1.src.pages.base_page import BasePage
from bdd_test1.src.locators.drag_page_locators import DragPageLocators
from selenium.webdriver.common.by import By


class DragPage(BasePage):

    def open_site(self):
        self.visit(url=DragPageLocators.url)

    def find_element(self, locator):
        selector = (By.XPATH, locator)
        self.web_driver_handler.find_element(*selector)

    def drag_drop(self):
        self.drag_and_drop(DragPageLocators.SOURCE_IMG, DragPageLocators.TRASH_FIELD)

    def drag_drop_offset(self):
        source = DragPageLocators.SOURCE_IMG2
        x = DragPageLocators.OFFSET["xoffset"]
        y = DragPageLocators.OFFSET["yoffset"]
        self.drag_and_drop_offset(source, x, y)

    def refresh(self):
        self.refresh()







