var search = require('./lib/search.js');

describe('The package search', function() {

  it('should find correct results when searching for "lib"', function() {

    browser.get('http://localhost');

    search.for("lib").expect([
      {name: 'libc6', version: []},
      {name: 'libc6-dev', version: []},
      {name: 'libdb3-dev',version: []},
      {name: 'libncurses-dev', version: []},
      {name: 'libpam0g', version: []},
      {name: 'libskynet', version: ['0.1.11']},
    ]);

    // clear the search
    search.clear().expect([]);
  });

  it('should not find any results for "asdfasdf"', function() {

    browser.get('http://localhost');

    // enter search query
    search.for("asdfasdf").expect([]);

  });

  it('should not find  pycsmbuilder for "p.*u.*der"', function() {

    browser.get('http://localhost');
    // enter search query
    search.for("p.*u.*der").expect([{
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
