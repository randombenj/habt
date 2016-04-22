module.exports = {
  for: searchFor,
  clear: clearSearch
};

/**
 * Tests if the expected version matches the given one
 * @param  {String} version
 *  Actual version
 * @param  {String} expectedVersion
 *  Expected version
 */
function testNextVersionResult(version, expectedVersion) {
  // check if the correct package in the correct order is found
  expect(version.getText()).toBe(expectedVersion);
}

/**
 * Text the next search result
 * @param  {Object} result
 *  Actual result
 * @param  {Object} expected
 *  Expected search result
 */
function testNextResult(result, expected) {
  var name = result.element(by.css('b')).getText();

  // check if the correct package in the correct order is found
  expect(name).toBe(expected.name);

  // check versions
  result.all(by.css(".tag.label.label-default:not(.ng-hide)")).then(function (tags) {
    expect(tags.length).toBe(expected.version.length);

    for (var i = 0; i < tags.length; i++) {
      testNextVersionResult(tags[i], expected.version[i]);
    }

  });
}

/**
 * Tests for the expected results of a previous search
 * @param  {Array} expectedResults
 *  The results to check for
 */
function expectResults(expectedResults) {

  function getTestCallback(results) {
    expect(results.length).toBe(expectedResults.length);
    for (var i = 0; i < results.length; i++) {
      testNextResult(results[i], expectedResults[i]);
    }
  }

  element.all( by.css(".container.search .list-group-item"))
    .then(getTestCallback);
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
