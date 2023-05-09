from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# from selenium.webdriver.support.select import Select
from Ashdod.Selenium.SeleniumMaster import SeleniumMaster

master = SeleniumMaster()
driver = master.selenium_start("http://the-internet.herokuapp.com/dropdown")
dropdown = Select (driver.find_element(By.ID,"dropdown"))
dropdown.select_by_index(1)
dropdown.select_by_visible_text("Option 1")


master.selenium_close(driver)