from flask import Flask, render_template, request, redirect, url_for, flash, get_flashed_messages
import sqlite3

app = Flask(__name__)
app.secret_key = "secret"

def get_db_connection():
    conn = sqlite3.connect('login_db.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def entry():
    return render_template("entrypage/EntryPage.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        conn = get_db_connection()
        user = conn.execute(
            "SELECT * FROM users WHERE username = ? AND password = ?",
            (username, password)
        ).fetchone()
        conn.close()

        if user:
            if user["access"] == 1:
                return redirect(url_for("dashboard")) # admin user
            else:
                return redirect(url_for("homepage")) # regular user
        else:
            flash("Invalid username or password.") # not in db
            return redirect(url_for("login"))

    return render_template("loginpage/LoginPage-inlineCss.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("new-username")
        password = request.form.get("new-password")
        email = request.form.get("email")

        if not username or not password or not email:
            flash("All fields are required.")
            return redirect(url_for("signup"))

        if not (email.endswith("@student.gsu.edu") or email.endswith("@gsu.edu")): # checking if student by email extension
            flash("Please register with a GSU school email.")
            return redirect(url_for("signup"))

        conn = get_db_connection()

        existing_user = conn.execute(
            "SELECT * FROM users WHERE username = ? OR email = ?", (username, email)
        ).fetchone()

        if existing_user:
            conn.close()
            flash("Username or email already exists.")
            return redirect(url_for("signup"))

        conn.execute(
            "INSERT INTO users (email, username, password) VALUES (?, ?, ?)",
            (email, username, password)
        )
        conn.commit()
        conn.close()

        flash("Account created successfully!")
        return redirect(url_for("login"))

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

if __name__ == "__main__":
    app.run(debug=True)
