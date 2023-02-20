from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
service = Service("/Users/shailakshigupta/Desktop/Automation/python-selenium-automation/chromedriver")
driver = webdriver.Chrome(service=service)



@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when('Click on Returns & Orders')
def click_returns_orders(context):
    context.driver.find_element(By.XPATH,"//a[@href='/gp/css/order-history?ref_=nav_orders_first']").click()


@then('Verify Amazon logo is shown')
def logo(context):
    context.driver.find_element(By.XPATH,"//i[@aria-label='Amazon']")


@then('Verify Sign in header is visible')
def sign_in_header(context):
    expected_result = 'Sign in'
    actual_result = context.driver.find_element(By.XPATH,"//h1[@class='a-spacing-small']").text
    assert expected_result == actual_result, f'Expected {expected_result} but got this as Actual_result {actual_result}'

@then('Verify email input field is present')
def input_field(context):
     context.driver.find_element(By.ID,'ap_email')


@when('Click on cart button')
def cart_button(context):
    context.driver.find_element(By.ID,'nav-cart').click()


@then('Verify Amazon cart is empty')
def cart_empty(context):
    expected_result = 'Your Amazon Cart is empty'
    actual_result = context.driver.find_element(By.XPATH,"//div[@class='a-row sc-your-amazon-cart-is-empty']").text
    assert expected_result == actual_result, f'Expected_result {expected_result}but got this as Actual_result {actual_result}'


@when('Input text teddy')
def input_text(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('teddy')


@when('Click on search button')
def click_search(context):
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()


@when('Click on add to cart')
def add_cart(context): \
        context.driver.find_element(By.ID, 'add-to-cart-button').click()

@when('Click on first item')
def first_item(context):
    context.driver.find_element(By.XPATH,"//div[@data-component-id='17']").click()


@then('Verify no.of items in the cart')
def no_of_items(context):
    #expected_result = 'Subtotal (1 item)'
   context.driver.find_element(By.XPATH,"//span[@class='a-button-text a-declarative']")
   # assert expected_result == actual_result, f'Expected_result {expected_result} but got this as Actual_result {actual_result}'








