from playwright.sync_api import sync_playwright


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    user = page.locator("[id='user-name']")
    user.fill("standard_user")


    login_button = user.locator("[name='login-button']")
    login_button.click()










    page.close()
    browser.close()
    print ("Test end****")