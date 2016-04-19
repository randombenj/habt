(function () {
  'use strict';

  angular
    .module('webly')
    .controller( 'DetailController', DetailController );

  /**
   * The detail controller
   *
   * @param {Object} $scope
   *  The injected DOM scope
   *
   * @param {[type]} $http
   *  Module to make async HTTP Requests
   */
  function DetailController ( $scope, $http, $routeParams ) {

    if ( $routeParams.hasOwnProperty( 'package' ) ) {

      // load the package data of the requested package
      loadPackageData( $routeParams.package );
    }

    // define $scope api
    $scope.loadVersionData = loadVersionData;

    /**
     * Loads the data of a package with agiven name
     * @param  {String} packageName
     *  The name of the packag
     */
    function loadVersionData( version ) {

      // make a search api request
      // to load data about a package
      $http({
        method: 'GET',
        url: '/api/package/' + $scope.package.name + '/version/' + version
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
          $scope.version = data.data.version;
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

    /**
     * Loads the data of a package with agiven name
     * @param  {String} packageName
     *  The name of the packag
     */
    function loadPackageData( packageName ) {

      // make a search api request
      // to load data about a package
      $http({
        method: 'GET',
        url: '/api/package/' + packageName
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
          $scope.package = data.data.package;

          if ( $scope.package.versions.length > 0 ) {

            // display the first version
            loadVersionData( $scope.package.versions[0].version );
          }
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

  }

})();
