from selenium.webdriver.common.by import By

from Ashdod.Selenium.SeleniumMaster import SeleniumMaster

master = SeleniumMaster()
driver = master.selenium_start("https://www.calculator.net/password-generator.html")
boxes = driver.find_elements(By.CLASS_NAME,"cbmark")
box = boxes[2]
box.click()

master.selenium_close(driver)