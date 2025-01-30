// Show the login form
function showLogin() {
    document.getElementById("account-check").classList.add("hidden");
    document.getElementById("login-form").classList.remove("hidden");
}

// Show the signup form
function showSignup() {
    document.getElementById("account-check").classList.add("hidden");
    document.getElementById("signup-form").classList.remove("hidden");
}

// Go back to the account check screen
function goBack() {
    document.getElementById("account-check").classList.remove("hidden");
    document.getElementById("login-form").classList.add("hidden");
    document.getElementById("signup-form").classList.add("hidden");
}
