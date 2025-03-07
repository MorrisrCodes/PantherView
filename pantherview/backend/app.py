from flask import Flask, send_from_directory

app = Flask(__name__, static_folder="static", static_url_path="/")

# Route for serving the React app
@app.route('/')
@app.route('/<path:path>')
def serve_react(path="index.html"):
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    app.run(debug=True)