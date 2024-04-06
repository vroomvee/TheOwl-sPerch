document.getElementById("loginForm").addEventListener("submit", async function(event) {
    event.preventDefault(); // Prevent default form submission

    // Get email, username, and password values
    var email = document.getElementById("email").value;
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    // Send POST request to the backend
    const response = await fetch('http://localhost:8000/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email, username, password })
    });

    // Check response status
    if (response.ok) {
        // Redirect the user to the homepage
        window.location.href = "homepage.html";
    } else {
        // Handle invalid credentials
        console.error('Login failed');
    }
});

