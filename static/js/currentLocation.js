var x = document.getElementById("Use_Current_Location");
if (navigator.geolocation) {
  var currentLocation = new google.maps.LatLng(latitude, longitude);
  var coordjson = currentLocation.toJSON();

  $.post("/get_coords", {coordjson : data});
  var request = $.ajax({
   url: "/get_coords",
   type: "POST",
   contentType: "application/json",
   data: JSON.stringify(coordjson),
});
  .done( function (request) {
})
} else {
  x.innerHTML = "Geolocation is not supported by this browser.";
}
