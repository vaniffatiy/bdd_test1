from bdd_test1.src.common.web_page_template import WebPageTemplate


class BasePage(WebPageTemplate):

    def visit(self, url):
        self.web_driver_handler.visit(url)

    def get_element(self, selector):
        element = self.web_driver_handler.find_element(selector)
        return element

    def drag_and_drop(self, selector_source, selector_target):
        self.web_driver_handler.drag_drop(selector_source, selector_target)

    def drag_and_drop_offset(self, selector_source, xoff, yoff):
        self.web_driver_handler.drag_drop_offset(selector_source, xoff, yoff)

    def find_element(self, *selector):
        element = self.web_driver_handler.find_element(*selector)
        return element

    def refresh(self):
        self.web_driver_handler.refresh()

