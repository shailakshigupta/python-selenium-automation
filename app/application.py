from Pages.main_page import MainPage
from Pages.header import Header
#from Pages.search_results_page import SearchResultsPage
from Pages.signin_page import Signin
from Pages.cart_page import Empty_cart


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.header = Header(self.driver)
        #self.search_results_page = SearchResultsPage(self.driver)
        self.signin_page = Signin (self.driver)
        self.cart_page = Empty_cart(self.driver)
