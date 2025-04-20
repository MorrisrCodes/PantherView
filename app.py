from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def entry():
    return render_template("entrypage/EntryPage.html")

@app.route("/login")
def login():
    return render_template("loginpage/LoginPage-inlineCss.html")

@app.route("/signup")
def signup():
    return "<h1>Signup Page Coming Soon!</h1>"

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
