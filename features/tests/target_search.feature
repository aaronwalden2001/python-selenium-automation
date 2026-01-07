# Created by aaronwalden at 12/27/25
Feature: Tests for search,sign in, and cart function
  Scenario: User can search for a product on Target
    Given Open Target main page
    When Search for tea
    Then Search results for tea are shown
  # Enter feature description here

#Feature: Cart functionality

  Scenario: User sees empty cart message
    Given Open Target main page
    When user clicks on cart icon
    Then user sees cart empty message


#Feature: Sign In navigation

  Scenario: Logged out user can navigate to Sign In page
    Given Open Target main page
    When user clicks Sign In button
    And user clicks Sign In from side navigation
    Then Sign In form is displayed
