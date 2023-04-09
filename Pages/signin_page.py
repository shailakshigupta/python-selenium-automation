from selenium.webdriver.common.by import By
from Pages.base_page import Page

class Signin (Page):
    AMAZON_Signin = (By.XPATH,"//h1[@class='a-spacing-small']")


    def sign_in_header(self, expected_text):
        #expected_result = 'Sign in'
        actual_result = self.driver.find_element(*self.AMAZON_Signin).text
        assert expected_text == actual_result, f'Expected {expected_text} but got this as Actual_result {actual_result}'
