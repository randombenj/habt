describe('The package search', function() {

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

  function searchFor(query) {
    // enter search query
    element(by.id("package-search")).click();
    element(by.id("package-search")).sendKeys(query);

    // fluent interface
    return {
      expect: expectResults
    };
  }

  function clearSearch(query) {
    // enter search query
    element(by.id("package-search")).clear();

    // fluent interface
    return {
      expect: expectResults
    };
  }


  it('should find correct results when searching for "lib"', function() {

    browser.get('http://localhost');

    searchFor("lib").expect([
      {name: 'libc6', version: []},
      {name: 'libc6-dev', version: []},
      {name: 'libdb3-dev',version: []},
      {name: 'libncurses-dev', version: []},
      {name: 'libpam0g', version: []},
      {name: 'libskynet', version: ['0.1.11']},
    ]);

    // clear the search
    clearSearch().expect([]);
  });

  it('should not find any results for "asdfasdf"', function() {

    browser.get('http://localhost');

    // enter search query
    searchFor("asdfasdf").expect([]);

  });

  it('should not find  pycsmbuilder for "p.*u.*der"', function() {

    browser.get('http://localhost');
    // enter search query
    searchFor("p.*u.*der").expect([{
      name: 'pycsmbuilder',
      version: [
        '1.1.0+deb8u3',
        '1.1.0+deb8u2',
        '1.1.0+deb8u1',
        '1.1.0',
        '1.0.0'
      ]
    }]);

  });
});
