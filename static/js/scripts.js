/*!
* Start Bootstrap - Small Business v5.0.5 (https://startbootstrap.com/template/small-business)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-small-business/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

$(document).ready(function() {

            $("#add-todo-button").click(function(){
               $("#todo-add-form").toggle( 'slow', function(){
               });
            });
         });

var x = document.getElementById("current-location");

function getLocation() {
    console.log(document.getElementById("hidden-location").value.split("$"))
    var val=document.getElementById("hidden-location").value.split("$")
  if (navigator.geolocation) {
    // navigator.geolocation.getCurrentPosition(showPosition);
      x.innerHTML = val[2];
      x.value = val[0]+","+val[1]
  } else {
    x.innerHTML = "Geolocation is not supported by this browser.";
  }
}

function showPosition(position) {
  x.innerHTML = "${val[2]}";
}
