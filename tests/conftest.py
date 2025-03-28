import pytest

@pytest.fixture(scope="class")
def login(request):
    """Setup login fixture for tests"""
    # Get credentials from the test class
    username = request.cls.username
    password = request.cls.password
    print(f"Setup with username: {username} and password: {password}")
    
    # Add a login helper function to the test class
    def perform_login(self, username, password):
        """Mock function to simulate login process"""
        # Simulate authentication logic
        if not username or not password:
            return {
                "success": False,
                "message": "Username is required"
            }
        elif username == "student123" and password == "1234":
            return {
                "success": True,
                "redirect": "/home",
                "message": "Login successful"
            }
        else:
            return {
                "success": False,
                "message": "Invalid credentials"
            }
    
    # Attach the function to the test class
    request.cls.perform_login = perform_login
    
    # Run tests
    yield
    
    # Cleanup after tests
    print("Cleanup after login tests")