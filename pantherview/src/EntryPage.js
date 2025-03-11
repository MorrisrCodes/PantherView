import React from "react";
import { useNavigate } from "react-router-dom";
import "./EntryPage.css";

function EntryPage() {
  const navigate = useNavigate();

  const handleEnter = () => {
    navigate("/login");
  };

  return (
    <div className="main">
      <div className="background">
        <img src="/images/PantherViewHomepage.png"/>
      </div>
      <header>
        <div className="name">
          <h1> PantherView </h1>
        </div>

        <div className="logo">
          <img src= "/images/pixel-panther.png" alt="Panther logo" className="panther-logo"/>
        </div>
      </header>

      <div className="intro-container">
        <div class="center">
          <div className="intro-header">
            <h1>Stay Safe, Stay Connected</h1>
          </div>

          <div className="intro">
            <h2>
              Join the Georgia State community in making our campus safer and more connected. Share and receive real-time alerts about campus activities and safety concerns.
            </h2>
          </div>

          <div>
            <button className="start-button" onClick={handleEnter}>Get Started</button>
          </div>
          
          <div className="boxes">
         
            <div className="box-1">
              <div className="box-1-image">
                <img src="/images/pixel-panther.png" alt="Panther logo" className="box-1-logo"/>
              </div>
      
              <div className="box-1-header">
                <h1>
                  Real-time Alerts
                </h1>
              </div>

              <div className="box-1-content">
                <p> Receive instant notifications about important campus events and safety concerns </p>
              </div>
            </div>

            <div className="box-2">
              <div className="box-2-image">
                <img src="/images/pixel-panther.png" alt="Panther logo" className="box-1-logo"/>
              </div>
      
              <div className="box-2-header">
                <h1>
                  Interactive Map
                </h1>
              </div>

              <div className="box-2-content">
                <p> Navigate campus with an interactive map showing real-time activity pins </p>
              </div>
            </div>

            <div className="box-3">
              <div className="box-3-image">
                <img src="/images/pixel-panther.png" alt="Panther logo" className="box-1-logo"/>
              </div>
      
              <div className="box-3-header">
                <h1>
                  Safety First
                </h1>
              </div>

              <div className="box-3-content">
                <p> Contribute to campus by reporting and viewing safety related information </p>
              </div>
            </div>

            <div className="box-4">
              <div className="box-4-image">
                <img src="/images/pixel-panther.png" alt="Panther logo" className="box-1-logo"/>
              </div>
      
              <div className="box-4-header">
                <h1>
                  Community Driven
                </h1>
              </div>

              <div className="box-4-content">
                <p> Connect with fellow Panthers and build a stronger campus community </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default EntryPage;