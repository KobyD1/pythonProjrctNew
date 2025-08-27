
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver


service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

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

first_price = driver.find_element(By.CLASS_NAME,"inventory_item_price")
price_text = first_price.text
price_text=price_text.replace("$","")
price_as_float = float(price_text)
if (price_as_float<50):
    print ("Price found its lower than 50$, test pass ")
else:
    print("Price found it is more than 50$- test failed  ")

prices = driver.find_elements(By.CLASS_NAME,"inventory_item_price")
for price in prices:
    price_as_text = price.text
    print (f"price found the value is {price_as_text}")


driver.close()
