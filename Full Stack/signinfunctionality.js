document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("signin-form").addEventListener("submit", function(event) {
        event.preventDefault(); // Prevent form submission
        
        // Get the username and password from the form
        var username = document.getElementById("username").value;
        var password = document.getElementById("password").value;

        // Simulate authentication process (replace with your actual authentication logic)
        // For demonstration, let's assume valid credentials are "user123" for both username and password
        if (username === "user123" && password === "user123") {
            alert("Sign in successful!");
            // Here you can redirect the user to another page or perform other actions after successful sign-in
        } else {
            alert("Invalid username or password. Please try again.");
        }
    });
});