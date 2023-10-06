Feature: Login in Swab Labs

  Scenario: Successfull login
    Given the user is on login page
    When the user enter the username "standard_user" and the password "secret_sauce"
    And the user clicks the login button
    Then the user is redirected to the inventory page

  Scenario: Successfull logout
    Given the user is on login page
    When the user enter the username "standard_user" and the password "secret_sauce"
    And the user clicks the login button
    Then the user is redirected to the inventory page
    When the user clicks the menu button
    And the user clicks the logout button
    Then the user is redirected to the home page



  Scenario: Invalid login with wrong password
    Given the user is on login page
    When the user enter the username "standard_user" and the password "1"
    And the user clicks the login button
    Then error message "Epic sadface: Username and password do not match any user in this service" is displayed


