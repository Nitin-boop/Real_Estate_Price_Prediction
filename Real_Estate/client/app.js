function onPageLoad() {
    console.log("document loaded");
    var url = "http://127.0.0.1:5000/get_locations";
    $.get(url, function (data, status) {
        console.log("got response for get_location_name request");
        if (data) {
            var locations = data.locations;
            var uiLocations = document.getElementById("uiLocations");
            $('#uiLocations').empty();
            for (var i in locations) {
                var opt = new Option(locations[i]);
                $('#uiLocations').append(opt);
            }
        }
    });
}

function getBHK() {
var uiBHK = document.getElementsByName("uiBHK");
for (var i in uiBHK) {
    if(uiBHK[i].checked) {
        return parseInt(i)+1;
    }
}
return -1;
}

function getbath() {
var uibath = document.getElementsByName("uibath");
for (var i in uibath) {
    if(uibath[i].checked) {
        return parseInt(i)+1;
    }
}
return -1;
}

function EstimatePrice() {
    console.log("Estimate price button clicked");
    var sqft = document.getElementById("uiSqft");
    var bhk = getBHK();
    var bath = getbath();
    var location = document.getElementById("uiLocations");
    var estPrice = document.getElementById("uiEstimatedPrice");
    var url = "http://127.0.0.1:5000/get_price";
    console.log("There's nothing here");
    $.post(url, {
        "total_sqft" : parseFloat(sqft.value),
        "bhk" : bhk,
        "bath" : bath,
        "location" : location.value
    } ,function(data,status) {
    estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + "Lakh</h2>";
    console.log(status);
    });
}

window.onload = onPageLoad;