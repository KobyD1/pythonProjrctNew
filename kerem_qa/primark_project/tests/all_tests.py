import unittest

from kerem_qa.primark_project.pages.main_page import MainPage
from kerem_qa.primark_project.tests.selenium_base_primark import seleniumBasePrimark


class allTests(unittest.TestCase):


    def setUp(self):
        self.base =  seleniumBasePrimark()
        self.driver = self.base.selenium_start_with_url("https://www.primark.com/en-gb")
        self.main_page = MainPage(self.driver)

    def tearDown(self):
        self.base.selenium_stop()

    def test_search_for_item(self):
        self.main_page.serach_for_item("Shirt")

    def test_click_on_gift_card_button(self):
        button_text = self.main_page.click_button_and_get_text("Gift")
        assert button_text == "Gift Card","Gift card button text is not as expected"

