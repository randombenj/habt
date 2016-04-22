var search = require('./lib/search.js');

describe('The package details page', function() {

  var urlChanged = function(url) {
    return function () {
      return browser.getCurrentUrl().then(function(actualUrl) {
        return url != actualUrl;
      });
    };
  };

  it('should display the "libskynet" package', function() {

    browser.get('http://localhost');

    // clear the search
    search.for('libskynet');

    element.all(by.css(".container.search .list-group-item"))
      .first()
      .click();

    browser.wait(urlChanged("http://localhost:9000/#/detail/libskynet"), 1000);

    var heading = element.all(by.css('h1')).first();
    var small = heading.all(by.css('small')).getText();

    // trick: https://www.reddit.com/r/learnpython/comments/2srdff/how_to_get_text_from_an_exact_html_element_using/
    heading.getText(function(headingText) {
      small.getText().then(function(smallText) {
        expect(headingText.replace(smallText, '')).toBe('libskynet');
      });
    });
  });

  describe('The "libskynet" details page', function () {

    browser.get('http://localhost/#/detail/libskynet');

    it('should show that "libskynet" is referenced by "shuttle"', function () {

      var referencedBy = element.all(by.repeater('referenced in package.referenced_by'));

      expect(referencedBy.count()).toEqual(1);

      // check the package link
      expect(referencedBy.all(by.css('b > a')).getAttribute('href'))
        .toMatch('http://localhost/#/detail/shuttle');

      // check the package name which references this package
      expect(referencedBy.all(by.css('b > a')).getText())
        .toMatch('shuttle');
    });

    it('should show a title but no description', function () {

      var callout = element.all(by.css('.bs-callout'));

      expect(callout.count()).toEqual(1);

      // check the title and description
      expect(callout.all(by.css('h4')).getText())
        .toMatch('This is the skynet library package');

      // check the description (empty)
      expect(callout.all(by.css('p.paragraph-text')).getText())
        .toMatch('');
    });

    it('should show a maintainer but no link to the sourcecode', function () {

      var callout = element.all(by.css('.bs-callout'));

      // Check the maintainer
      expect(callout.all(by.css('div.key-value')).first().getText())
        .not.toBe('');

      // check the sourcecode link (empty)
      expect(callout.all(by.css('div.key-value')).get(1).getText())
        .toMatch('');
    });

    it('should show the distribution and architecture', function () {

      var installtargets = element.all(by.repeater('target in version.installtargets'));

      expect(installtargets.all(by.css('.panel-body  div.key-value .tag')).first().getText())
        .toMatch('amd64');
    });

    it('should show the correct dependencies', function () {

      var dependencies = element.all(by.repeater('section in version.dependencies')).first()
        .all(by.repeater('dependency in section.dependencies'));

      expect(dependencies.count()).toEqual(5);
    });

  });
});
