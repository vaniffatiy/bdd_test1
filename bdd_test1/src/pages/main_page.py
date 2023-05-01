
from UI_test.UI_Test_3.MY_python_pytest.src.common.web_page_template import WebPageTemplate


class MainPage(WebPageTemplate):

    def visit(self, url,locator):
        self.visit_and_verify(url, locator)

    def switch_to(self,locator):
        self.verify_page_has_been_loaded(locator)



