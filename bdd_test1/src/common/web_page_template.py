class WebPageTemplate:

    def __init__(self, webdriver_handler):
        self.web_driver_handler = webdriver_handler
        self.web_elements_cache = {}

    def get_element(self, selector):
        element = self.web_driver_handler.find_element(selector)
        return element

    def visit(self, url):
        self.web_driver_handler.visit(url)

