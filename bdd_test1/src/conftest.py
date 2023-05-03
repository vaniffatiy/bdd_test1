import pytest
from bdd_test1.src.common.webdriver_handler import WebDriverHandler


@pytest.fixture(scope="function")
def webdriver_handler():
    webdriver = WebDriverHandler()
    webdriver.setup()
    yield webdriver
    webdriver.quit()



