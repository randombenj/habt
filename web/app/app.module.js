(function () {
  'use strict';

  // declare the 'habt' module
  var habt = angular.module( 'habt', [
    // angular router plugin
    'ngRoute',
    // angular clipboard plugin
    'ngclipboard'
  ]);

  // define routes using the route provider (angular router)
  habt.config( [ '$routeProvider', function( $routeProvider ) {

    // configure the routes
    $routeProvider

      // configure the 'detail' route
      .when('/detail/:package', {
        templateUrl: '/app/components/detail/detail.view.html',
        controller: 'DetailController'
      })

      // default redirect to the 'search'
      .otherwise({
        redirectTo: '/'
      });
  }]);
})();
