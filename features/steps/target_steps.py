from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep




@given('Open target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')

@when('Search for a product')
def search_product(context):
    context.driver.find_element(By.XPATH, '//*[@id="product-search"]').click()


@when('Click on cart icon')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="@web/CartLink"]').click()

@then ('Verify Cart Empty message shown')
def verify_cart_empty(context):
    expected_text = 'Your cart is empty'
    actual_text = context.driver.find_element(By.CSS_SELECTOR, '[data-test="boxEmptyMsg"] h1').text
    assert expected_text == actual_text, f'{expected_text} did not match actual {actual_text}'
