import pytest
from playwright.sync_api import sync_playwright, expect

from Examples.PlayWright.pageObject.pages.LoginPage import LoginPage
from Examples.PlayWright.pageObject.tests.constants import BASE_URL

@pytest.fixture()

def get_playwright():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(BASE_URL)
        yield page
        page.close()
        browser.close()


def test(get_playwright):
    page = get_playwright
    print(get_playwright)
    expect(page).to_have_url("https://www.ebay.com/")