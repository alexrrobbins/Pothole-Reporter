//Code taken from https://stackoverflow.com/questions/17382128/google-maps-api-center-map-on-clients-current-location/17383412 and fixed with CoPilot's help

function loadScript() {
  var script = document.createElement('script');
  script.src = 'https://maps.googleapis.com/maps/api/js?key=<insertkeyhere>&callback=initMap';
  script.async = true;
  script.defer = true;
  document.head.appendChild(script);
}

var map;
var latitude;
var longitude;
var initialLocation;
function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    center: { lat: 41.201992, lng: -75.913101 },
    zoom: 8
  });
  navigator.geolocation.getCurrentPosition(function(position) {
      latitude = position.coords.latitude;
      longitude = position.coords.longitude;
      initialLocation = new google.maps.LatLng(latitude, longitude);
      map.setCenter(initialLocation);
      map.setZoom(12);
  }, function(positionError) {
      map.setZoom(5);
  });
}

function getCoords() {
      var coordsjson = JSON.stringify(initialLocation.toJSON());
      $.ajax({
        type: 'POST',
        contentType: 'application/json',
        data: coordsjson,
        dataType: 'json',
        url: '/get_coords',
        success: function (e) {
          console.log(e);
        },
        error: function(error) {
          console.log(error);
        }
      });      
}


loadScript();