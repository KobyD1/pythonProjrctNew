from selenium.webdriver.common.by import By

from Examples.PythonCharm.Python.Selenium.Selenium4.BaseSeleniumCommon import BaseSeleniumCommon

base = BaseSeleniumCommon()
driver = base.selenium_init("https://www.ebay.com/")
search = driver.find_element(By.ID,"gh-ac")
search.click()
search.send_keys("Selenium")
base.test_end()
