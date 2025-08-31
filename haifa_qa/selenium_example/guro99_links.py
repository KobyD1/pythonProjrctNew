# from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By

from haifa_qa.selenium_example.selenium_common import seleniumCommon

common = seleniumCommon()

driver = common.selenium_start("https://demo.guru99.com/Security/SEC_V1/index.php")

agile  = driver.find_element(By.PARTIAL_LINK_TEXT,"Agile")

agile.click()
user = driver.find_element(By.NAME,"uid")
password = driver.find_element(By.NAME,"password")
common.click_and_send_keys(user,"frffd")
common.click_and_send_keys(password,"dsssdsd")
login_button = driver.find_element(By.NAME,"btnLogin")
login_button.click()



common.selenium_end()