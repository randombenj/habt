var search = require('./lib/search.js');


describe('The package search', function() {

  it('should find expected results when searching for "cli"', function() {

    // to to the search page (index)
    browser.get('http://localhost');

    // check for the expected search results
    search.for("cli").expect([
      {name: 'cli-common', version: ['0.9~xamarin1']},
      {name: 'cli-common-dev', version: ['0.9~xamarin1']},
      {name: 'cli-runtime', version: []},
      {name: 'cli-virtual-machine', version: []},
      {name: 'libmono-system-data-services-client4.0-cil', version: ['4.2.3.4-0xamarin2']}
    ]);
  });

  it('should clear the shown results when clearing the search input', function () {

    // clear the search and expect no results
    search.clear().expect([]);
  });

  it('should not find any results for "asdfasdf"', function() {

    // to to the search page (index)
    browser.get('http://localhost');

    // enter search query to find no results
    search.for("asdfasdf").expect([]);

  });

  it('should not find  the c# 2.0, 3.0, 4.0 and 4.5 compiler for "c-sharp-[0-9]\.[0\|5]-compiler"', function() {

    // to to the search page (index)
    browser.get('http://localhost');

    // test for the expected c# compilers
    search.for("c-sharp-[0-9]\.[0|5]-compiler").expect([
      {name: 'c-sharp-2.0-compiler', version: []},
      {name: 'c-sharp-3.0-compiler', version: []},
      {name: 'c-sharp-4.0-compiler', version: []},
      {name: 'c-sharp-4.5-compiler', version: []}
    ]);

  });
});
