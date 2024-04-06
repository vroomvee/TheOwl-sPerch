document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission
    // Your login logic here
    console.log('Login button clicked');
});
// script.js

document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent default form submission

    // Get username and password values
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    // Here, you might want to perform authentication checks.
    // For simplicity, let's assume the login is successful.
    // You can add your authentication logic here.

    // Redirect the user to the homepage
    window.location.href = "homepage.html";
});
