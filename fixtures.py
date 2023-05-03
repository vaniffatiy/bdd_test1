import pytest
from behave import fixture
from selenium import webdriver
from selenium.webdriver import Keys

driver = webdriver.Chrome()
from selenium.webdriver.common.by import By

@pytest.fixture
def search_query():
    return "Weather today"


@pytest.fixture()
def click_element():
    click=driver.find_element(By.NAME, 'q').send_keys(Keys.ENTER)
    return click