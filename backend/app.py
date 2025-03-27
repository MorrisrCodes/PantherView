from flask import Flask, render_template, redirect, url_for, request, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize Flask app and database
app = Flask(__name__, static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SECRET_KEY'] = 'mysecretkey'  # For session management

# Initialize database
db = SQLAlchemy(app)

# Define the admin credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin"

# Define the Post model
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()  # This creates the tables in the database

# Route for the Admin Login Page
@app.route('/adminlogin', methods=['GET', 'POST'])
def adminlogin():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check if the username and password are correct
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['logged_in'] = True  # Store session data for login state
            return redirect(url_for('admin_dashboard'))  # Redirect to the admin dashboard page
        else:
            error = "Invalid username or password"
    
    return render_template('adminlogin.html', error=error)


# Route for the Admin Dashboard
@app.route('/admin', methods=['GET'])
def admin_dashboard():
    if not session.get('logged_in'):
        return redirect(url_for('adminlogin'))  # Redirect to login if not logged in
    
    posts = Post.query.all()  # Fetch all posts from the database
    return render_template('admin.html', posts=posts)  # Render admin dashboard with posts


# Route for Manage Posts
@app.route('/manageposts')
def manage_posts():
    # Here, you would manage posts
    return "Manage Posts Page"

# Route for Manage Users
@app.route('/manageusers')
def manage_users():
    # Here, you would manage users
    return "Manage Users Page"

# Route for Logging Out
@app.route('/logout')
def logout():
    session.pop('logged_in', None)  # Remove login session
    return redirect(url_for('adminlogin'))  # Redirect to login page


if __name__ == '__main__':
    app.run(debug=True)
