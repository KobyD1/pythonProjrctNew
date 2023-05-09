from selenium.webdriver import Keys

from xyte.LawnMowers.Pages.locators import WelcomePageLocators


class WelcomeNTPage(object):


    def __init__(self, driver):
        self.driver = driver


# method for clicking over any link into side menu
    def search_for_pattern(self,user_pattern):
        search = self.driver.find_element(*WelcomePageLocators.SEARCH_MENU)

        search.click()
        search.clear()
        search.send_keys(user_pattern)
        search.send_keys(Keys.ENTER)


