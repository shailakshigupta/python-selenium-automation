from selenium.webdriver.common.by import By
from Pages.base_page import Page


class MainPage(Page):
    cart = By.ID, 'nav-cart'
    def open_main_url(self):
        self.open_url('https://www.amazon.com/')

    def cart_button(self):
        self.click(*self.cart)