
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
  specs: ['search.test.js']
};
