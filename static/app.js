function getBathValue() {
  var uiBathrooms = document.getElementsByName("bath");
  for(var i in uiBathrooms) {
    if(uiBathrooms[i].checked) {
        return parseInt(uiBathrooms[i].value);
    }
  }
  return -1; // Invalid Value
}

function getBHKValue() {
  var uiBHK = document.getElementsByName("bhk");
  for(var i in uiBHK) {
    if(uiBHK[i].checked) {
        return parseInt(uiBHK[i].value);
    }
  }
  return -1; // Invalid Value
}









function onClickedEstimatePrice() {
  console.log("Estimate price button clicked");
  var sqft = document.getElementById("uiSqft").value;
  var bhk = getBHKValue();
  var bathrooms = getBathValue();
  var location = document.getElementById("uiLocations").value;
  var estPrice = document.getElementById("uiEstimatedPrice");

  var formData = {
    sqft: parseFloat(sqft),
    bhk: bhk,
    bath: bathrooms,
    location: location
  };

  $.post('/predict', formData, function(data) {
    estPrice.innerHTML = "<h2>" + data.prediction_text + "</h2>";
  }).fail(function(xhr, status, error) {
    console.log("Error: " + error);
  });
}

