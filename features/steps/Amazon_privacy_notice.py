from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then


privacy_notice = (By.CSS_SELECTOR, "a[href='https://www.amazon.com/privacy']")

@given("Open Amazon T&C page")
def open_amazon_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')


@when("Store original windows")
def store_window(context):
    context.original_window = context.driver.current_window_handle
    print(context.original_window)

@when("Click on Amazon Privacy Notice link")
def click_privacy_notice(context):
    context.driver.find_element(*privacy_notice).click()


@when("Switch to the newly opened window")
def new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    windows = context.driver.window_handles
    print('\nAll window:', windows)
    context.driver.switch_to.window(windows[1])


@then("Verify Amazon Privacy Notice page is opened")
def privacy_page_opened(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/help/customer/display'))


@then("User can close new window")
def close_window(context):
    context.driver.close()


@then("Switch back to original")
def switch_original_window(context):
    context.driver.switch_to.window(context.original_window)




