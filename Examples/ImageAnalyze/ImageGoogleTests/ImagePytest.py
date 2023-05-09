import unittest

from Examples.ImageAnalyze.ImageGoogleTests.BaseSelenium import BaseSelenium
from Examples.ImageAnalyze.Utils.ImagesUtils import ImagesUtils

# https://www.iloveimg.com/crop-image  - cropping site
class SeleniumPytest(unittest.TestCase,BaseSelenium):

    def setUp(self):
        print ('Test Start')
        base = BaseSelenium()
        driver = base.selenium_init("https://www.google.com")
        images_utils = ImagesUtils(driver,False)
        self.images_utils = images_utils
        self.base = base



    def test_image_compare_positive_test(self):

        path_ref_image = "../Images/Ref/Google/Logo1.png"

        # rectangle parameters :x, y, x+width, y+highet
        rectangle = {
            'x': 620,
            'y': 120,
            'x+width': 1030,
            'y+highet': 250
        }
        is_equals = self.images_utils.compare_image_rectangle(path_ref_image, rectangle, 'namePositive')
        self.base.selenium_end()
        assert is_equals == True , 'mismatch found at compare images '


    def test_image_compare_negative_test(self):

        path_ref_image = "../Images/Ref/Google/Error.png"

        # rectangle parameters :x, y, x+width, y+highet
        rectangle = {
            'x': 620,
            'y': 120,
            'x+width': 1030,
            'y+highet': 250
        }
        is_equals  = self.images_utils.compare_image_rectangle(path_ref_image, rectangle, 'nameNegative')
        self.base.selenium_end()
        assert is_equals == True , 'mismatch found at compare images '



    def test_image_compare_coardinations_test(self):

        path_ref_image = "../Images/Ref/Google/Logo1.png"

        # coardination parameters :x, y (left /down point)
        coardination = {
            'x': 620,
            'y': 120
        }
        is_equals = self.images_utils.compare_image_coardinations(path_ref_image, coardination, 'by coardination')
        self.base.selenium_end()
        assert is_equals == True , 'mismatch found at compare images'




