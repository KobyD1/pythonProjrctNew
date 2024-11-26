import pytest






@pytest.mark.usefixtures("setup_create")
class TestWeather():
    def test_get_current_tempature_by_zip(self,setup_create):
        driver,welcome_weather_page = setup_create

        welcome_weather_page.search_and_get_tempature_by_zip("20852")

        print ("Test end")


