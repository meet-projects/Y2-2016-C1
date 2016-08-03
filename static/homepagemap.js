$(document).ready(function() { 
	var map = new google.maps.Map(document.getElementById("map"), {center: {lat: 0, lng: 0}, zoom:2});
	console.log(map);


	// In the following example, markers appear when the user clicks on the map.
// Each marker is labeled with a single alphabetical character.
var labels = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
var labelIndex = 0;

function initialize() {
  var france = { lat: 46.2276, lng: 2.2137 };
  var india = { lat: 20.5937, lng: 78.9629 };
  var zero = { lat: 46.2276, lng: 0 };
  var peru = { lat: 9.1900, lng: 75.0152 };
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 2,
    center: zero
  });

  // This event listener calls addMarker() when the map is clicked.
  google.maps.event.addListener(map, 'click', function(event) {
    addMarker(event.latLng, map);
  });

  // Add a marker at the center of the map.
  addMarker(france, map);
  addMarker(india, map);
  addMarker(peru, map);
}

// Adds a marker to the map.
function addMarker(location, map) {
  // Add the marker at the clicked location, and add the next-available label
  // from the array of alphabetical characters.
  var marker = new google.maps.Marker({
    position: location,
    label: labels[labelIndex++ % labels.length],
    map: map
  });
}

google.maps.event.addDomListener(window, 'load', initialize);
}); 