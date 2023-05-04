from selenium import webdriver

from bdd_test1.src.common.webdriver_handler import WebDriverHandler

def before_scenario(context, scenario):
    context.webdriver_handler = WebDriverHandler()


def after_scenario(context, scenario):
    context.webdriver_handler.quit()

