import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver

from Selenium_fixtures.Pages.WelcomeBookingPage import welcomeBookingPage


@pytest.fixture()
def setup_create(request):
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.booking.com")
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield driver
    driver.close()


@pytest.mark.usefixtures("setup_create")
class TestCreateZone():
    def test_search_hotel(self):
        welcomePage = welcomeBookingPage(self.driver)
        welcomePage.close_pop_up()

        welcomePage.click_on_search_menu("London")

        print ("Test end")


