function startInterview() {
    var role = document.getElementById('roleSelect').value;
    // Redirect to live interview page with selected role
    window.location.href = 'live-interview.html?role=' + role;
}
