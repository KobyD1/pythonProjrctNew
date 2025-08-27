
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

url = driver.current_url

print(url)

if (url =="https://www.saucedemo.com/inventory.html"):
    print ("###### TEST PASS #####")

driver.close()
