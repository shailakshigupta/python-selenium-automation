from selenium.webdriver.common.by import By
from Pages.base_page import Page


class Empty_cart(Page):
    amazon_cart = By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']"
    #amazon_cart = By.XPATH, "//div[@class='sc-your-amazon-cart-is-empty']//h2[contains(text(), 'Your Amazon Cart is empty')]"

    def cart_empty(self,expected_text):
        #expected_result = 'Your Amazon Cart is empty'
        actual_result = self.driver.find_element(*self.amazon_cart).text
        assert expected_text == actual_result, f'Expected_result {expected_text}but got this as Actual_result {actual_result}'