from time import sleep
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest

from Examples.ImageAnalyze.ImageGogglePages.GoogleMain import GoogleMain


@pytest.fixture(autouse=True)
def selenium_init():
    print("initiating chrome driver")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get('https://www.google.com/')
    sleep(3)
    main_page = GoogleMain(driver)
    yield main_page
    driver.close()