//Code taken from https://stackoverflow.com/questions/17382128/google-maps-api-center-map-on-clients-current-location/17383412
  var map;
  function initMap() {
    map = new google.maps.Map(document.getElementById('map'));
    navigator.geolocation.getCurrentPosition(function(position) {
    var latitude = position.coords.latitude
    var longitude = position.coords.longitude
    var initialLocation = new google.maps.LatLng(latitude, longitude);
    var coordsjson = initialLocation.toJSON();
    map.setCenter(initialLocation);
    map.setZoom(12);
    $.ajax({
                type: 'POST',
                contentType: 'application/json',
                data:  JSON.stringify(coordsjson),
                dataType: 'json',
                url: '/get_coords',
                success: function (e) {
                    console.log(e);
                    window.location = "/get_coords";
                },
                error: function(error) {
                console.log(error);
            }
            });
  }, function(positionError) {
    map.setCenter(new google.maps.LatLng(41.201992, -75.913101));
    map.setZoom(8);
  });
}
