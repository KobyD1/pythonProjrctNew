import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from SeleniumExam.Google.Pages.WelcomePage import WelcomePage
from SeleniumExam.Google.SearchlTests.Base import Base


@pytest.fixture(scope="class")   # scope describe how often it will run (class ,function ....)
def setup(request):
    print("initiating chrome driver")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(Base.url)
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver

    yield driver
    driver.close()


@pytest.mark.usefixtures("setup")
class TestGoogle(Base):
    def test_search_dog(self):
        welcome = WelcomePage(self.driver)
        welcome.search_for_pattern("dog")
        print('Test Completed')


    def test_search_cat(self):
        welcome = WelcomePage(self.driver)
        welcome.search_for_pattern("cat")
        print('Test Completed')

