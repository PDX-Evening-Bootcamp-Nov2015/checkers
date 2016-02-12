// //windows onload function
// //loads functions upon opening webpage
// //adds event listener to the submit button
// window.onload = function() {
//   document.getElementById("submit").addEventListener("click", checkForm, false);
// };
//
// function checkForm(event){
//
//
//   // errorDisplay1.style.display = 'none';
//   // errorDisplay2.style.display = 'none';
//   // errorDisplay3.style.display = 'none';
//   // errorDisplay4.style.display = 'none';
//   var xpass1 = document.getElementById("password1").value;
//   var xpass2 = document.getElementById("password2").value;
//   document.getElementById("login").noValidate = true;
//   if (xname === null || xname ===""){
//     event.preventDefault();
//     errorDisplay1.style.display = 'inline';
//   }else if (xusername === null || xusername ===""){
//     event.preventDefault();
//     errorDisplay2.style.display = 'inline';
//   }else if (xemail === null || xemail ===""){
//     errorDisplay3.style.display = 'inline';
//     event.preventDefault();
//   }else if (testEmail(xemail) === false){
//     errorDisplay4.style.display = 'inline';
//     event.preventDefault();
//   } else {
// event.preventDefault();
// sessionStorage.setItem('username', xusername);
// redirect();
//   }
// }
//
// //regex that is called by the checkform function to check proper email format
// // function testEmail(xemail){
// //   var regemail = /\S+@\S+\.\S+/;
// //   return regemail.test(xemail);
// // }
//
// //function called after checkform function is complete to redirect to gallery
// // function redirect(){
// //     window.location.href = "gallery.html";
// // }
