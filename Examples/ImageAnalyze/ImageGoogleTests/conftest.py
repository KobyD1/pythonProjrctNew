import pytest
from _pytest.fixtures import fixture
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Examples.ImageAnalyze.ImageGogglePages.GoogleMain import GoogleMain


@pytest.fixture
def setup_selenium():
    print("initiating chrome driver")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get(globals.URL)
    driver.maximize_window()
    sleep(3)
    main_page = GoogleMain(driver)
    yield driver
    driver.close()
    pass
