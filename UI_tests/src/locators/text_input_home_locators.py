from selenium.webdriver.common.by import By


class TextInputHomeLocators:
    url = "/textinput"
    input_field_locator = (By.ID, "newButtonName")
    changeable_btn_locator = (By.LINK_TEXT, "Button That Should Change it's Name Based on Input Value")



