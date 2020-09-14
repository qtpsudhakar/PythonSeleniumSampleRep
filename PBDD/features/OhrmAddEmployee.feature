
Feature: Ohrm Add Employee
  @addemp @smoke
  Scenario: adding an employee
    Given sudhakar launch Chrome Browser
    And sudhakar navigated orangehrm url
    When sudhakar enter username and password
    And sudhakar click on Login button
    Then sudhakar should see welcome page