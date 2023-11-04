from time import sleep
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest

from Examples.ImageAnalyze.ImageGogglePages.GoogleMain import GoogleMain





def test_start(selenium_init):
    main_page = selenium_init
    main_page.searchForPattern("cat")
    print ("gfgfgf")




