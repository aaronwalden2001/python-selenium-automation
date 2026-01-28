Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open Google page
    When Input Car into search field
    And Click on search icon
    Then Product results for Car are shown



  Scenario: User can search for a product1
    Given Open Google page
    When Input tree into search field
    And Click on search icon
    Then Product results for tree are shown

  Scenario: User can search for a product with a variable
    Given user opens Target homepage
    When user searches for "laptop"
    Then search results are displayed
