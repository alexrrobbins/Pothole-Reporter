$.ajax({
            type: 'POST',
            contentType: 'application/json',
            data:  JSON.stringify({'buttonPress' : 'T'}),
            dataType: 'json',
            url: '/button_press',
            success: function (e) {
                console.log(e);
                window.location = "/button_press";
            },
            error: function(error) {
            console.log(error);
        }
        });
