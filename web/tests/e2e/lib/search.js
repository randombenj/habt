
/**
 * Search module api
 * @type {Object}
 */
module.exports = {
  for: searchFor,
  clear: clearSearch
};

/**
 * Text the next search result
 * @param  {Object} result
 *  Actual result
 * @param  {Object} expected
 *  Expected search result
 */
function testNextResult(result, expected) {

  var versions = result.all(by.css(".tag.label.label-default:not(.ng-hide)"));

  // check if the correct package in the correct order is found
  expect(result.element(by.css('b')).getText()).toBe(expected.name);
  expect(versions.count()).toBe(expected.version.length);

  // check if the versions match and are in the correct order
  for (var i = 0; i < versions.length; i++) {
    expect(versions[i].getText()).toMatch(expected.version[i]);
  }
}

/**
 * Tests for the expected results of a previous search
 * @param  {Array} expectedResults
 *  The results to check for
 */
function expectResults(expectedResults) {

  var searchResults = element.all(by.css(".container.search .list-group-item"));

  expect(searchResults.count()).toEqual(expectedResults.length);

  searchResults.then(function (results) {
    for (var i = 0; i < results.length; i++) {
      testNextResult(results[i], expectedResults[i]);
    }
  });
}

/**
 * Search for a search query in the search bar
 * @param  {String} query
 *  The query to search for
 */
function searchFor(query) {
  // enter search query
  element(by.id("package-search")).click();
  element(by.id("package-search")).sendKeys(query);

  // fluent interface
  return {
    expect: expectResults
  };
}

/**
 * Clear the search query
 */
function clearSearch(query) {
  // enter search query
  element(by.id("package-search")).clear();

  // fluent interface
  return {
    expect: expectResults
  };
}
