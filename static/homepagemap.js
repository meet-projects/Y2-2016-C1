$(document).ready(function() { 
	var map = new google.maps.Map(document.getElementById("map"), {center: {lat: 0, lng: 0}, zoom:2});
	console.log(map);


	// In the following example, markers appear when the user clicks on the map.
// Each marker is labeled with a single alphabetical character.
var labels = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
var labelIndex = 0;

var france = { lat: 46.2276, lng: 2.2137 };
var zero = { lat: 46.2276, lng: 0 };
var india = { lat: 20.5937, lng: 78.9629 };
var peru = { lat: 9.1900, lng: 75.0152 };


  var FranceMarker = new google.maps.Marker({
    position: france,
    label: labels[labelIndex++ % labels.length],
    title: 'This link opens Wikipedia home page',
    url : '/test'
  });
  var IndiaMarker = new google.maps.Marker({
    position: india,
    label: labels[labelIndex++ % labels.length],
    title: 'This link opens Wikipedia home page',
    url : '/test2'
  });
  var PeruMarker = new google.maps.Marker({
    position: peru,
    label: labels[labelIndex++ % labels.length],
    title: 'This link opens Wikipedia home page',
    url : '/test3'
  });

function initialize() {

  var mapProps = {
    zoom: 2,
    center: zero,
    draggable: false,
    scrollwheel: false
  }
  ; 
  // This event listener calls addMarker() when the map is clicked.
  var map=new google.maps.Map(document.getElementById("map"),mapProps);
  FranceMarker.setMap(map);
  IndiaMarker.setMap(map);
  PeruMarker.setMap(map);
  // add another marker
}

google.maps.event.addDomListener(window, 'load', initialize);
google.maps.event.addListener(FranceMarker, 'click', function() {window.location.href = FranceMarker.url;});
google.maps.event.addListener(PeruMarker, 'click', function() {window.location.href = PeruMarker.url;});
google.maps.event.addListener(IndiaMarker, 'click', function() {window.location.href = IndiaMarker.url;});
// add another listener to the new marker

}); 
