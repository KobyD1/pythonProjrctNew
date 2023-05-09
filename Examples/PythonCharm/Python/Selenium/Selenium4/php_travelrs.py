from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from PythonCharm.Python.Selenium.Selenium4.BaseSelenium import BaseSelenium

base_selenium = BaseSelenium()
driver = base_selenium.selenium_init("https://phptravels.net/")
prices=driver.find_elements(By.CLASS_NAME,"price__num")
total = 0
for price in prices:
    value = price.text
    if value.__contains__('USD'):
        value = value.replace('USD ','')
        value_as_int = int(value)
        if (value_as_int == 450):
            print ('450 USD found')
        total = total + value_as_int
print(total)

places=driver.find_elements(By.CLASS_NAME,"active_hotels.waves-effect")

for place in places:
    place_as_str = place.text
    print(place_as_str)


base_selenium.test_end()