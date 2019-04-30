function currentLocation() {
  var x = document.getElementById("Use_Current_Location");
  if (navigator.geolocation) {
    getPosition(navigator.geolocation.getCurrentPosition());
  } else {
    x.innerHTML = "Geolocation is not supported by this browser.";
  }
}
function getPosition(position) {
  $.ajax({
              type: 'POST',
              contentType: 'application/json',
              data:  JSON.stringify({"latitude":position.coords.latitude,"longitude":position.coords.longitude}),
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
}

currentLocation();
