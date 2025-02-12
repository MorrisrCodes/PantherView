import React from "react";
import "./LoginPage.css";

function LoginPage() {
  return (
    <div className="login-page-wrapper">
      <div className="login-container">
        <div className="gif-section">
          <img src="/images/flag.gif" alt="Login Gif" className="login-gif" />
          <div className="logo-container">
            <img src="/images/gsuwordlogo.png" alt="Logo" className="logo" />
          </div>
        </div>
        <div className="sign-in-box">
          <h2>PantherView</h2>
          <input type="text" placeholder="StudentID" />
          <input type="password" placeholder="Password" />
          <button>Sign In</button>
        </div>
      </div>
    </div>
  );
}

export default LoginPage;
