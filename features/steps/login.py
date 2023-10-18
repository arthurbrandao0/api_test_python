from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


@given('the user is on login page')
def step_user_on_login_page(context):
    context.driver.get('https://www.saucedemo.com/')


@when('the user enter the username "{username}" and the password "{password}"')
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
    login_button = context.driver.find_element(By.ID, 'react-burger-menu-btn')
    login_button.click()


@when('the user clicks the logout button')
def step_user_clicks_logout_button(context):
    login_button = WebDriverWait(context.driver, 5).until(
        ec.element_to_be_clickable((By.ID, 'logout_sidebar_link'))
    )
    login_button.click()


@then('the user is redirected to the inventory page')
def step_user_redirected_to_inventory_page(context):
    assert context.driver.current_url == 'https://www.saucedemo.com/inventory.html'


@then('the user is redirected to the home page')
def step_user_redirected_to_homepage(context):
    assert context.driver.current_url == 'https://www.saucedemo.com/'


@then('error message "{message}" is displayed')
def step_user_error_message_displayed(context, message):
    error_text = context.driver.find_element(By.CSS_SELECTOR, '.error-message-container.error').text
    assert message in error_text
