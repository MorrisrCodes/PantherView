from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('login_db.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def entry():
    return render_template("entrypage/EntryPage.html")

@app.route("/login")
def login():
    return render_template("loginpage/LoginPage-inlineCss.html")

@app.route("/signup")
def signup():
    return render_template("loginpage/signupPage.html")

@app.route("/homepage")
def homepage():
    return render_template("homepage/buildings.html")

@app.route("/chats")
def chats():
    return render_template("homepage/chats.html")

@app.route("/map")
def map_page():
    return render_template("homepage/map.html")

@app.route("/dashboard")
def dashboard():
    return render_template("adminpage/dashboard.html")



# Add other routes similarly...

if __name__ == "__main__":
    app.run(debug=True)
