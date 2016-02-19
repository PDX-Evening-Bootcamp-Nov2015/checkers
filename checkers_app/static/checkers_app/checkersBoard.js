//Functions assigned to buttons in the HTML
window.onload = function() {
console.log("test");

document.getElementById('board').addEventListener('click', selectSquare);
document.getElementById('getPositions').addEventListener('click', get_positions);
gameUrl = window.location.pathname;

function selectSquare (event){
  console.log("test");
  var clickedItem = event.target.parentNode;
  // alert(clickedItem.id);

  var response = $.ajax({
      type: 'GET',
      url: "/board/" + clickedItem.id,
      contentType: "application/json",
      success: function(result){console.log(result)},
      error: function(result){console.log("Error")}
  });
}
function get_positions () {
var response = $.ajax({
  type: 'GET',
  url: "/get_positions/" + gameUrl.split("/game/").pop(),
  contentType: "application/json",
  success: function(result){console.log(result)},
  error: function(result){console.log("error")}

});
}
gameUrl = window.location.pathname;
console.log(gameUrl.split("/game/").pop());
};
