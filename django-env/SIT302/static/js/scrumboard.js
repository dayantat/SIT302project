(function(){
                'use strict';

                angular.module('scrumboard.demo', ['ngRoute'])
                    .controller('ScrumboardController', [ '$scope', '$http', ScrumboardController]);  // the services $scope and $http must be strings

                function ScrumboardController($scope, $http) {  // $http must be used as a variable
                    $scope.add = function(list, title) {
                        var card = {
                            list: list.id,
                            title: title
                        };
                        $http.post('/scrumboard/cards/', card).then(function(response){  // This is a completed post request
                            list.cards.push(response.data);  // Adds a new card to the server
                        },
                        // 403 errors can occurs when a user is logged in, this will be solved later
                        function(){  // If something fails the below will execute
                            alert('Could not create card');  // Only the Alert will show
                        });


                    };



                    $scope.data = [];
                    // This is a instance call, and will be updated when it receives a response from the server
                    $http.get('/scrumboard/lists/').then(function(response){  //  This is a get request the lists object
                        $scope.data = response.data;

                    });


                }

            }());