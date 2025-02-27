import React from "react";
import { useNavigate } from "react-router-dom";
import "./EntryPage.css";

function EntryPage() {
  const navigate = useNavigate();

  const handleEnter = () => {
    navigate("/login");
  };

  return (
    <div className="entry-background-gif">
      <img src="/images/PantherViewHomePage.gif" alt="Background gif" className="background-gif" />
      <div className="entry-header">
        <header>
          <div className="header-text">PantherView</div>
          <img src="/images/pixel-panther.png" alt="Panther logo" className="header-logo" />
        </header>
        {/* entry-logo class for panther pixel image */}
      </div>
      
      <div className="intro-container">
        <div className="intro-header">
          <p> Stay Connected, Stay Safe. </p>
        </div>
        <div className="introduction">
          <p>Join the Georgia State community in making our campus safer and more connected. Share and receive real-time alerts about campus activities and safety concerns.</p>
        </div>
      </div>

      <div className="button">
        <button onClick={handleEnter}>Get Started</button>
      </div>


      <div className="safety-container">
        <div className="safety-image">
          {/* insert image */}
          <h2><b>Safety Alerts</b></h2>
          <h3>Receive real-time notifications about safety concerns on campus</h3>
        </div>
      </div>
    </div>
  );
}

export default EntryPage;