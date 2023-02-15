# Created by shailakshigupta at 2/13/23
Feature: Test scenario for sign in when clicking returns and orders


  Scenario: User can open Amazon
    Given Open Amazon page
    When Click on Returns & Orders
    Then Verify Amazon logo is shown

  Scenario: User can be landed on sign in page
    Given Open Amazon page
    When Click on Returns & Orders
    Then Verify Sign in header is visible

  Scenario: User can access sign in page
    Given Open Amazon page
    When Click on Returns & Orders
    Then Verify email input field is present

  Scenario: User can view cart as empty
    Given Open Amazon page
    When Click on cart button
    Then Verify Amazon cart is empty


  Scenario: User can search for an item
    Given Open Amazon page
    When Input text teddy
    When Click on search button
    When Click on first item
    When Click on add to cart
    When Click on cart button
    Then Verify no.of items in the cart

