from time import sleep

from selenium.webdriver.common.by import By

from PythonCharm.Python.Selenium.Selenium4.BaseSelenium import BaseSelenium


class newtours_link(BaseSelenium):


    base = BaseSelenium()
    driver = base.selenium_init("https://demo.guru99.com/test/newtours/")
    sleep(3)
    register = driver.find_element(By.LINK_TEXT,"REGISTER")
    register.click()

    link2=driver.find_element(By.PARTIAL_LINK_TEXT,"SUPP")
    link2.click()
    base.test_end()

    print('test success ')
