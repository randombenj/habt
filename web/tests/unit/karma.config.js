
/**
 * Karma configuration
 * @param  {Object}
 *  Injected Karma configuration
 */
module.exports = function( config ) {

  // configure the runner
  config.set({

    // set the base path (angular app root)
    basePath: '../../',

    // run the tests only once
    singleRun: true,

    // files to load (frameworks, application, tests)
    files: [

      // application dependencies
      'assets/lib/jquery/dist/jquery.js',
      'assets/lib/angular/angular.js',
      'assets/lib/angular-route/angular-route.js',
      'assets/lib/clipboard/dist/clipboard.js',
      'assets/lib/ngclipboard/dist/ngclipboard.js',

      // angular mock (fake dependency injection)
      'node_modules/angular-mocks/angular-mocks.js',

      // json mocks
      'node_modules/jasmine-jquery/lib/jasmine-jquery.js',
      {
        pattern: 'tests/mock/*.json',
        watched: true,
        served: true,
        included: false
      },

      // angular application
      'app/**/*.js',

      // angular tests
      'tests/unit/*.test.js'
    ],

    // use jasmine as testing framework
    frameworks: ['jasmine'],

    // test in the chrome browser
    browsers: ['Chrome'],

    // load the required plugins
    plugins : [
      'karma-jasmine-html-reporter',
      'karma-chrome-launcher',
      'karma-coverage',
      'karma-jasmine',
    ],

    // coverage reporter generates the coverage
    reporters: ['coverage', 'kjhtml'],

    preprocessors: {

      // source files, to generate coverage for
      'app/**/*.js': ['coverage']
    },

    // optionally, configure the reporter
    coverageReporter: {

      // generate html coverage report
      type : 'html',
      dir : 'tests/unit/.coverage/'
    }
  });
};
