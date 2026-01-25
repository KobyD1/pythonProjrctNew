

class TestEbay:

    def test_ebay_advanced(self,setup_playwright):

        page = setup_playwright
        page.goto("https://www.ebay.com/")
        adv= page.get_by_role("link", name= "Advanced")
        adv.click()
        assert page.title() == "Advanced Search | eBay"
        assert page.url == "https://www.ebay.com/sch/ebayadvsearch","Page URL is not correct after click on Adv. button"