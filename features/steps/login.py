from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('the user is on login page')
def step_user_on_login_page(context):
    context.driver = webdriver.Chrome()
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


@then('the user is redirected to the home page')
def step_user_redirected_to_homepage(context):
    assert context.driver.current_url == 'https://www.saucedemo.com/inventory.html'


@then('error message "{message}" is displayed')
def step_user_error(context, message):
    error_text = context.driver.find_element(By.CSS_SELECTOR, '.error-message-container.error').text
    assert message in error_text
