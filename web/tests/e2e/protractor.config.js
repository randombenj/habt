var SpecReporter = require('jasmine-spec-reporter');

/**
 * The protractor test engine config
 * @type {Object}
 */
exports.config = {

  // use jasmine as testing framework
  framework: 'jasmine2',

  // bind to the running browser
  seleniumAddress: 'http://localhost:4444/wd/hub',

  // tests to execute
  specs: [
    'search.test.js',
    'details.test.js'
  ],

  // test it in firefox and chrome
  multiCapabilities: [
    {'browserName': 'chrome'},
    {'browserName': 'firefox'}
  ],

  jasmineNodeOpts: {
    print: function() {}
  },

  onPrepare: function() {
    // Add spec reporter for beautiful output:
    jasmine.getEnv().addReporter(new SpecReporter({displayStacktrace: 'all'}));
  }
};
