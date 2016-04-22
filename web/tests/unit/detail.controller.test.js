
/**
 * Tests for the search controller
 */
describe( 'The Detail Controller', function () {

  // locals
  var $controller,
    $httpBackend,
    create,
    requestHandler,
    $rootScope;

  // angular 'webly' module
  beforeEach(module('webly'));

  /**
   * Use the $injector to create the controller factory
   * and inject mock dependencies
   */
  beforeEach(inject(function( $injector ) {

    // empty rootscope
    $rootScope = {};

    // load json mock data
    jasmine.getJSONFixtures().fixturesPath = 'base/tests/mock';

    // fake the http requests
    $httpBackend = $injector.get( '$httpBackend' );
    var package = { 'package': getJSONFixture( 'test.libskynet.json' ).results[0] };
    // package details mock
    requestHandler = $httpBackend
      .whenGET( '/api/package/libskynet' )
      .respond( package );

    // version details mock
    requestHandler = $httpBackend
      .whenGET( '/api/package/libskynet/version/0.1.11' )
      .respond( package );

    // version details mock
    requestHandler = $httpBackend
      .whenGET( '/api/package/libsk' )
      .respond({
        "package": null
      });

    // get the controller factory to create the search controller
    $controller = $injector.get( '$controller' );
    create = function ( $scope, $routeParams ) {
      // create the search controller
      return $controller( 'DetailController', {
        '$scope': $scope,
        '$rootScope': $rootScope,
        '$routeParams': $routeParams
      });
    };
  }));

  /**
   * Make shure after each test there is no
   * pending request to make
   */
  afterEach(function () {
    $httpBackend.verifyNoOutstandingExpectation();
    $httpBackend.verifyNoOutstandingRequest();
  });


  it( 'should load a package', function () {

    var $scope = {};
    var $routeParams = { 'package': 'libskynet' };
    var controller = create( $scope, $routeParams );

    // expect a request to the search api
    $httpBackend.expectGET( '/api/package/libskynet' );
    $httpBackend.expectGET( '/api/package/libskynet/version/0.1.11' );

    $httpBackend.flush();

    expect($scope.package.name).toBe('libskynet');
  });


  it( 'should show an error when a package is not found', function () {

    var $scope = {};
    var $routeParams = { 'package': 'libsk' };
    var controller = create( $scope, $routeParams );

    // expect a request to the search api
    $httpBackend.expectGET( '/api/package/libsk' );

    $httpBackend.flush();

    expect($rootScope.alerts.length).toBe(1);
  });


  it( 'should log a failed request of a package', function () {

    var $scope = {};
    var $routeParams = { 'package': 'libskynet' };
    var controller = create( $scope, $routeParams );

    // expect a request to the search api
    $httpBackend.expectGET( '/api/package/libskynet' )
      .respond(500, 'Internal Server error');

    // spy on the log
    spyOn(console, 'error');

    $httpBackend.flush();

    expect(console.error).toHaveBeenCalled();
  });


  it( 'should log a failed request of a package version', function () {

    var $scope = {};
    var $routeParams = { 'package': 'libskynet' };
    var controller = create( $scope, $routeParams );

    // expect a request to the search api
    $httpBackend.expectGET( '/api/package/libskynet' );

    // expect a request to the search api
    $httpBackend.expectGET( '/api/package/libskynet/version/0.1.11' )
      .respond(500, 'Internal Server error');

    // spy on the log
    spyOn(console, 'error');

    $httpBackend.flush();

    expect(console.error).toHaveBeenCalled();
  });
});
