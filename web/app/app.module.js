(function () {
  'use strict';

  // declare the 'webly' module
  var webly = angular.module( 'webly', [
    // angular router plugin
    'ngRoute',
    // angular clipboard plugin
    'ngclipboard'
  ]);

  // define routes using the route provider (angular router)
  webly.config( [ '$routeProvider', function( $routeProvider ) {

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
