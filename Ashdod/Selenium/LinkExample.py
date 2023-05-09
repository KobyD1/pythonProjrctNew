from selenium.webdriver.common.by import By

from Ashdod.Selenium.SeleniumMaster import SeleniumMaster

master = SeleniumMaster()
driver = master.selenium_start("http://the-internet.herokuapp.com/")
#
# link_to_image = driver.find_element(By.LINK_TEXT,"Broken Images")
# link_to_image.click()
link_to_image_partial = driver.find_element(By.PARTIAL_LINK_TEXT,"Drag")
link_to_image_partial.click()
master.selenium_close(driver)
