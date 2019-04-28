//Code taken from https://stackoverflow.com/questions/17382128/google-maps-api-center-map-on-clients-current-location/17383412
  var map;
  function initMap() {
    map = new google.maps.Map(document.getElementById('map'));
  navigator.geolocation.getCurrentPosition(function(position) {
    var initialLocation = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
    map.setCenter(initialLocation);
    map.setZoom(12);
  }, function(positionError) {
    map.setCenter(new google.maps.LatLng(41.201992, -75.913101));
    map.setZoom(8);
  });
}
