Feature: Cart tests

  Scenario: User can see cart empty message
    Given Open target main page
    When Click on cart icon
    Then Verify Cart Empty message shown