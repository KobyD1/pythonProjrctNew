import pytest
from playwright.sync_api import sync_playwright, expect

from kerem_qa.playwright_example.pages.login_page import loginPage
from kerem_qa.playwright_example.pages.product_page import productPage

expect.set_options(timeout=10_000)


@pytest.fixture()
def setup_playwright():
    print("### Test start ###")

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()


        yield page
        print("### Test end ###")
        page.close()
        browser.close()

@pytest.fixture()
def setup_playwright_with_users():
    print("### Test start into setup playwright with users###")

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()


        yield page
        print("### Test end ###")
        page.close()
        browser.close()