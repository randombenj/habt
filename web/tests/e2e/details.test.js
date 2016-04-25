var search = require('./lib/search.js');


describe('The package details page', function() {

  it('should display an error message when requesting a package that does not exist', function (){

    var package = 'asdfasdf';

    browser.get('http://localhost/#/detail/' + package);

    var message = element.all((by.repeater('alert in $root.alerts')));

    expect(message.count()).toEqual(1);
    expect(message.first().getText()).toMatch('Requested Package: "' + package + '" was not found on the Server.');
  });

  it('should display the "mono-csharp-shell" package', function () {

    var package = 'mono-csharp-shell';

    browser.get('http://localhost');

    // clear the search
    search.for(package);

    // click on the search result
    element.all(by.css(".container.search .list-group-item"))
      .first()
      .click();
    browser.waitForAngular();

    expect(browser.getCurrentUrl()).toMatch("http://localhost/#/detail/" + package);

    // check if the correct package is displayed
    var heading = element.all(by.css('h1')).first();
    var small = heading.all(by.css('small')).getText();

    // trick: https://www.reddit.com/r/learnpython/comments/2srdff/how_to_get_text_from_an_exact_html_element_using/
    heading.getText(function(headingText) {
      small.getText().then(function(smallText) {
        expect(headingText.replace(smallText, '')).toBe(package);
      });
    });
  });

});


describe('The "mono-csharp-shell" details page', function () {

  browser.get('http://localhost/#/detail/mono-csharp-shell');
  browser.waitForAngular();

  it('should show that "mono-csharp-shell" is referenced by "mono-complete" and "mono-devel"', function () {

    var expected = [
      {name: 'mono-complete', version: '(4.2.3.4-0xamarin2)'},
      {name: 'mono-devel', version: '(4.2.3.4-0xamarin2)'}
    ];

    var referencedBy = element.all(by.repeater('referenced in package.referenced_by'));
    expect(referencedBy.count()).toEqual(expected.length);

    for (var i = 0; i < referencedBy.length; i++) {
      // check for correct link
      expect(referencedBy[i].all(by.css('b > a')).getAttribute('href'))
        .toMatch('http://localhost/#/detail/' + expected[i].name);

      // check for the correct package in the correct order
      expect(referencedBy[i].all(by.css('b > a')).getText())
        .toMatch(expected[i].name);
    }
  });

  it('should show a title and a description', function () {

    var callout = element.all(by.css('.bs-callout'));
    expect(callout.count()).toEqual(1);

    // check the title and description
    expect(callout.all(by.css('h4')).getText())
      .toMatch('interactive C# shell');

    // check the description (empty)
    expect(callout.all(by.css('p.paragraph-text')).getText())
      .not.toBe('');
  });

  it('should show a maintainer and a link to the sourcecode', function () {

    var callout = element.all(by.css('.bs-callout'));

    // Check the maintainer
    expect(callout.all(by.css('div.key-value')).first().getText())
      .toMatch('Debian Mono Group <pkg-mono-group@lists.alioth.debian.org>');

    var sourcecode = callout.all(by.css('div.key-value')).get(1).all(by.css('a')).first();
    var sourcecodeLink = 'http://git.debian.org/?p=pkg-mono/packages/mono.git';

    // check the sourcecode link
    expect(sourcecode.getText()).toEqual(sourcecodeLink);
    expect(sourcecode.getAttribute('href')).toEqual(sourcecodeLink);
  });

  it('should show the distribution/part and architecture', function () {

    var installtargets = element.all(by.repeater('target in version.installtargets'));
    var distributionPart = installtargets.all(by.css('.panel-body  div.key-value a')).first();

    // check the distribution and part
    expect(distributionPart.getText()).toMatch('wheezy/main');
    expect(distributionPart.getAttribute('href'))
      .toMatch('http://download.mono-project.com/repo/debian/dists/wheezy/main');

    // check the architecture
    expect(installtargets.all(by.css('.panel-body  div.key-value .tag')).first().getText())
      .toMatch('armhf');
  });

  it('should show the correct dependencies in correct order', function () {

    var dependencies = element.all(by.repeater('section in version.dependencies')).first()
      .all(by.repeater('dependency in section.dependencies'));

    expect(dependencies.count()).toEqual(6);
  });
});


describe('The "libmono-addins-gui-cil-dev" details page', function () {

  it('should find the correct versions in the correct order', function () {

    var package = 'libmono-addins-gui-cil-dev';
    var expected = ['1.1-0xamarin1'];

    browser.get('http://localhost/#/detail/' + package);

    var versions = element.all(by.repeater('packageVersion in package.versions'));

    expect(versions.count()).toEqual(expect.length);

    for (var i = 0; i < versions.length; i++) {
      expect(versions[i].all(by.css('b')).getText()).toMatch(expected[i]);
    }

  });
});
