@regression
Feature: Test the functionality of the Migrator
  In order to be shure the correct data is served
  from the api, the migrator has to be tested

  @good_case
  Scenario: Run a migration
    Given The database is set up and clean
    When I run a migration for sources.list
    Then I expect there top be packages in the database
