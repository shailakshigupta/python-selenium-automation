from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


color_options = (By.CSS_SELECTOR, "#variation_color_name li")
current_color = (By.CSS_SELECTOR, "#variation_color_name .selection")


@given('Open Amazon Product B07BJKRR25 Page')
def open_product(context):
    context.driver.get('https://www.amazon.com/gp/product/B07BJKRR25/')


@then('Verify user can select colors')
def select_colors(context):
    context.driver.find_element(*color_options).click()

    all_colors = context.driver.find_elements(*color_options)
    print('All colors', all_colors)
    expected_color = ["Black", "Blue, Over Dye", "Bright White", "Dark Blue Vintage", "Dark Indigo/Rinsed", "Dark Khaki Brown", "Dark Wash", "Indigo Wash", "Light Blue Vintage", "Light Khaki Brown", "Light Wash", "Medium Blue, Vintage", "Medium Wash", "Olive", "Rinsed", "Sage Green", "Vintage Wash", "Washed Black", "Washed Grey" ]

    actual_colors = []
    for color in all_colors:
        color.click()
        CURRENT_COLORS = context.driver.find_element(*current_color).text
        print('current color: ', CURRENT_COLORS)

    assert expected_color == actual_colors, f"Expected{expected_color}, but got {actual_colors}"


