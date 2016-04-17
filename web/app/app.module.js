(function () {
  'use strict';

  // declare the 'webly' module and add the route module
  var webly = angular.module('webly', ['ngRoute']);

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
