from selenium.webdriver.common.by import By

from Ashdod.Selenium.SeleniumMaster import SeleniumMaster

master = SeleniumMaster()
driver = master.selenium_start("https://www.saucedemo.com/")

user  = driver.find_element(By.ID,"user-name")
user.click()
user.clear()
user.send_keys("standard_user")


password = driver.find_element(By.ID,"password")
password.click()
password.clear()
password.send_keys("secret_sauce")

login_btn = driver.find_element(By.ID,'login-button')
login_btn.click()

prices = driver.find_elements(By.CLASS_NAME,"inventory_item_price")
price_text  = prices [3].text
for price in prices:
    print (price.text)


master.selenium_close(driver)