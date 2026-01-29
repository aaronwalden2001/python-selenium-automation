# Created by aaronwalden at 1/29/26
Feature: Test color options
  Scenario: user can check color options
    Given Open Target main page
    When user selects each available color
    Then each selected color has been selected
    # Enter steps here