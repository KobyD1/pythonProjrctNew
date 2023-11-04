from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from Examples.PythonCharm.Python.Selenium.googleall.GoogleTests.BaseSelenium import BaseSelenium

base_selenium = BaseSelenium()
driver = base_selenium.selenium_init("https://connecteam.com/")

driver.find_element(By.TAG_NAME('a'))


input.clear()
input.send_keys("python")
input.send_keys(Keys.ENTER)


sleep(3)
base_selenium.test_end()
print ('noPom End')