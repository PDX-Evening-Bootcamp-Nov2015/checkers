//Functions assigned to buttons in the HTML
window.onload = function() {
  document.getElementById("play").onclick = randomnumber;
  document.getElementById("dice1keep").onclick = savedice2;
  document.getElementById("dice2keep").onclick = savedice1;
  document.getElementById("reset").onclick = reset;
};

//Stage counter the game begins at stage1
var stage = 1
//Number of rolls counter
count = 0

//rolls two random die and pushes both values to the dicelist,
//then updates the rolls counter, and passes the die values from dicelist to
//the diceholder object
function randomnumber () {
  if (stage <= 3) {
var dicelist = []
for (var i=0; i < 2; i++) {
  var rando = Math.random();
  rando = Math.floor(rando * 6);
  rando = rando + 1;
  dicelist.push(rando);
}
count = count +1;
diceholder(dicelist[0], dicelist[1]);
}
};

//rolls two random die but saves the value of dice1 and only pushes a new dice2
//to the the diceholder object
//updates the rolls counter
function savedice1 () {
  //player cannot save a 6
  if (stage <= 3 && dice1 != 6){
var dicelist = []
for (var i=0; i < 2; i++) {
  var rando = Math.random();
  rando = Math.floor(rando * 6);
  rando = rando + 1;
  dicelist.push(rando);
}
count = count +1;
diceholder(dice1 , dicelist[1]);
}
};

//rolls two random die but saves the value of dice2 and only pushes a new dice1
//to the the diceholder object
//updates the rolls counter
function savedice2 () {
  //player cannot save a 6
  if (stage <= 3 && dice2 != 6){
var dicelist = []
for (var i=0; i < 2; i++) {
  var rando = Math.random();
  rando = Math.floor(rando * 6);
  rando = rando + 1;
  dicelist.push(rando);
    }
count = count +1;
diceholder(dicelist[0], dice2)
  }
};

//saves the number of rolls already played
function rollcounter (count) {
  this.count = count;
}

//saves the value of dice1 and dice2 from the randomnumber and saveddice functions
//then calls the updatelist and addrow functions
function diceholder(dice1, dice2) {
  this.dice1 = dice1;
  this.dice2 = dice2;
  updateList();
  addrow(dice1, dice2);
}
//clears the HTML table
function updateList() {
  document.getElementById("Dice").innerHTML = "";
}

//resets the roll count and stage level, calls the randomnumber function
//to start the game over
function reset () {
  stage = 1;
  count = 0;
  randomnumber();
}

//takes the value of dice1, dice2, roll count, and stage level and creates cells
function addrow() {
  var table = document.getElementById("Dice");
  var row = table.insertRow();
  var cell1 = row.insertCell();
  var cell2 = row.insertCell();
  var cell3 = row.insertCell();
  var cell4 = row.insertCell();
  cell1.innerHTML = "<img  src=" + dice1 +  '.png>';
  cell2.innerHTML = "<img  src=" + dice2 +  '.png>';
  cell3.innerHTML = "Stage:" + stage;
  cell4.innerHTML = "Number of rolls:"+count

//if player rolls two 3's(angry dice) they lose and must press reset
if (dice1 === 3 && dice2 === 3) {
    if (stage <= 3) {
      stage = "Game Over";
      alert("You lost please press reset to play again");
      updateList();
      addrow();
    }
}
// if player rolls a 1 and a 2 they move on to stage 2
else if ((dice1 + dice2) === 3 && stage === 1) {
  stage = 2;
  updateList();
  addrow();
}
// if player rolls a 3 and a 4 they move on to stage 3
else if ((dice1 + dice2) === 7 && dice1 <= 4 && dice2 <= 4 && stage === 2) {
  stage = 3;
  updateList();
  addrow();
}
//if a player rolls a 5 and a 6 they win
else if ((dice1 + dice2) === 11 && stage === 3) {
  stage = "You are the Winner!";
  updateList();
  addrow();
  }
}
