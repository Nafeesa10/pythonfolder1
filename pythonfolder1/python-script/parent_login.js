// Simple client-side validation for demonstration

document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const parentName = document.getElementById('parentName').value.trim();
    const password = document.getElementById('password').value.trim();
    const messageDiv = document.getElementById('loginMessage');

    if (parentName === '' || password === '') {
        messageDiv.textContent = 'Please enter both parent name and password.';
        messageDiv.style.color = '#d32f2f';
        return;
    }

    // Demo: Accept any non-empty input as valid
    messageDiv.textContent = 'Login successful! (Demo only)';
    messageDiv.style.color = '#388e3c';
    // In a real app, send credentials to the server here
});
