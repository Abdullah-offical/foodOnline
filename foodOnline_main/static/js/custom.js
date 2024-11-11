

let autocomplete;

function initAutoComplete(){
autocomplete = new google.maps.places.Autocomplete(
    document.getElementById('id_address'),
    {
        types: ['geocode', 'establishment'],
        //default in this app is "PK" - add your country code
        componentRestrictions: {'country': ['pk']},
    })
// function to specify what should happen when the prediction is clicked
autocomplete.addListener('place_changed', onPlaceChanged);
}

function onPlaceChanged (){
    var place = autocomplete.getPlace();

    // User did not select the prediction. Reset the input field or alert()
    if (!place.geometry){
        document.getElementById('id_address').placeholder = "Start typing...";
    }
    else{
        console.log('place name=>', place.name)
    }
    // get the address components and assign them to the fields
    // console.log(place) // get all data for place 
    var geocoder = new google.maps.Geocoder()
    var address = document.getElementById('id_address').value
    // console.log(address) // get only address

    geocoder.geocode({'address': address}, function(results, status){
        // console.log('results=>', results);
        // console.log('status=>', status);

        if(status == google.maps.GeocoderStatus.OK){
            var latitude = results[0].geometry.location.lat();
            var longitude = results[0].geometry.location.lng();

            // console.log('lat=>', latitude);
            // console.log('long=>', longitude);
            // Set the values using vanilla JS
            document.getElementById('id_latitude').value = latitude;
            document.getElementById('id_longitude').value = longitude;

            document.getElementById('id_address').value = address;

        }
    });
}
