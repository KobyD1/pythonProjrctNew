import unittest

from Examples.PythonCharm.Python.PythonTraining.IntegerTest import result


class myFirstPytest(unittest.TestCase):

    def test_summery(self):
        num1 = 3
        num2 = 9
        summery = num1 + num2


        assert summery==12,"our code did not suport summery "
        result=summery*2
        print (result)


