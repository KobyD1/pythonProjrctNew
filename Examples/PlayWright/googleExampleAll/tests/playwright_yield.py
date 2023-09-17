import pytest
from playwright.sync_api import sync_playwright, expect

from Examples.PlayWright.googleExampleAll.pages.MainPage import MainPage
from Examples.PlayWright.googleExampleAll.pages.ResultsPage import ResultsPage
from Examples.PlayWright.googleExampleAll.tests.constants import BASE_URL


@pytest.fixture()
def setup_ebay():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(BASE_URL)
        main_page = MainPage(page)
        results_page = ResultsPage(page)
        yield main_page,results_page
        page.close()
        browser.close()


def test(setup_ebay):
    main_page,results_page = setup_ebay
    main_page.search("Cat")
    results_page.get_results()
