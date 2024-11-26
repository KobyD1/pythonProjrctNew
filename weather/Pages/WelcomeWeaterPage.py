import time
from telnetlib import EC

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class welcomeWeatherPage(object):


    def __init__(self, driver):
        self.__driver = driver
        self.driver = driver

        self.__search_locator = "LocationSearch_input"
        self.__results_locator = "a[data-from-string='locationCard']"



    def search_by_zip(self,zip_to_send):
        search_element = self.__driver.find_element(By.ID,self.__search_locator)
        search_element.click()
        search_element.send_keys(zip_to_send)
        search_element.send_keys(Keys.ENTER)

    def get_tempature(self):

        search_results = self.__driver.find_element(By.CSS_SELECTOR,self.__results_locator)
        tempature_text = search_results.text
        print (f"Tempature found the value is {tempature_text} ")
        tempature_text=tempature_text[-1:]
        return tempature_text


    def search_and_get_tempature_by_zip(self,zip):
        self.search_by_zip(zip)
        self.get_tempature()

