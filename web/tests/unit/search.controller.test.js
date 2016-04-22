
/**
 * Tests for the search controller
 */
describe( 'The Search Controller', function () {

  // locals
  var $controller,
    $httpBackend,
    create,
    requestHandler;

  // angular 'webly' module
  beforeEach(module('webly'));

  /**
   * Use the $injector to create the controller factory
   * and inject mock dependencies
   */
  beforeEach(inject(function( $injector ) {

    // load json mock data
    jasmine.getJSONFixtures().fixturesPath = 'base/tests/mock';

    // fake the http requests
    $httpBackend = $injector.get( '$httpBackend' );
    requestHandler = $httpBackend
      .whenGET( '/api/search/lib' )
      .respond(getJSONFixture( 'test.libskynet.json' ));

    // get the controller factory to create the search controller
    $controller = $injector.get( '$controller' );
    create = function ( $scope ) {
      // create the search controller
      return $controller( 'SearchController', { '$scope': $scope } );
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

  it( 'should find packages', function () {

    var $scope = {};
    var controller = create( $scope );

    // expect a request to the search api
    $httpBackend.expectGET( '/api/search/lib' );

    $scope.searchQuery = 'lib';
    $scope.change();

    $httpBackend.flush();

    console.log( $scope.results );

    expect($scope.results.length).toBe(2);
  });

  it( 'should not make an empty request', function () {

    var $scope = {};
    var controller = create( $scope );

    $scope.searchQuery = '';
    $scope.change();

    expect($scope.results.length).toBe(0);
  });


  it( 'should clear the result on click', function () {

    var $scope = {
      results: [ { 'result1': 1 }]
    };

    var controller = create( $scope );

    $scope.clearResults();

    expect($scope.results.length).toBe(0);
  });

  it( 'should log a failed request', function () {

    var $scope = {
      results: [ { 'result1': 1 }]
    };

    // expect a request to the search api
    $httpBackend.expectGET( '/api/search/lib' )
      .respond(500, 'Internal Server error');

    var controller = create( $scope );
    $scope.searchQuery = 'lib';
    $scope.change();

    // spy on the log
    spyOn(console, 'error');

    $httpBackend.flush();

    expect(console.error).toHaveBeenCalled();
  });

});
