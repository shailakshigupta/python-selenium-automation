from selenium.webdriver.common.by import By
from behave import given, when, then

@given("Open Amazon New UI")
def open_new_UI(context):
    context.driver.get(' https://www.amazon.com/gp/help/customer/display.html')



@then("Verify Amazon UI elements")
def amazon_UI(context):
    UI_elements_count = context.driver.find_elements(By.CSS_SELECTOR, "div.page-container div.issue-card-wrapper")
    print(UI_elements_count)

    assert len(UI_elements_count) == 10 , f'Expected 10 links, but got {len(UI_elements_count)}'


@then("Verify help library")
def amazon_help_library(context):
    help_library_count = context.driver.find_elements(By.CSS_SELECTOR, "div.page-container h2")
    print(help_library_count)

    assert len(help_library_count) == 2, f'Expected 2 links, but got {len(help_library_count)}'


@then("verify help topics")
def amazon_help_topics(context):
    help_topics_count = context.driver.find_elements(By.CSS_SELECTOR, "li.help-topics")
    print(help_topics_count)

    assert len(help_topics_count) == 11 , f'Expected 11 links, but got {len(help_topics_count)}'
