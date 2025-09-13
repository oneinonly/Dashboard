document.getElementById('registrationForm').addEventListener('submit', function(event) {
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirm_password').value;
    
    // Regular expression for password validation
    // Requires: at least 4 characters, one uppercase letter, one lowercase letter, one number, and one special character
    const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{4,}$/;

    // Check if passwords match
    if (password !== confirmPassword) {
        event.preventDefault(); // Stop the form from submitting
        alert("Passwords do not match. Please try again.");
        return; // Exit the function
    }

    // Check if password meets the complexity requirements
    if (!passwordRegex.test(password)) {
        event.preventDefault(); // Stop the form from submitting
        alert("Password must be at least 8 characters long and include at least one uppercase letter, one lowercase letter, one number, and one special character (@$!%*?&).");
        return; // Exit the function
    }
});