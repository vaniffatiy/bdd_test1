from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def before_all(context, feature):
    service = Service(ChromeDriverManager(version="94.0.4606.61").install())
    context.driver = webdriver.Chrome(service=service)


def after_all(context, feature):
    context.driver.quit()

