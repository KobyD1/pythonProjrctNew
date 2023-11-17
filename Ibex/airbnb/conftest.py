import pytest
from playwright.sync_api import sync_playwright, expect

from Ibex.airbnb.pages.paymentPage import paymentPage
from Ibex.airbnb.pages.resultsPage import resultsPage
from Ibex.airbnb.pages.placePage import placePage
from Ibex.airbnb.pages.commonPages import commonPages
from Ibex.airbnb.tests.globals import BASE_URL, BROWSER


@pytest.fixture()
def setup_browser():
    with sync_playwright() as playwright:
        if (BROWSER == 1):
            browser = playwright.chromium.launch(headless=False)
        else:
            browser = playwright.firefox.launch(headless=False)

        page = browser.new_page()
        page.goto(BASE_URL)
        common_pages = commonPages(page)
        results_page = resultsPage(page)
        place_Page = placePage(page)
        payment_page = paymentPage(page)
        common_pages.set_translator()

        yield common_pages, results_page, place_Page, payment_page
        page.close()
        browser.close()
