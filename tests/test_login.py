import pytest

@pytest.mark.usefixtures("login")
class TestLogin:
    username = "student123"
    password = "1234"
    
    def test_login_valid_credentials(self):
        """Test login with valid credentials"""
        # Simulate successful login using the fixture
        result = self.perform_login(self.username, self.password)
        
        # Assert login was successful
        assert result["success"] == True
        assert result["redirect"] == "/home"
    
    def test_login_invalid_credentials(self):
        """Test login with invalid credentials"""
        # Simulate failed login
        result = self.perform_login("wrong_user", "wrong_pass")
        
        # Assert login failed appropriately
        assert result["success"] == False
        assert "Invalid credentials" in result["message"]
    
    def test_login_empty_fields(self):
        """Test login with empty fields"""
        # Simulate login with empty fields
        result = self.perform_login("", "")
        
        # Assert proper validation error
        assert result["success"] == False
        assert "Username is required" in result["message"]