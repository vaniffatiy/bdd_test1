import requests
import re
from pyshould import *
from behave import given, when, then, step
from capybara.dsl import *
from selenium.webdriver.common.keys import Keys


URL_GOOGLE_TW = 'https://www.google.com.tw/?gl=tw'
URL_GOOGLE_TW_SEARCH = 'https://www.google.com.tw/search?gl=tw'


@given('I am on the Google TW page')
def step_impl(context):
    r = requests.get(URL_GOOGLE_TW)
    assert int(r.status_code / 100) == 2


@when('I search \'{keyword}\'')
def step_impl(context, keyword):
    payload = {'q': keyword}
    r = requests.get(URL_GOOGLE_TW_SEARCH, params=payload)
    int(r.status_code / 100) | should.equal(2)
    # print(r.text)
    context.result_count = count_search_results(r.text)


@then('I can see many results.')
def step_impl(context):
    assert context.failed is False
    print(context.result_count)
    assert len(context.result_count) > 0
    assert context.result_count != 0
