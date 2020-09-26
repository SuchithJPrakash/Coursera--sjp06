(function () {
'use strict';

angular.module('myFirstApp', [])

.controller('MyFirstController',MyFirstController) 
function MyFirstController($scope) {
	$scope.name="";
	$scope.result="";
	$scope.compute = function () {
    var quote= calculate($scope.name);
    $scope.result = quote;
  };
  function calculate(string) {
    var char=string.split(',');
    if(string==''){
      	return "Please enter data first";
    }
    if(char.length<=3){
    	return "Enjoy";
    }
    if(char.length>3){
    	return "Too Much";
    }
    
  }


	// body...
}

})();
