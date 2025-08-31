import time

from selenium.webdriver.common.by import By

from haifa_qa.selenium_example.selenium_common import seleniumCommon

common = seleniumCommon()

driver = common.selenium_start("https://www.calculator.net/")
time.sleep(3)
button = driver.find_elements(By.CLASS_NAME,"btn.btn-primary.btn-lg")[1]
button.click()


common.selenium_end()