//windows onload function
//loads functions upon opening webpage
//adds event listener to the submit button
window.onload = function() {
  document.getElementById("submit").addEventListener("click", checkForm, false);
};
console.log( document.getElementById("test").value)
function checkForm(event){
  var xpass1 = document.getElementById("password1").value;
  var xpass2 = document.getElementById("password2").value;
  document.getElementById("login").noValidate = true;
  document.getElementById("submit").noValidate = true;
  if (xpass1 === null || xpass1 ===""){
    event.preventDefault();
  }else if (xpass1 != xpass2){
    event.preventDefault();
  } else {
// event.preventDefault();
// sessionStorage.setItem('username', xusername);
// redirect();
console.log("password good")
  }
}

//regex that is called by the checkform function to check proper email format
// function testEmail(xemail){
//   var regemail = /\S+@\S+\.\S+/;
//   return regemail.test(xemail);
// }

//function called after checkform function is complete to redirect to gallery
// function redirect(){
//     window.location.href = "gallery.html";
// }
