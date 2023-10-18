from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


# Given
@given('the user is on the login page')
def step_user_on_login_page(context):
    context.driver.get('https://www.saucedemo.com/')


# When
@when('the user enters the username "{username}" and the password "{password}"')
def step_user_enters_credentials(context, username, password):
    username_field = context.driver.find_element(By.ID, 'user-name')
    password_field = context.driver.find_element(By.ID, 'password')

    username_field.send_keys(username)
    password_field.send_keys(password)


@when('the user clicks the login button')
def step_user_clicks_login_button(context):
    login_button = context.driver.find_element(By.ID, 'login-button')
    login_button.click()


@when('the user clicks the menu button')
def step_user_clicks_menu_button(context):
    menu_button = context.driver.find_element(By.ID, 'react-burger-menu-btn')
    menu_button.click()


@when('the user clicks the logout button')
def step_user_clicks_logout_button(context):
    logout_button = WebDriverWait(context.driver, 5).until(
        expected_conditions.element_to_be_clickable((By.ID, 'logout_sidebar_link'))
    )
    logout_button.click()


# Then
@then('the user is redirected to the inventory page')
def step_user_redirected_to_inventory_page(context):
    inventory_url = 'https://www.saucedemo.com/inventory.html'
    WebDriverWait(context.driver, 5).until(expected_conditions.url_to_be(inventory_url))


@then('the user is redirected to the home page')
def step_user_redirected_to_homepage(context):
    homepage_url = 'https://www.saucedemo.com/'
    WebDriverWait(context.driver, 5).until(expected_conditions.url_to_be(homepage_url))


@then('error message "{message}" is displayed')
def step_user_error_message_displayed(context, message):
    error_text = context.driver.find_element(By.CSS_SELECTOR, '.error-message-container.error').text
    assert message in error_text
