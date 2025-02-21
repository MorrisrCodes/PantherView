from flask import Flask, render_template

def create_app():
    app = Flask(__name__, static_folder="static")


    @app.route("/")
    def index():
        return render_template("buildings.html")
    
    return app
    

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", debug=True, port=2244, threaded=True)