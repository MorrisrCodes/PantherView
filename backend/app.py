from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
import os

# Initialize Flask app and DB
app = Flask(__name__, static_folder="static", static_url_path="/")
app.config['SECRET_KEY'] = 'super-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
admin = Admin(app, name='PantherView Admin', template_mode='bootstrap4')

# 🧠 Example model to manage from the admin panel
class DetectionLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email_text = db.Column(db.Text)
    classification = db.Column(db.String(50))
    confidence = db.Column(db.Float)

# Add model to admin interface
admin.add_view(ModelView(DetectionLog, db.session))


# Serve your React app (if you're using one)
@app.route('/')
@app.route('/<path:path>')
def serve_react(path="index.html"):
    file_path = os.path.join(app.static_folder, path)
    if os.path.exists(file_path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, "index.html")
    
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
