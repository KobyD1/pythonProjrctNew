class utils():


    def get_avg(self,num1,num2):
        print (f"find the avg between 2 numbers:{num1} {num2}")
        summery = num1 + num2
        avg = summery/2
        print (f"Avg found the value is {avg} ")
        return avg

    def add_vat_to_price(self,price):
        print ("calculate VAT to price")
        price=price.replace("$","")
        price_as_int = int(price)
        final_price = price_as_int*1.18
        print (final_price)
