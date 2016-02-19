//Functions assigned to buttons in the HTML
window.onload = function() {
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
  success: function(result){display_pieces(result)},
  error: function(result){console.log("error")}

});
}

function display_pieces(data) {
var listOfPieces = data["key"];
for (i=0;i<listOfPieces.length;i++){
    if (listOfPieces[i][2] === "Red"){
      var a = listOfPieces[i][0] + "" + listOfPieces[i][1];
      var test = document.getElementById(String(a));
      test.children[0].src = redPieceNonKing;
    } else if (listOfPieces[i][2] === "Black") {
      var a = listOfPieces[i][0] + "" + listOfPieces[i][1];
      var test = document.getElementById(String(a));
      test.children[0].src = blackPieceNonKing;


    }



  // if ("" + listOfPieces[i][0] + "" + listOfPieces[i][1] === )

}

}

gameUrl = window.location.pathname;
console.log(gameUrl.split("/game/").pop());
};
