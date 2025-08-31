from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver

class seleniumCommon():

    def selenium_start(self,url):
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        self.driver = driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get(url)
        return driver

    def selenium_end (self):
        self.driver.close()

    def click_and_send_keys(self,element , text):
        element.click()
        element.clear()
        element.send_keys(text)

        print ("test End")
