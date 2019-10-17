

var app = angular.module('myApp', []);
  
 app.controller('homeController', function($scope) {
     $scope.message = 'I am the homepage';
 });

app.controller('test', function($scope, $http) {
  $scope.message = "hellow angular";
});

//--------------------------------------User List Controller-----------------------------------------------
app.controller("UserList", function ($scope, $http) {
    $scope.message= "shadmaan s"
    $scope.init = function () {
        $scope.getUserlist();
    }
    $scope.getUserlist = function () {
        $http.get("/api/userlist/")
        .then(function (response) {
            $scope.getUserlist = response.data.user_list
            console.log($scope.getUserlist)
            console.log($scope.getUserlist.slug)
        });
    }
});

//---------------------------------------User Profile Controller----------------------------------------------
app.controller("User_profile", function ($scope, $http) {
    $scope.init = function () {
        $scope.getUserProfile();
    }
    pk = 1;
    url = '/api/userprofile/'+pk+''
    $scope.getUserProfile = function () {
        $http.get(url)
        .then(function (response) {
            $scope.getUserProfile = response.data.user_profile 
        });
    }
});

//---------------------------------------Friends Controller----------------------------------------------
app.controller("profilecontroller", function ($scope, $http) {
    $scope.init = function () {
        $scope.profile();
    }
    url = '/api/current-user-detail/'
    $scope.profile = function () {
        $http.get(url)
        .then(function (response) {
            $scope.profile = response.data 
            console.log($scope.profile) 
        });
    }
});


//---------------------------------------Get google news----------------------------------------------
app.controller("newscontroller", function ($scope, $http) {
    $scope.init = function () {
        $scope.getnews();
    }
    url = 'https://newsapi.org/v2/top-headlines?sources=google-news&apiKey=8a3e61e6a74743b897c9e6add302e400'
    $scope.getnews = function () {
        $http.get(url)
        .then(function (response) {
            angular.forEach(response.data, function(value, key) {

                $scope.getnews=value
            })           
        });
    }
});

//---------------------------------------Weather information----------------------------------------------
app.controller("weathercontroller", function ($scope, $http) {
    $scope.init = function () {
        $scope.message= 'working'
        $scope.getweather();
        $scope.weatherinfo=[];
        $scope.windinfo=[];
    }
    url = 'http://api.openweathermap.org/data/2.5/weather?q=india,delhi&APPID=73a333995eb98f4d8142f56af163a5ad'
    $scope.getweather = function () {
        
        $http.get(url)
        .then(function (response) {
            $scope.getweather = response.data
            $scope.weatherinfo.push(response.data.weather[0]);           
        });
    }
});

