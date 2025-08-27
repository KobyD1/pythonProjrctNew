# from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By

from haifa_qa.selenium_example.selenium_common import seleniumCommon

common = seleniumCommon()

driver = common.selenium_start("https://www.saucedemo.com/")


user = driver.find_element(By.NAME,"user-name")
password = driver.find_element(By.ID,"password")
login_button = driver.find_element(By.ID,"login-button")

user.click()
user.clear()
user.send_keys("standard_user")

password.click()
password.clear()
password.send_keys("secret_sauce")

login_button.click()

url = driver.current_url

print(url)

if (url =="https://www.saucedemo.com/inventory.html"):
    print ("###### TEST PASS #####")


common.selenium_end()