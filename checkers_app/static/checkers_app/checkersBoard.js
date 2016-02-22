//Functions assigned to buttons in the HTML
window.onload = function() {
document.getElementById('board').addEventListener('click', moveSquareDetermine);
document.getElementById('getPositions').addEventListener('click', get_positions);
//gameurl identifies the url in the users browser which is used in ajax calls
//to ensure that the user is sending and receiving data for the right game
gameUrl = window.location.pathname;
//get_positions function runs on pageload to automatically populate board's pieces
get_positions();
};


//store json data from the get_positions function for later manipulation
function saveData (data){
  lastKnownPieces = data;
}
//lastKnownPieces and moveCoordinates save click data prior to sending to the django views
var lastKnownPieces = 0
var moveCoordinates = {
  valid: 0,
  start_coords:0,
  color_start_coords:0,
  end_coords:0,
  color_end_coords:0,
  first_click:0,
  second_click:0,

}

//moveSquareDetermine calls either the moveSquareFirst or moveSquareSecond
//function depending on whether the user has clicked a selected piece or has
//clicked the square he wants to move to
function moveSquareDetermine (event){
  var clickedItem = event.target.parentNode;
  if (moveCoordinates.first_click === 0){
    moveSquareFirst(clickedItem);
  } else if (moveCoordinates.first_click === 1){
    moveSquareSecond(clickedItem);
  }
}

function moveSquareFirst (clickedItem) {
  for (i=0;i < lastKnownPieces.length; i++){
    if (clickedItem.id === lastKnownPieces[i][3]){
      moveCoordinates.start_coords = clickedItem.id;
      moveCoordinates.color_start_coords = lastKnownPieces[i][2];
      moveCoordinates.first_click = 1;
    }
  }
}

function moveSquareSecond (clickedItem) {
  if (clickedItem.id === moveCoordinates.start_coords){
    console.log("same piece - do nothing")
    return;
  }
  for (i=0;i < lastKnownPieces.length; i++){
    if (clickedItem.id === lastKnownPieces[i][3]){
      console.log("cant move a piece to a piece")
      return;
    }
  }
  moveCoordinates.end_coords = clickedItem.id;
  console.log("good move");
}
//get_positions makes an ajax call to the django views and returns the latest
//position of pieces on the board. The ajax calls upon the django views function
//"get_positions". Additionally the game id number which is taken from the
//gameurl object is sent as a variable to ensure the user is sending and
//receiving data for the right game. Upon return, this function calls the
//display_pieces function
function get_positions () {
var response = $.ajax({
  type: 'GET',
  url: "/get_positions/" + gameUrl.split("/game/").pop(),
  contentType: "application/json",
  success: function(result){display_pieces(result)},
  error: function(result){console.log("error")}

});
}
//the display_pieces function populates the checkers pieces on the game board
//additionally it calls the savedata function which saves the location information
//for the pieces
function display_pieces(data) {
var listOfPieces = data["key"];
saveData(listOfPieces);

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
  }
}
