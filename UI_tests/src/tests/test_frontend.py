import pytest
from bdd_test1.src.pages.main_page import MainPage


class TestFrontend:

    @pytest.mark.smoke_gui
    def test_latest_stable_and_beta_releases_are_listed_on_main_page(self, webdriver_handler):
        main_page=MainPage(webdriver_handler)
        main_page.visit()

    @pytest.mark.smoke_gui
    def test_downloads_page_is_opened_when_downloads_link_is_clicked(self, webdriver_handler):
        main_page = MainPage(webdriver_handler)
        main_page.visit()


