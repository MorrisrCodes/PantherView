from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from pathlib import Path

# Root path resolution
BASE_DIR = Path(__file__).resolve().parent.parent

# Flask app setup
app = Flask(
    __name__,
    template_folder=str(BASE_DIR / 'templates'),
    static_folder=str(BASE_DIR / 'static')
)

app.secret_key = 'your_secret_key_here'

# ------------------ ROUTES ------------------ #

@app.route('/adminlogin', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'admin' and password == 'admin':
            return redirect(url_for('admin_dashboard'))
        else:
            flash('Invalid credentials', 'error')
    return render_template('adminlogin.html')


@app.route('/admin-dashboard')
def admin_dashboard():
    return render_template('dashboard.html')  # renamed from 'admin.html'


@app.route('/manage-posts')
def manage_posts():
    return render_template('managePosts.html')  # must match your actual HTML file


@app.route('/manage-users')
def manage_users():
    return render_template('manageUsers.html')  # fixed typo: was 'manage-users.html'


@app.route('/logout')
def logout():
    # Optional: session.clear()
    return redirect(url_for('admin_login'))


@app.route('/add-post', methods=['POST'])
def add_post():
    title = request.form.get('title')
    content = request.form.get('content')
    flash(f"Post '{title}' added successfully!", "success")
    return redirect(url_for('manage_posts'))


@app.route('/add-user', methods=['POST'])
def add_user():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')

    # Dummy user object for frontend (you’ll replace with DB logic later)
    new_user = {
        "id": 123,
        "username": username,
        "email": email
    }

    print(f"New user added: {new_user}")  # Debug print
    return jsonify(new_user), 200


if __name__ == '__main__':
    app.run(debug=True)
