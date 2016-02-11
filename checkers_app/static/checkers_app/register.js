//Functions assigned to buttons in the HTML
window.onload = function() {
document.getElementById("submit").addEventListener("click", passwordCheck, false);


function passwordCheck(){
  console.log(document.getElementById("password1").value);
  if (document.getElementById("password1").value != document.getElementById("password2").value){
    event.preventDefault();


  }
}



}
