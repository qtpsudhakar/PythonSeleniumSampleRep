Feature: OrangeHRM Logo

Scenario: Logo Presence on Orange HRM Home Page
    Given launch chrome browser
    When open orange hrm homepage
    Then verify that the logo present on the page
    And close browser