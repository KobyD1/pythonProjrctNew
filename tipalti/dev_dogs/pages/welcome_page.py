class welcomePage():
    def __init__(self, page):
        self.page = page
        self.menu_button = self.page.query_selector_all("a[href='#menu']")[0]
        self.menu_item_1 = self.page.get_by_text("Home")
        self.menu_items = self.page.query_selector_all("a[href*='.html']")
        self.menu_item_2 = self.page.query_selector_all("a[href*=kika]")[0]
        self.menu_item_3 = self.page.query_selector_all("a[href*='lychee']")[0]
        self.menu_item_4 = self.page.query_selector_all("a[href*='kimba']")[0]

    def click_on_menu_button(self):
        self.menu_button.click()
        print("Menu button success to clicked")

    def get_and_assert_menu_items(self, exp_items: list):
        # done per each element   - I try by CSS a[href*=html] - it return 17 elements , not stable solution
        act_mneu_items_text = []

        menu_item_1_text = self.menu_item_1.text_content()
        act_mneu_items_text.append(menu_item_1_text)

        menu_item_2_text = self.prapare_menu_item(self.menu_item_2.text_content())
        act_mneu_items_text.append(menu_item_2_text)

        menu_item_3_text = self.prapare_menu_item(self.menu_item_3.text_content())
        act_mneu_items_text.append(menu_item_3_text)

        menu_item_4_text = self.prapare_menu_item(self.menu_item_4.text_content())
        act_mneu_items_text.append(menu_item_4_text)

        assert act_mneu_items_text == exp_items, "One or more menu item text is not as expected"

    def prapare_menu_item(self, menu_item: str) -> str:
        menu_item = menu_item.replace("\t", "")
        menu_item = menu_item.replace("\n", "")
        return menu_item

    def click_on_item_and_verify(self, pattern: str):
        icon = self.page.query_selector_all(f"a[href*={pattern}]")[0]
        icon.click()
        page_url = self.page.url
        assert pattern in page_url, " Page did not opened as expected at correct URL after click on Icon "
