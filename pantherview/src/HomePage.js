import React, { useState } from "react";
import "./HomePage.css";

function HomePage() {
  const [dropdowns, setDropdowns] = useState([]);

  const toggleDropdown = (type) => {
    setDropdowns((prev) =>
      prev.includes(type) ? prev.filter((item) => item !== type) : [...prev, type]
    );
  };

  return (
    <div className="home-container">
      <div className="logo-container">
        <img src="/images/gsuwordlogo.png" alt="GSU Logo" className="gsu-logo" />
        <button className="button" data-text="Awesome">
          <span className="actual-text">&nbsp;PantherView&nbsp;</span>
          <span aria-hidden="true" className="hover-text">&nbsp;PantherView&nbsp;</span>
        </button>
      </div>
      <input type="text" className="search-bar" placeholder="Search" />
      <div className="content-container">
        <div className="map-container">
          <p>Map</p>
          <div className="taskbar">
            {['Buildings', 'Dorms', 'Parks', 'Alerts'].map((item) => (
              <div key={item} className="taskbar-item">
                <button className="taskbar-button" onClick={() => toggleDropdown(item)}>{item}</button>
                {dropdowns.includes(item) && (
                  <div className="dropdown-box">
                    <p>{item} Information</p>
                  </div>
                )}
              </div>
            ))}
          </div>
        </div>
        <div className="chat-container">
          <div className="alerts-container">Alerts</div>
          <div className="chats-container">Chats</div>
        </div>
      </div>
    </div>
  );
}

export default HomePage;
