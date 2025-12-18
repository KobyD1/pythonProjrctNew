from selenium.webdriver.common.by import By

from kerem_qa.selenium_example.seleniumBaseDalya import seleniumBaseDalya

base = seleniumBaseDalya()
exp_link = "Payment Calculator"
driver = base.selenium_start_with_url("https://www.ebay.com")
search_menu = driver.find_element(By.ID,"gh-ac")
search_menu.click()
search_menu.send_keys("Shoes")
search_button = driver.find_element(By.ID,"gh-search-btn")
search_button.click()
price_all = driver.find_element(By.CLASS_NAME,"su-card-container__attributes.su-card-container__attributes--has-secondary")
print (price_all.text)
price_all = driver.find_element(By.CSS_SELECTOR,"div[class='su-card-container__attributes.su-card-container__attributes--has-secondary']")

# su-card-container__attributes__primary
# su-card-container__attributes su-card-container__attributes--has-secondary





base.selenium_stop()