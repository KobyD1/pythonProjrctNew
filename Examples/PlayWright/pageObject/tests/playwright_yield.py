import pytest
from playwright.sync_api import sync_playwright, expect
from Examples.PlayWright.pageObject.tests.constants import BASE_URL

@pytest.fixture()
def setup_ebay():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(BASE_URL)
        yield page
        page.close()
        browser.close()


def test(setup_ebay):
    page = setup_ebay
    print(setup_ebay)
    expect(page).to_have_url("https://www.ebay.com/")