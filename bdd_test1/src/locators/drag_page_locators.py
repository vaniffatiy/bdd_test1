from selenium.webdriver.common.by import By


class DragPageLocators:
    url = "https://demo.automationtesting.in/Static.html"
    SOURCE_IMG = '//img[@id="angular"]'
    TRASH_FIELD = '//div[@id="droparea"]'
    SOURCE_IMG2 = '//img[@id="mongo"]'
    OFFSET = {"xoffset": 30, "yoffset": 50}
    print(OFFSET["yoffset"])


