from time import sleep

from selenium.webdriver.common.by import By

from Examples.PythonCharm.Python.Selenium.googleall.GoogleTests.BaseSelenium import BaseSelenium


class calculator_link(BaseSelenium):


    base = BaseSelenium()
    driver = base.selenium_init("https://www.calculator.net/math-calculator.html")


    link2=driver.find_element(By.LINK_TEXT,"OTHER")
    link2.click()
    base.test_end()

    print('test success ')
