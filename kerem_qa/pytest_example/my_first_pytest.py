import unittest

from Examples.PythonCharm.Python.PythonTraining.IntegerTest import result


class myFirstPytest(unittest.TestCase):

    def setUp(self):
        print ("into setup")
        self.num1= 2
        self.num2=3

    def tearDown(self):
        print ("into test end ")


    def test_summery(self):

        summery = self.num1 + self.num2


        assert summery==12,"our code did not suport summery "
        result=summery*2
        print (result)

    def test_multiple(self):

        multiple = self.num1 * self.num2
        assert multiple==28,"our code did not suport multiple "


