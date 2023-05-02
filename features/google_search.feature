Feature: testing Google searching

  Scenario: run 1 simple test of searching function on Google
     Given we have set the webbrowser settings to Chrome webdriver
      When we type in a request for the weather in Google input field
      Then it shows the current weather in the region
