from selenium.webdriver.common.by import By

from PythonCharm.Python.Selenium.Selenium4.BaseSelenium import BaseSelenium


class AutomationpractisLink(BaseSelenium):
    base=BaseSelenium()
    driver= base.selenium_init("https://demo.guru99.com/test/newtours/reservation.php")
     # "http://automationpractice.com/index.php?id_category=3&amp;controller=category"
    user = driver.find_element(By.CLASS_NAME,'mouseOver')

    base.test_end()