import pytest

from playwright.sync_api import sync_playwright, expect

from tipalti.dev_dogs.pages.dog_page import dogPage
from tipalti.dev_dogs.pages.welcome_page import welcomePage
from tipalti.dev_dogs.utils.globals import BROWSER, URL


@pytest.fixture()
def setup_dev_dogs():
    print("### Test start ###")

    with sync_playwright() as playwright:
        if (BROWSER == 1):
            browser = playwright.chromium.launch(headless=False)
        else:
            browser = playwright.firefox.launch(headless=False)

        page = browser.new_page()
        page.goto(URL)
        welcome_page = welcomePage(page)
        dog_page = dogPage(page)
        yield page, welcome_page, dog_page
        page.close()
        browser.close()
        print("### Test end ###")
