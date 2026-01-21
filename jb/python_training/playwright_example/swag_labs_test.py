from playwright.sync_api import sync_playwright


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    user = page.locator("[id='user-name']")
    user.fill("standard_user")


    login_button = page.locator("[name='login-button']")
    login_button.click()

    url = page.url
    print (F"url: {url}")
    if url == "https://www.saucedemo.com/":
        print ("####Test Pass####")
    else:
        print ("####Test Fail####")

    page.close()
    browser.close()
    print ("Test end****")