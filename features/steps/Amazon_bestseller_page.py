from selenium.webdriver.common.by import By
from behave import given, when, then

""""
@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')
"""
@when('Click on Bestseller tab')
def bestseller_tab(context):
    context.driver.find_element(By.XPATH,"//a[@data-csa-c-content-id='nav_cs_bestsellers']").click()

@then('Verify Bestseller is present')
def verify_bestseller(context):
    element = context.driver.find_element(By.XPATH,"//a[@data-csa-c-content-id='nav_cs_bestsellers']")
    print(element)


@then('Verify Bestseller has five links')
def links(context):
    links_count = context.driver.find_elements(By.CSS_SELECTOR,"div#zg_header a[href*='/ref=zg_bs_tab']")
    print(links_count)

    assert len(links_count) == 5, f'Expected 5 links, but got {len(links_count)}'

