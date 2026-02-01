# Created by aaronwalden at 1/21/26
#
 Feature: Cart functionality

  Scenario: User can add product to cart
   Given Open Target main page
   When user adds a product to cart
   Then cart contains at least one item

  Scenario: Your cart is empty message is shown
   Given Open Target main page
   When user clicks on cart icon
   Then user sees empty cart message