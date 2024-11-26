import pytest

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from weather.Pages.WelcomeWeaterPage import welcomeWeatherPage
from weather.Tests.globals import url


@pytest.fixture()
def setup_create(request):
    print ("Test start...")
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(10)
    welcome_weather_page = welcomeWeatherPage(driver)
    yield driver ,welcome_weather_page

    driver.close()
    print ("...Test end")

