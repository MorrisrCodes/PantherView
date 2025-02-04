from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('login_db.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return render_template('entry.html')

@app.route('/login', methods=["GET", "POST"])
def main():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ? AND password = ?', 
                            (username, password)).fetchone()
        conn.close()
        
        if user:
            return redirect(url_for('dashboard'))
        else:
            return "Invalid credentials, please try again."
    
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return "Welcome to your dashboard!"

@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == 'POST':
        username = request.form['new-username']
        password = request.form['new-password']
        email = request.form['email']

        conn = get_db_connection()
        conn.execute('INSERT INTO users (email, username, password) VALUES (?, ?, ?)', 
                     (email, username, password))
        conn.commit()
        conn.close()

        return redirect(url_for('main'))
    
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)