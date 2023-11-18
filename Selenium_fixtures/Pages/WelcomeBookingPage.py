import time

from selenium.common import WebDriverException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from noTraffic.Pages.Locators import WelcomePageLocators


class welcomeBookingPage(object):


    def __init__(self, driver):
        self.driver = driver
        self.search_menu = self.driver.find_element(By.ID,":re:")


    def click_on_search_menu(self,text):
        self.search_menu.click()
        self.search_menu.send_keys(text)

    def close_pop_up(self):
        time.sleep(3)
        close_button = self.driver.find_elements(By.CSS_SELECTOR, "div[class*='abcc616ec7']")[1]
        close_button.click()
