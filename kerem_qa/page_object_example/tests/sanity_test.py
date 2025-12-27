import unittest

from kerem_qa.page_object_example.pages.login_page import loginPage
from kerem_qa.page_object_example.tests.selenium_base_example import seleniumBaseExample


class sanityTest(unittest.TestCase):


    def setUp(self):
        self.base =  seleniumBaseExample()
        self.driver = self.base.selenium_start_with_url("https://www.saucedemo.com/")
        self.login_page = loginPage(self.driver)

    def tearDown(self):
        self.base.selenium_stop()


    def test_login_with_correct_parameters(self):
        print ("into login with correct parameters test")
        self.login_page.set_user_and_password("standard_user","secret_sauce")
        self.login_page.click_on_login_button()
        assert self.driver.current_url == 'https://www.saucedemo.com/inventory.html',"URL did not set as expected after login"


    def test_login_with_incorrect_password(self):
        print ("into login with correct parameters test")
        self.login_page.set_user_and_password("standard_user","incorrect_password")
        self.login_page.click_on_login_button()

        # item34daf06344 > div > div.su-card-container__content > div.su-card-container__attributes > div > div:nth-child(1) > span.su-styled-text.primary.bold.large-1.s-card__price
        assert self.driver.current_url == 'https://www.saucedemo.com/',"URL did not set as expected after login"