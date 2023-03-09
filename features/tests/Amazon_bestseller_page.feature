Feature: Amazon bestseller page test

  Scenario: User can see bestseller menu
    Given Open Amazon page
    Then Verify Bestseller is present

  Scenario: User can see five links in bestseller menu
    Given Open Amazon page
    When Click on Bestseller tab
    Then Verify Bestseller has five links


