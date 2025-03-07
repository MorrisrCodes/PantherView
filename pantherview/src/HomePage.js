import React from "react";
import "./HomePage.css";

function HomePage() {
  return (
    <div className="home-container">
      <div className="logo-container">
        <img src="/images/gsupantherlogo.png" alt="GSU Logo" className="gsu-logo" />
        <button className="button" data-text="Awesome">
          <span className="actual-text">&nbsp;PantherView&nbsp;</span>
          <span aria-hidden="true" className="hover-text">&nbsp;PantherView&nbsp;</span>
        </button>
      </div>
      <div className="content-container">
        <div className="map-container">
          <p>Map</p>
        </div>
        <div className="chat-box">
          <p>Chat</p>
        </div>
      </div>
    </div>
  );
}

export default HomePage;