import pytest
from playwright.sync_api import sync_playwright
from minutes.common.globals import BROWSER, URL_MINUTES
from minutes.pages.minutes_welcome_page import welcomePage


@pytest.fixture()
def setup_browser():
    with sync_playwright() as playwright:
        if (BROWSER == 1):
            browser = playwright.chromium.launch(headless=False)
        else:
            browser = playwright.firefox.launch(headless=False)

        page = browser.new_page()
        page.goto(URL_MINUTES)
        welcome_page = welcomePage(page)

        yield page, welcome_page
        page.close()
        browser.close()
        print("Test end")
