from selenium.webdriver.common.by import By

from haifa_qa.selenium_example.selenium_common import seleniumCommon

# 1.	Go to https://www.zara.com/il/en/
# 2.	Read the text from shopping bag
# 3.	Verify it contains 0
# 4. verify the Login button navigate to login page

common = seleniumCommon()

driver = common.selenium_start("https://www.zara.com/il/en/")
shopping = driver.find_element(By.PARTIAL_LINK_TEXT,"SHOPPING")
text_shopping = shopping.text
if (text_shopping.count("[0]")==1):
    print ("### shopping test pass###")


log_on_button = driver.find_element(By.PARTIAL_LINK_TEXT,"LOG")
log_on_button.click()
url = driver.current_url
print (f"URL value is {url}")
if not (url =="https://www.zara.com/il/en/logon"):
    print ("##### Test Failed")


common.selenium_end()
