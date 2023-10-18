Feature: Login in Swab Labs

  Scenario Outline: Successfull login
    Given the user is on the login page
    When the user enters the username "<username>" and the password "<password>"
    And the user clicks the login button
    Then the user is redirected to the inventory page

    Examples:
      | username                | password     |
      | standard_user           | secret_sauce |
      | problem_user            | secret_sauce |
      | performance_glitch_user | secret_sauce |

  Scenario: Successfull logout
    Given the user is on the login page
    When the user enters the username "standard_user" and the password "secret_sauce"
    And the user clicks the login button
    Then the user is redirected to the inventory page
    When the user clicks the menu button
    And the user clicks the logout button
    Then the user is redirected to the home page

  @test3
  Scenario: Invalid login with wrong password
    Given the user is on the login page
    When the user enters the username "standard_user" and the password "1"
    And the user clicks the login button
    Then error message "Epic sadface: Username and password do not match any user in this service" is displayed


  Scenario: Invalid login with blocked user
    Given the user is on the login page
    When the user enters the username "locked_out_user" and the password "secret_sauce"
    And the user clicks the login button
    Then error message "Epic sadface: Sorry, this user has been locked out." is displayed


