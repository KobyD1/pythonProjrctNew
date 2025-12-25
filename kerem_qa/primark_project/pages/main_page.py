from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self,driver):
        self.driver = driver


    def serach_for_item(self,item="Shoes"):
        self.driver.find_element(By.ID,"search-field").click()
        search = self.driver.find_element(By.ID,"search-field").click()

        search.clear()
        search.send_keys(item)

    def click_button_and_get_text (self,text):
        button  = self.driver.find_element(By.PARTIAL_LINK_TEXT,text)
        button_text = button.text
        button.click()
        return button_text





