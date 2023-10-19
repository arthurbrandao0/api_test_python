Feature: Weather API

  Scenario Outline: Verify Location Information
    Given the user wants to get current weather information
    When the user makes a request with latitude "<latitude>" and longitude "<longitude>"
    Then the response should contain the location information
      | country   |
      | <country> |

    Examples:
      | latitude           | longitude          | region             | country        |
      | -22.49994629161425 | -44.12550426202531 | 1                  | Brazil         |
      | 53.1               | -0.13              | -44.12550426202531 | United Kingdom |
