# GSU Campus Map Reporting System

An interactive 3D map of Georgia State University designed to allow students to report campus-related issues or events and assist administrators in managing and monitoring incident reports.

## 🚀 Features

### 🗺 Interactive Campus Map
- Built with **MapLibre GL JS** for dynamic 3D rendering  
- Displays buildings, dorms, and parks across the campus  
- Custom markers with popups containing report buttons  

### 📢 Issue & Event Reporting
- Users can click on a building/dorm/park to:  
  - Report an **Issue** (e.g., Theft, Vandalism, Safety Hazard)  
  - Report an **Event** (e.g., Party, Protest, Meeting)  
- Reports are submitted with the user's username and stored in a SQLite database  

### 👤 User Authentication
- Secure login & signup flow  
- Email validation to ensure `@gsu.edu` or `@student.gsu.edu` usage  
- Session-based access control  

### 🔐 Access Levels
- **Student Users:** Can log in, report events/issues, and navigate the map  
- **Admin Users:** Can access a dashboard to manage posts and users  

### 🛠 Admin Dashboard
- View and delete submitted reports  
- View and remove user accounts  

## 💾 Technologies Used
- **Frontend:** HTML, CSS, JavaScript, MapLibre GL JS  
- **Backend:** Python, Flask  
- **Database:** SQLite  

## 📌 Setup Instructions

1. **Clone this repo**:
   ```bash
   git clone https://github.com/yourusername/gsu-campus-map.git
   cd gsu-campus-map

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. **Install Flask**:
   ```bash
   pip install Flask

4. **Run the app**:
   ```bash
   python app.py

5. **Visit the app in your browser**:
   ```bash
   http://127.0.0.1:5000

## 🧠 Future Enhancements
- Real-time notifications for admins
- Filtering posts by location or type
- User profile and report history
- Map view toggle: satellite vs 3D
  

#### *Built with 💙 by Georgia State University students.*
