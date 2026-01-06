# Created by aaronwalden at 12/27/25
Feature: Tests for search
  Scenario: User can search for a product on Target
    Given Open Target main page
    When Search for tea
    Then Search results for tea are shown
  # Enter feature description here

 Feature: Tests for Signin
  Scenario: User Sign into Target
    Given Open Target main page
    When Account button clicked
    Then Signin page shown