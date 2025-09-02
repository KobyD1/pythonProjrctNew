import time

from selenium.webdriver.common.by import By

from haifa_qa.selenium_example.selenium_common import seleniumCommon
low_number = "32"
high_number="55"
common = seleniumCommon()
driver = common.selenium_start("https://www.calculator.net/")
random = driver.find_element(By.PARTIAL_LINK_TEXT,"Random")
random_text = random.text
assert random_text=="Random Number Generator","The text over Random button is not as exepcted "

random.click()
lower = driver.find_element(By.NAME,"slower")
lower.clear()
lower.send_keys(low_number)
upper = driver.find_element(By.NAME,"supper")
upper.clear()
upper.send_keys(high_number)
generate = driver.find_element(By.NAME,"x")
generate.click()
result_text = driver.find_element(By.CLASS_NAME,"verybigtext").text

assert len(result_text)==2,"The number is not double digit as expected "
result_text_as_int = int (result_text)
assert result_text_as_int>int(low_number), "the number that genereted is not more than 32 as expected  "

print (f" result found the vlue is {result_text}")

common.selenium_end()