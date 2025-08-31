import time

from selenium.webdriver.common.by import By

from haifa_qa.selenium_example.selenium_common import seleniumCommon

common = seleniumCommon()
driver = common.selenium_start("https://www.calculator.net/")
random = driver.find_element(By.PARTIAL_LINK_TEXT,"Random")
random.click()
lower = driver.find_element(By.NAME,"slower")
lower.clear()
lower.send_keys("32")
upper = driver.find_element(By.NAME,"supper")
upper.clear()
upper.send_keys("55")
generate = driver.find_element(By.NAME,"x")
generate.click()
result_text = driver.find_element(By.CLASS_NAME,"verybigtext").text

print (f" result found the vlue is {result_text}")

common.selenium_end()