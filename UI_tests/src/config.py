import os


class Config:
    browser = os.getenv('TEST_BROWSER', "chrome")
    app_host1 = "http://uitestingplayground.com/"
    app_host2 = "https://www.globalsqa.com/demo-site/draganddrop/"



