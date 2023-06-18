import pytest
from playwright.sync_api import Page, expect, sync_playwright
from bendaPlayWright.pages.CategoryPage import CategoryPage
from bendaPlayWright.pages.WelcomePage import WelcomePage

URL = "https://benda2b.co.il/#/store"


@pytest.fixture(scope="function", autouse=True)
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(URL)
        yield page
        page.close()
        browser.close()


def test_sanity(page: Page):
    welcome_page = WelcomePage(page)
    expect(page).to_have_url(URL)


def test_get_product_amount(page: Page):
    welcome_page = WelcomePage(page)
    cat_page = CategoryPage(page)
    welcome_page.click_on_category(0) # category - describe the index of the category
    cat_page.get_products_amount()


def test_get_products_details(page: Page):
    welcome_page = WelcomePage(page)
    cat_page = CategoryPage(page)
    welcome_page.click_on_category(0)
    cat_page.get_products_details(4) # 0 - f0r all products in page , any other number for partial print start from 1
