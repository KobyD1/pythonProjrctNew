

class TestSwagLabsTest():

    def test_login(self,setup_playwright):
        print("test_login")
        page = setup_playwright
        page.goto("https://www.saucedemo.com/")


