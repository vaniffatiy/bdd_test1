import pytest
from UI_test.UI_Playground.src.pages.base_page import BasePage


class TextInputHome(BasePage):


    @pytest.fixture
    def get_input_url(self):
        url = "http://uitestingplayground.com/textinput"
        return url

locators = {
    "input_field": ("By.ID", "newButtonName"),
    "changeable_btn": ("By.LINK_TEXT", "Button That Should Change it's Name Based on Input Value")
}


