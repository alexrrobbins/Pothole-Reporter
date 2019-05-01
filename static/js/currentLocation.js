

var coordsjson = {'filler':'tokens'}

navigator.geolocation.getCurrentPosition(function(position) {
var latitude = position.coords.latitude
var longitude = position.coords.longitude
var initialLocation = new google.maps.LatLng(latitude, longitude);
coordsjson = initialLocation.toJSON();
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

});
