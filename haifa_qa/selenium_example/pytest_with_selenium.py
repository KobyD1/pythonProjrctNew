from selenium.webdriver.common.by import By

from haifa_qa.selenium_example.selenium_common import seleniumCommon


class TestPyTestWithSelenium():


    def setup(self):
        print ("into setup")
        common = seleniumCommon()
        self.driver = common.selenium_start("https://www.saucedemo.com/")


    def test_login_negative_test(self):
        print ("into login test ")
        user = self.driver.find_element(By.NAME, "user-name")
        password = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.ID, "login-button")
        user.click()
        user.send_keys("dsdsdsd")
        password.click()
        password.send_keys("fdfdfdfdf")
        login_button.click()
        url = self.driver.current_url
        assert url == "https://www.saucedemo.com/"
        self.driver.close()

    def test_login_positive_test(self):
        print ("into login test ")
        user = self.driver.find_element(By.NAME, "user-name")
        password = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.ID, "login-button")
        user.click()
        user.send_keys("standard_user")
        password.click()
        password.send_keys("secret_sauce")
        login_button.click()
        url = self.driver.current_url
        assert url =="https://www.saucedemo.com/inventory.html"
        self.driver.close()