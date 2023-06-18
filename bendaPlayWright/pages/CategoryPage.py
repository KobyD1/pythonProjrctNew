import time

from playwright.sync_api import Page, expect


class CategoryPage():

    def __init__(self, page: Page):
        self.page = page
        self.product_css = "div.mybackground.full-height"
        self.more_css = "div.tabs-body > div:nth-child(1) > ion-button"
        self.close_css = "item > app-header > ion-toolbar > ion-buttons > ion-button"

    def get_products_amount(self) -> int:
        products = self.page.query_selector_all(self.product_css)
        print(f'\n{len(products)} products found at tested page ')
        return len(products)

    def get_product_details(self):
        more = self.page.wait_for_selector(self.more_css)
        more.click()
        details = self.page.query_selector_all("li")
        for detail in details:
            print(detail.inner_text())

        close = self.page.wait_for_selector(self.close_css)
        close.click()

    def get_products_details(self, max_index:int):
        amount = self.get_products_amount()
        if max_index == 0:
            max_index = amount
        for index in range(1, max_index):
            print (f'%%%%% find details for product#{index} %%%%%%%')
            icon = self.page.query_selector_all("div.flex-grid.big > div:nth-child(" + str(index) + ") > div")[0]
            icon.click()
            self.get_product_details()
