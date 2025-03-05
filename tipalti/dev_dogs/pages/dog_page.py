class dogPage():
    def __init__(self, page):
        self.page = page
        self.name_menu = self.page.locator("[id='name']")
        self.email_menu = self.page.locator("[id='email']")
        self.message_menu = self.page.locator("[id='message']")
        self.send_button = self.page.get_by_text("Send")

    def fill_message(self, message_prefix: str, dog_name: str):
        message_text = message_prefix + dog_name
        self.message_menu.fill(message_text)

    def fill_contant_details(self, name: str, email: str):
        self.name_menu.fill(name)
        self.email_menu.fill(email)

    def click_on_send(self):
        # there is no verify for the success of the send - it responsed with error
        self.send_button.click()
