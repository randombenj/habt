@regression
Feature: Test the functionality of the Importer
  In order to be shure the correct data is served
  from the api, the Importer has to be tested

  @good_case
  Scenario: Run an import
    Given The database is set up and clean
    When I run an import for sources.list
    Then I expect there top be packages in the database
