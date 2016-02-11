//Functions assigned to buttons in the HTML
window.onload = function() {
var click = document.getElementById('submit').addEventListener("click", sendPost);
function sendPost() {
var xname = document.forms["slogin"]["name"].value;
  $.ajax({
    url: "getgames/request",
    method: "POST",
    dataType: "xml",
    data: {"test"}
    success: function (){console.log("yay")},
    error: function (){console.log("no")}
  });
}

}
