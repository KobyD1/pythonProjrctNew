



class TestPytestExample():

    def setup(self):
        print ("into setup ")
        self.num1 = 3
        self.num2=8



    def test_with_failure(self):
        print ("test start")

        print ("calculate complted ")
        assert self.num1+self.num2==12, " the summery of 6 and 2 is not 12  as expected"


    def test_multiple(self):

        assert self.num2*self.num1==15 , "the result of multiple is not 15 as expected"

    def test_add(self):
        num1= 3
        num2= 4
        sum = num1+num2

        assert sum==7 , "the summery of num1 and num2 is not 7 as expected "





