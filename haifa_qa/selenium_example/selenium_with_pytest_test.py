from selenium.webdriver.common.by import By

from haifa_qa.selenium_example.selenium_common import seleniumCommon


class TestSeleniumWithPytest():


    def setup(self):
        self.common = seleniumCommon()
        self.driver = self.common.selenium_start("https://www.saucedemo.com/")

    def test_login_positive(self):
        print ("into login possitive test ")

        user = self.driver.find_element(By.NAME, "user-name")
        password = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.ID, "login-button")

        user.click()
        user.clear()
        user.send_keys("standard_user")

        password.click()
        password.clear()
        password.send_keys("secret_sauce")

        login_button.click()

        url = self.driver.current_url
        assert url == 'https://www.saucedemo.com/inventory.html',"URL is not as expected after login"
        self.common.selenium_end()

    def test_login_negative(self):
        print ("into login negative ")