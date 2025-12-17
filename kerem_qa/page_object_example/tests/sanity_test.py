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


    def test_login_with_correct_parameeters(self):
        print ("into login with correct parameters test")
        self.login_page.set_user_and_password("standard_user","secret_sauce")
        self.login_page.click_on_login_button()