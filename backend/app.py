from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

@app.route('/adminlogin', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'admin' and password == 'admin':
            return redirect(url_for('admin_dashboard'))  # You can define this route
        else:
            flash('Invalid credentials', 'error')
    return render_template('adminlogin.html')

@app.route('/admin-dashboard')
def admin_dashboard():
    return render_template('admin.html')

@app.route('/manage-posts')
def manage_posts():
    return render_template('managePosts.html')

@app.route('/manage-users')
def manage_users():
    return render_template('manageUsers.html')

if __name__ == '__main__':
    app.run(debug=True)
