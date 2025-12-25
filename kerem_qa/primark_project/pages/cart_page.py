from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self,driver):
        self.driver = driver

    def get_cart_message(self):
        text = self.driver.find_element(By.CSS_SELECTOR,"h4[data-testautomation-id='title']").text
        print (text)
        return text