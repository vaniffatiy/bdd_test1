Feature: testing Google searching

  Scenario Outline: run 1 simple test of searching function on Google
    Given I have set the webbrowser settings to Chrome webdriver
    And I am on the main page
    When I type in <search_query> in Google input field
    And click Enter key
    Then I see the weather reports

    Examples:

      | search_query         |
      | weather today  |
      | weather tomorrow   |
      | weather in Minsk |
