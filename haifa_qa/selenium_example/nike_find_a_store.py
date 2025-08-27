
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver


service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://www.nike.com/il")

# using link text in all cases of element contains href
find_a_store = driver.find_element(By.PARTIAL_LINK_TEXT,"Find a")
find_a_store.click()

search = driver.find_element(By.ID,"ta-Location_input")
search.click()
search.send_keys("Haifa")
time.sleep(3)
search.send_keys(Keys.ENTER)
time.sleep(3)
stores = driver.find_elements(By.CLASS_NAME,"d-sm-flx.mt1-sm")
for store in stores:
    print (store.text)

driver.close()
