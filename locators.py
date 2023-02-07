""""
#2. Practice with locators.
Create locators + search strategy for these page elements of Amazon Sign in page:

#Amazon logo:
driver.find_element(By.XPATH,"//i[@aria-label='Amazon']")

#Email Field:
driver.find_element(By.ID, 'ap_email')

#Continue Button:
driver.find_element(By.ID, "continue")
 # or
driver.find_element(By.XPATH,"//input[@type='submit']")

#Need help link:
driver.find_element(By.XPATH,"//span[@class='a-expander-prompt']")

#Forgot your password link:
driver.find_element(By.ID,'auth-fpp-link-bottom']")

#Other issues with Sign-In link:
driver.find_element(By.ID,"ap-other-signin-issues-link")

#Create your Amazon account button
driver.find_element(By.ID,"createAccountSubmit")

#Conditions of use link: Tried multiple ways but could not able to find unique attribute
driver.find_element(By.XPATH,"//a[@class='a-link-normal' and @target='_blank' and @rel='noopener']")
driver.find_element(By.XPATH,"//a[@class='a-link-normal' and @target='_blank']")
driver.find_element(By.XPATH,"//a[@class='a-link-normal' and @rel='noopener']")

#Privacy Notice link: Same Issue with this as above
driver.find_element(By.XPATH,"//a[@class='a-link-normal' and @target='_blank']")
"""

#3. Create a test case for the Sign In page using python & selenium script.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep
#driver = webdriver.Chrome(executable_path="/Users/shailakshigupta/Desktop/Automation/python-selenium-automation/chromedriver")

service = Service("/Users/shailakshigupta/Desktop/Automation/python-selenium-automation/chromedriver")
driver = webdriver.Chrome(service=service)
driver.get("https://www.amazon.com")

driver.find_element(By.ID, "nav-orders").click()
sleep(5)
expected_result = "Email or mobile phone number"
actual_result = driver.find_element(By.XPATH, "//label[@class='a-form-label']").text
print (actual_result)
assert expected_result == actual_result, f'Expected(expected_result) is not same as Actual(actual_result)'
print("Test Case Passed")


