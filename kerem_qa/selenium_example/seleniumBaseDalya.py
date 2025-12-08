
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver

class seleniumBaseDalya():

    def selenium_start(self):
        print("**** Test start ****")
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.maximize_window()
        driver.implicitly_wait(10)
        return driver