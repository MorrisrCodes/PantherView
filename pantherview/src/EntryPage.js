import React from "react";
import { useNavigate } from "react-router-dom";
import "./EntryPage.css";

function EntryPage() {
  const navigate = useNavigate();

  const handleEnter = () => {
    navigate("/login");
  };

  return (
    <div className="entry-page-wrapper">
      <div className="entry-logo-container">
        <img src="/images/gsuwordlogo.png" alt="GSU Logo" className="entry-logo" />
      </div>
      <div className="entry-container">
        <div className="sign-in-box">
          <h1>Welcome to PantherView</h1>
          <button onClick={handleEnter}>Enter</button>
        </div>
      </div>
    </div>
  );
}

export default EntryPage;
