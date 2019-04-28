function currentLocation() {
  var x = document.getElementById("Use_Current_Location");
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  } else {
    x.innerHTML = "Geolocation is not supported by this browser.";
  }
}
function getPosition(position) {
  var lat = position.coords.latitude;
  var long = position.coords.longitude;
  var coordjson = [
    {"latitude":lat},
    {"longitude":long}
  ];
  $.post("result", coordjson, function(){});
}
