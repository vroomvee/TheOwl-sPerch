// script.js

document.getElementById("employerLoginForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent default form submission

    // Get employer username and password values
    var employerUsername = document.getElementById("employerUsername").value;
    var employerPassword = document.getElementById("employerPassword").value;

    // Here, you might want to perform authentication checks for employers.
    // For simplicity, let's assume the login is successful.
    // You can add your authentication logic here.

    // Redirect the employer to the employer dashboard or relevant page
    window.location.href = "employer_dashboard.html"; // Change the destination page as needed
});
