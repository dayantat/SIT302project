(function(){
    'use strict';

    angular.module('scrumboard.demo').directive('scrumboardCard', CardDirective);

    function CardDirective(){
        return {
            templateUrl: '/static/scrumboard/card.html',  // this calls the card.html
            restrict: 'E',  // passing E is for html element, 'A' is bound to an html attribute
            controller: ['$scope', '$http', function($scope, $http){
                var url = '/scrumboard/cards/' + $scope.card.id + '/';  // this is the url for the card being used
                $scope.update = function() {
                    $http.put(url, $scope.card);  // Put is used to update post is used to create
                };

                $scope.delete = function(){
                    $http.delete(url).then(
                        function(){
                            var cards = $scope.list.cards;  // the card list is assigned to the var cards
                            // The below finds the index of the card in the list.
                            cards.splice(cards.indexOf($scope.card), 1);
                        }
                    );
                };

                $scope.modelOptions = {
                    debounce: 500
                };
            }]
        };
    }
})();