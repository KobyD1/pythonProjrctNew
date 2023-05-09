from selenium.webdriver.common.by import By

from Ashdod.Selenium.SeleniumMaster import SeleniumMaster

master = SeleniumMaster()
driver = master.selenium_start("https://demo.applitools.com/#")
user_name = driver.find_element(By.ID,"username")
user_name.click()
user_name.clear()
user_name.send_keys("aa")

password = driver.find_element(By.ID,"password")
password.click()
password.clear()
password.send_keys("password")
login_btn = driver.find_element(By.ID,"log-in")
login_btn.click()

header= driver.find_element(By.ID,"time")
header_text = header.text
index = header_text.index(":")
header_suffix = header_text[index+1:]
header_suffix=header_suffix.strip()
header_prefix = header_text[:index]
header_prefix=header_prefix.strip()


print(header_text)
print(header_suffix)
print(header_prefix)


master.selenium_close(driver)




