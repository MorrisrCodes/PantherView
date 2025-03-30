import React from "react";
import { useNavigate } from "react-router-dom";
import "./LoginPage.css";

function LoginPage() {
  const navigate = useNavigate();

  const handleSignIn = () => {
    navigate("/home");
  };

  const handleSignUp = () => {
    navigate("/signup"); 
  };

  return (
    <div className="login-page-wrapper">
      <div className="login-container">
        <div className="gif-section">
          <div className="logo-container">
            <img src="/images/gsuwordlogo.png" alt="GSU Logo" className="logo" />
          </div>
          <img src="/images/flag.gif" alt="Login Gif" className="login-gif" />
        </div>
        <div className="sign-in-box">
          <h1>PantherView</h1>
          <input type="text" placeholder="StudentID" />
          <input type="password" placeholder="Password" />
          <button onClick={handleSignIn}>Sign In</button>
          <button className="sign-up-button" onClick={handleSignUp}>Sign Up</button>
        </div>
      </div>
    </div>
  );
}

export default LoginPage;