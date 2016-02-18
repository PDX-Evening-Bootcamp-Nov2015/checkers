//Functions assigned to buttons in the HTML
window.onload = function() {
console.log("test");

document.getElementById('board').addEventListener('click', selectSquare);


function selectSquare (event){
  console.log("test");
  var clickedItem = event.target.parentNode;
  alert(clickedItem.id);
}

};
