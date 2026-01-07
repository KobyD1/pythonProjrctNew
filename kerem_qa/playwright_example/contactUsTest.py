from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://advantageonlineshopping.com/#/https://advantageonlineshopping.com/#/")
    # contact_us = page.locator("[href='javascript:void(0)']")
    # contact_us.click()
    category = page.locator("[name='categoryListboxContactUs']")
    category.select_option(index=1)



    browser.close()