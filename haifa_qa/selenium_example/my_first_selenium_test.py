
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver


service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://www.ebay.com")

search=driver.find_element(By.ID,"gh-ac")
search.click()
search.send_keys("Johnson")
search.send_keys(Keys.ENTER)


driver.close()
print ("test end")
