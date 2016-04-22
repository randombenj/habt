var reporter = require('protractor-html-screenshot-reporter');

/**
 * The protractor test engine config
 * @type {Object}
 */
exports.config = {

  // use jasmine as testing framework
  framework: 'jasmine',

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

  onPrepare: function() {
      // Add a screenshot reporter and store screenshots to `/tmp/screnshots`:
      jasmine.getEnv().addReporter(new reporter({
         baseDirectory: '.coverage/'
      }));
   }
};
