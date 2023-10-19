Feature: Weather API

  Scenario Outline: Verify Location Information
    Given the user wants to get current weather information
    When the user makes a request with latitude "<latitude>" and longitude "<longitude>"
    Then the response should contain the location information
      | country   | region   |
      | <country> | <region> |

    Examples:
      | latitude           | longitude          | region         | country        |
      | -22.49994629161425 | -44.12550426202531 | Rio de Janeiro | Brazil         |
      | 53.1               | -0.13              | Lincolnshire   | United Kingdom |
      | 37.983810          | 23.727539          | Attica         | Greece         |
