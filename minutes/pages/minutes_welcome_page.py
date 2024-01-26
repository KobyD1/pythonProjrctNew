class welcomePage():

    def __init__(self, page):
        self.__page = page
        self.page = page
        self.__news = self.__page.locator("[href='/categories/football-news']")
        self.__transfer = self.__page.locator("[href='/categories/transfer']")
        self.__premier = self.__page.get_by_text("Premier")


    def verify_for_news(self,exp_text):
        print ("Start testing for up menu-news button")
        text  = self.__news.text_content()
        assert exp_text == text ,"News up pannel button is not appears as expectrd "


    def verify_for_transfer(self,exp_text):
        print ("Start testing for transfer -up menu")
        text  = self.__transfer.text_content()
        assert exp_text == text ,"Transfer up pannel button is not appears as expectrd "

    def verify_for_premier(self,exp_text):
        print ("Start testing for Primier Leage up menu")
        text  = self.__premier.text_content()
        assert exp_text == text
        # mm-root > header > div.headerFirstRow_ednzzn > div.subMenuWrapper_tkhkkr > div._hi77gs