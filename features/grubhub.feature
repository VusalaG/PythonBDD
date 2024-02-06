Feature: GrubHub Logo

  Scenario: Logo presence on Grubhub home page
    Given launch safari browser
    When open grubhub home page
    Then verify that logo presence on the page
    And close browser