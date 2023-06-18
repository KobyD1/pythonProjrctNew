import time

from playwright.sync_api import Page, expect


class WelcomePage():

    def __init__(self, page: Page):
        self.page = page
        self.category_css = "div.mybackground.full-height.style-img.fullWidth"

    def click_on_category(self, category_index: int):
        time.sleep(5)
        categories = self.page.query_selector_all(self.category_css)
        categories[category_index].click()
