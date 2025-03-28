from flask import Flask, render_template, request, jsonify

def create_app():
    app = Flask(__name__, static_folder="static")

    @app.route("/")
    def index():
        return render_template("buildings.html")

    @app.route("/create_post", methods=["POST"])
    def create_post():
        data = request.get_json()
        # Process the data and create the post
        return jsonify({"message": "Post created successfully"}), 201

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", debug=True, port=2244, threaded=True)