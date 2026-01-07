from kerem_qa.playwright_example.pages.login_page import loginPage


class TestLogin():


    def test_calculator(self,setup_playwright):
        page = setup_playwright
        page.goto("https://www.calculator.net")
        print ("Test end")

    def test_calculator_with_fixture_2(self,setup_playwright_with_users):
        page = setup_playwright_with_users
        page.goto("https://www.calculator.net")
        print ("Test end")

    def test_login_swag_lab(self,setup_playwright_swaglabs):
        page ,login_page, product_page,excel_utils = setup_playwright_swaglabs
        login_page.login("standard_user","secret_sauce")
        login_page.verify_login_success()

    def test_login_swag_lab_with_incorrect_parameters(self,setup_playwright_swaglabs):
        page,login_page, product_page,excel_utils = setup_playwright_swaglabs
        login_page.login("standard_user","fake")
        login_page.verify_login_fail()


    def test_get_products_prices_to_excel(self,setup_playwright_swaglabs):
        page ,login_page, product_page,excel_utils = setup_playwright_swaglabs
        login_page.login("standard_user","secret_sauce")
        product_page.verify_product_prices()











