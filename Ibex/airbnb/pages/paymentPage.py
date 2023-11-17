import calendar
import time

from playwright.sync_api import expect
from datetime import datetime, timedelta

from retry import retry


class PaymentPage:
    def __init__(self, page):
        self.__page = page

    def get_and_assert_url(self, search_details: dict):
        self.__page.reload()
        url = self.__page.url
        adults_pattern = "adults=" + str(search_details["adults"])
        children_pattern = "children=" + str(search_details["children"])
        is_adults = adults_pattern in url
        is_children = children_pattern in url
        assert (is_adults, is_children) == (True, True), "Adults or Children amount failure found into reservation URL"
