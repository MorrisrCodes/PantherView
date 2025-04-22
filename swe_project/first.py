from flask import Flask, render_template
 
def create_app():
     app = Flask(__name__)
 
 
     @app.route("/")
     def index():
         return render_template("buildings.html")
     
     return app
     
def get_db_connection():
    conn = sqlite3.connect('login_db.db')
    conn.row_factory = sqlite3.Row
    return conn
 
if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", debug=True, port=2244, threaded=True)