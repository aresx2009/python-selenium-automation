# Created by walterkieke at 10/6/24
Feature: Tests for Target Search functionality


  Scenario: User can search for a product
    Given Open target main page
    When Search for a product
    Then Verify thst correct search reqults shown

