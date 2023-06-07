from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@given(u"I have set the webbrowser settings to Chrome webdriver")
def set_browser(context):
    context.driver = webdriver.Chrome()
    assert hasattr(context, "driver"), "Driver not found in context"


@given(u"I am on the main page")
def step_open_website(context):
    context.driver.get("https://www.google.com/")


@when(u'I type in {search_query} in Google input field')
def step_type_in(context, search_query):
    print(f"search_query = {search_query}")
    search_box = context.driver.find_element(By.NAME, 'q')
    search_box.send_keys(search_query)


@when(u'click Enter key')
def step_click_search(context):
    context.driver.find_element(By.NAME, 'q').send_keys(Keys.ENTER)


@then(u'I see the weather reports')
def step_assert_search(context):
    # results = context.driver.find_element(By.XPATH, '//div[@id="taw"]')
    # results = context.driver.find_element(By.XPATH, '//div[@class="g"]')
    results = context.driver.find_elements(By.XPATH, "//div[@class='ULSxyf']")
    # assert "weather" in results.text
    assert len(results) > 0


