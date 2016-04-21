Feature: Test the functionality of the PackageManager
  In order to enshure the functionality of the api
  the PackageManager has to work propperly


  # Search tests:

  @good_case
  @precondition(Migrator.Test.feature: Run a migration)
  Scenario: Serach for debian packages
    Given The api is ready
    When I search for lib
    Then I expect 6 packages to be found

  @good_case
  Scenario: Serach for debian package libskynet
    Given The api is ready
    When I search for lib
    Then I expect libskynet to be in the results list

  @bad_case
  Scenario: Serach for a package that does not exist
    Given The api is ready
    When I search for asdfasdf
    Then I expect 0 packages to be found


  # Package data tests:

  @good_case
  Scenario: Get the details of the libskynet package
    Given The api is ready
    When I request the libskynet package
    Then I expect the package libskynet

  @bad_case
  Scenario: Get the details of a nonexistent package
    Given The api is ready
    When I request the asdfasdf package
    Then I don't expect there to be any package

  @good_case
  Scenario: Get the version details of the libskynet version 0.1.11
    Given The api is ready
    When I request the version 0.1.11 of the libskynet package
    Then I expect the version 0.1.11 of the libskynet package
