from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@given(u"we have set the webbrowser settings to Chrome webdriver")
def set_browser(context):
    context.browser = webdriver.Chrome()
    assert hasattr(context, "browser"), "Driver not found in context"


@when(u"we type in a request for the weather in Google input field")
def step_open_website(context):
    context.browser.get("https://www.google.com/")


def step_type_in(context):
    context.browser.find_element(By.XPATH, '//textarea[@title="Search"]').send_keys("Weather")


def step_click_search(context):
    context.browser.find_element(By.XPATH, '//textarea[@title="Search"]').send_keys(Keys.ENTER)


@then(u'it shows the current weather in the region')
def step_assert_search(context):
    result = context.browser.find_element(By.XPATH, '//div[@id="taw"]')
    assert " Minsk" in result.text


