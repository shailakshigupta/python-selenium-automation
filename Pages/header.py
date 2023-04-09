from selenium.webdriver.common.by import By
from Pages.base_page import Page


class Header(Page):
    AMAZON_SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    Returns_orders = (By.XPATH, "//a[@href='/gp/css/order-history?ref_=nav_orders_first']")

    def input_search_text(self, text):
        self.input_text(text, *self.AMAZON_SEARCH_FIELD)

    def click_search(self):
        self.click(*self.SEARCH_ICON)

    def click_returns_orders(self):
        #self.driver.find_element(*self.Returns_orders).click()
         self.click(*self.Returns_orders )

