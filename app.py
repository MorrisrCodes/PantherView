from flask import Flask, render_template, request, redirect, url_for, flash, get_flashed_messages, session, jsonify
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
            # Use username instead of ID
            session["username"] = user["username"]
            session["email"] = user["email"]
            session["access"] = int(user["access"] or 0)

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
    if "username" not in session: # check if user is logged in
        flash("You must be logged in to view the homepage.")
        return redirect(url_for("login"))
    return render_template("homepage/buildings.html")

@app.route("/chats")
def chats():
    if "username" not in session:
        flash("You must be logged in to view this page.")
        return redirect(url_for("login"))
    return render_template("homepage/chats.html")

@app.route("/map")
def map_page():
    if "username" not in session:
        flash("You must be logged in to view this page.")
        return redirect(url_for("login"))
    return render_template("homepage/map.html")

@app.route("/dashboard")
def dashboard():
    if "username" not in session or session.get("access") != 1: # check if user is logged in and has admin access
        flash("Login under an admin account to access this page.")
        return redirect(url_for("login"))
    return render_template("adminpage/dashboard.html")

@app.route("/manage_posts", methods=["GET", "POST"])
def manage_posts():
    if "username" not in session or session.get("access") != 1:
        flash("Login under an admin account to access this page.")
        return redirect(url_for("login"))

    conn = get_db_connection()

    if request.method == "POST":
        post_id = request.form.get("delete_id")
        if post_id:
            conn.execute("DELETE FROM posts WHERE post_id = ?", (post_id,))
            conn.commit()

    posts = conn.execute("SELECT post_id, type, location FROM posts").fetchall()
    conn.close()

    return render_template("adminpage/managePosts.html", posts=posts)

@app.route("/manage_users", methods=["GET", "POST"])
def manage_users():
    if "username" not in session or session.get("access") != 1:
        flash("Login under an admin account to access this page.")
        return redirect(url_for("login"))

    conn = get_db_connection()

    if request.method == "POST":
        username_to_delete = request.form.get("delete_username")
        if username_to_delete:
            conn.execute("DELETE FROM users WHERE username = ?", (username_to_delete,))
            conn.commit()

    users = conn.execute("SELECT username, email FROM users").fetchall()
    conn.close()

    return render_template("adminpage/manageUsers.html", users=users)

@app.route("/report", methods=["POST"])
def report():
    if "username" not in session:
        print("Not logged in")
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json()
    location = data.get("location")
    type_ = data.get("type")
    username = session["username"]

    print("Received report:", location, type_, username)

    conn = get_db_connection()
    conn.execute(
        "INSERT INTO posts (type, location, username) VALUES (?, ?, ?)",
        (type_, location, username)
    )
    conn.commit()
    conn.close()

    print("Inserted into DB successfully")
    return jsonify({"message": "Report submitted successfully!"})

@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out.")
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
