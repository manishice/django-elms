
//password show hide

var a;
function pass(){

        if(a==1){
            document.getElementById('password').type = 'password';
            document.getElementById('show-pass').style.visibility = 'hidden';
            document.getElementById('hide-pass').style.visibility = 'visible';
            
            a = 0;
        
        }
        else {
            document.getElementById('password').type = 'text';
            document.getElementById('show-pass').style.visibility = 'visible';
            document.getElementById('hide-pass').style.visibility = 'hidden';
            a = 1;
        }
}


var b;
function cnfm_pass(){

        if(b==1){
            document.getElementById('password2').type = 'password';
            document.getElementById('show-pass2').style.visibility = 'hidden';
            document.getElementById('hide-pass2').style.visibility = 'visible';
            
            b = 0;
        
        }
        else {
            document.getElementById('password2').type = 'text';
            document.getElementById('show-pass2').style.visibility = 'visible';
            document.getElementById('hide-pass2').style.visibility = 'hidden';
            b = 1;
        }
}

// const toggler = document.querySelector(".btn");
// toggler.addEventListener("click", function(){
//   document.querySelector("#sidebar").classList.toggle("collapsed");
// })

//password validation


//confirm password validation
function checkPassword(){
  let password = document.getElementById('password').value;
  let cnfm_password = document.getElementById('password2').value;

  let message = document.getElementById('pass-message');

  if (password.length != 0){
    if (password != cnfm_password){
      message.textContent = "password doesn't match";
      message.style.color = "red";
    }
    else{
      message.textContent = "password matched";
      message.style.color = "grenn";
    }
  }
  else{
    alert("password must be required !!")
  }
}

$(".alert-dismissible").fadeTo(5000, 500).slideUp(500, function(){
  $(".alert-dismissible").alert('close');
});

// function toggleSidebar() {
//   document.querySelector('.wrapper').classList.toggle('sidebar-hidden');
// }


//phone number validation
function validatePhoneNumber() {
  const phoneNumber = document.getElementById("phone").value;
  const repeatedDigits = /^(.)\1{9}$/;
  const phoneRegex = /^\d{10}$/;

  if (!phoneRegex.test(phoneNumber)) {
      alert("Phone number must be exactly 10 digits.");
      return false;
  }

  if (repeatedDigits.test(phoneNumber)) {
      alert("Phone number cannot consist of repeated digits.");
      return false;
  }

  alert("Phone number is valid!");
  return true;
}

//auto close alert
$(document).ready(function () {
 
  window.setTimeout(function() {
      $(".alert").fadeTo(1000, 0).slideUp(1000, function(){
          $(this).remove(); 
      });
  }, 5000);
   
  });


//side bar
document.getElementById('toggleSidebar').addEventListener('click', function() {
  document.querySelector('.sidebar').classList.toggle('hidden');
  document.querySelector('.main').classList.toggle('full-width');
});
  
const pathName = window.location.pathname;
const pageName = pathName.split('/').pop();

//emp sidebar start
if (pageName === "leave_request"){
  document.querySelector('.leave_request').classList.add('active');
}

if (pageName === "view_history"){
  document.querySelector('.view_history').classList.add('active');
}

//emp sidebar end




//admin sidebar start
if (pageName === "dashboard"){
  document.querySelector('.dashboard').classList.add('active');
}

if (pageName === "emp_section"){
  document.querySelector('.emp_section').classList.add('active');
}

if (pageName === "department_section"){
  document.querySelector('.department_section').classList.add('active');
}

if (pageName === "leave_types"){
  document.querySelector('.leave_types').classList.add('active');
}

if (pageName === "pending"){
  document.querySelector('.pending').classList.add('active');
}

if (pageName === "approved"){
  document.querySelector('.approved').classList.add('active');
}

if (pageName === "declined"){
  document.querySelector('.declined').classList.add('active');
}

if (pageName === "leave_history"){
  document.querySelector('.leave_history').classList.add('active');
}

if (pageName === "admin_manage"){
  document.querySelector('.admin_manage').classList.add('active');
}


var fname = document.getElementById("fname");
var lname = document.getElementById("lname");
var address = document.getElementById("address");


var email = document.getElementById("email");
var password = document.getElementById("password");
var password2 = document.getElementById("password2");
var phone = document.getElementById("phone");


var fnameerror = document.getElementById("fnameerror");
var lnameerror = document.getElementById("lnameerror");
var addresserror = document.getElementById("addresserror");
var emailerror = document.getElementById("emailerror");
var phoneerror = document.getElementById("phoneerror");
var passworderror = document.getElementById("passworderror");
var password2error = document.getElementById("password2error");


var fullname = document.getElementById("fullname");
var uname = document.getElementById("uname");

var fullnameerror = document.getElementById("fullnameerror");
var usernameerror = document.getElementById("usernameerror");

var adminform = document.getElementById("adminform");

var form = document.getElementById("form");


const isValidEmail = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
const isValidPassword = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&#])[A-Za-z\d@$!%*?&#]{8,}$/;
const isValidPhone = /^(?!1\d{9})(?!.*(\d)\1{6})\d{10}$/;

form.addEventListener('submit', e => {
    let valid = true;

    if (!validateFname()) valid = false;
    if (!validateLname()) valid = false;
    
    if (!validateEmail()) valid = false;
    if (!validatePhone()) valid = false;
    if (!validateAddress()) valid  =  false;
    if (!validatePassword()) valid = false;
    if (!validatePassword2()) valid = false;
    
    if (valid) {
      form.submit();
     
        
    } else {
      e.preventDefault();
    }
});

adminform.addEventListener('submit', ed => {
  let valid = true;

  if (!validateFullname()) valid = false;
  if (!validateUsername()) valid = false;
  if (!validateEmail()) valid = false;
  if (!validatePassword()) valid = false;
  if (!validatePassword2()) valid = false;
  
  if (valid) {
    adminform.submit();
   
      
  } else {
    ed.preventDefault();
  }
});



function validateFname(){
  if (fname.value === ""){
      fnameerror.innerHTML = "Please enter first name";
      return false;
  } else {
      fnameerror.innerHTML = "";
      return true;
  }
}

function validateLname(){
  if (lname.value === ""){
      lnameerror.innerHTML = "Please enter last name";
      return false;
  } else {
      lnameerror.innerHTML = "";
      return true;
  }
}

function validateEmail(){
    if (email.value === ""){
        emailerror.innerHTML = "Please enter email";
        return false;
    } else if (!isValidEmail.test(email.value)){
        emailerror.innerHTML = "Please enter a valid email";
        return false;
    } else {
        emailerror.innerHTML = "";
        email.value = email.value.toLowerCase();
        return true;
    }
}

function validatePhone(){
    if (phone.value === ""){
        phoneerror.innerHTML = "Please enter phone number";
        return false;
    } else if (!isValidPhone.test(phone.value)){
        phoneerror.innerHTML = "Please enter a valid phone number";
        return false;
    } else {
        phoneerror.innerHTML = "";
        return true;
    }
}

function validateAddress(){
  if (address.value === ""){
      addresserror.innerHTML = "Please enter address";
      return false;
  } else {
      addresserror.innerHTML = "";
      return true;
  }
}

function validatePassword(){
    if (password.value === ""){
        passworderror.innerHTML = "Please enter password";
        return false;
    } else if (!isValidPassword.test(password.value)){
        passworderror.innerHTML = "Please enter a valid password";
        return false;
    } else {
        passworderror.innerHTML = "";
        return true;
    }
}

function validatePassword2(){
    if (password2.value === ""){
        password2error.innerHTML = "Please confirm password";
        return false;
    } else if (password.value !== password2.value){
        password2error.innerHTML = "Passwords do not match";
        return false;
    } else {
        password2error.innerHTML = "";
        return true;
    }
}






function validateFullname(){
  if (fullname.value === ""){
      fullnameerror.innerHTML = "Please enter full name";
      return false;
  }else if (fullname.value.length < 4){
    fullnameerror.innerHTML = "fullname must be 4 character"
    return false;
  } 
  else {
      fullnameerror.innerHTML = "";
      return true;
  }
}

function validateUsername(){
  if (uname.value === ""){
      usernameerror.innerHTML = "Please enter username";
      return false;
  } else if (uname.value.length < 4){
    usernameerror.innerHTML = "username must be 4 character"
    return false;
  }
  else {
      usernameerror.innerHTML = "";
      return true;
  }
}