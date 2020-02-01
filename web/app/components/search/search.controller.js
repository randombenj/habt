(function () {
  'use strict';

  angular
    .module('habt')
    .controller( 'SearchController', SearchController );

  /**
   * The search controller
   *
   * @param {Object} $scope
   *  The injected DOM scope
   *
   * @param {[type]} $http
   *  Module to make async HTTP Requests
   */
  function SearchController ( $scope, $http ) {

    $scope.clearResults = function () {

      // when a user clicks on a result,
      // hide the shown suggestions
      $scope.results = [];
    };

    /**
     * Gets called when the search input changes
     */
    $scope.change = function () {

      if ( $scope.searchQuery === '' ) {

          // don't perform an empty search
          $scope.results = [];

      } else {

        // make a search api request
        $http({
          method: 'GET',
          url: '/api/search/' + $scope.searchQuery
        })
        .then(

          /**
           * Successful api call
           * @param  {Object} data
           *  api response from the server
           */
          function success( data ) {

            // log the data in the console
            console.log( 'Got from ' + data.config.url + ': ', data );

            // display the search results
            $scope.results = data.data.results;
          },

          /**
           * An error has occured while performing the api call
           * @param  {Object} error
           *  Error details
           */
          function error( error ) {

            // log the error in the console
            console.error( 'Error from ' + error.config.url + ': ', error );
          }
        );
      }
    };
  }

})();
