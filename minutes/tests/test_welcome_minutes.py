
import pytest

# to run in terminal playwright install at the first time

class Test_Welcome_Minutes():
    @pytest.mark.flaky(reruns=2)
    def test_news_button(self, setup_browser):
        page,welcome_page = setup_browser
        welcome_page.verify_for_news("News")

    def test_transfer_button(self, setup_browser):
        page,welcome_page = setup_browser
        welcome_page.verify_for_transfer("Transfer News")

    def test_premier_button(self, setup_browser):
        page,welcome_page = setup_browser
        welcome_page.verify_for_premier("Premier League")


