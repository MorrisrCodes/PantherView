from flask import Flask, render_template, request, jsonify, g 
import sqlite3
import os

def create_app():
    app = Flask(__name__, static_folder="static")

def get_db_connection():
    conn = sqlite3.connect('login_db.db')
    conn.row_factory = sqlite3.Row
    return conn

    with app.app_context():
        init_db()

    @app.route("/")
    def index():
        return render_template("buildings.html")
    
    @app.route("/get_alerts", methods=["GET"])
    def get_alerts():
        db = get_db()
        try:
            cursor = db.execute('SELECT * FROM alerts ORDER BY created_at DESC')
            alerts = [dict(row) for row in cursor.fetchall()]
            return jsonify(alerts)
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        finally:
            db.close()
    

    @app.route("/report_issue", methods=["POST"])
    def report_issue():
        data = request.get_json()
        db = get_db()
        
        try:
            # Insert into issues table
            db.execute('''
                INSERT INTO issues (location, issue_type, description)
                VALUES (?, ?, ?)
            ''', [data['location'], data['issue_type'], data.get('description', '')])
            
            # Create corresponding alert
            db.execute('''
                INSERT INTO alerts (location, message, alert_type)
                VALUES (?, ?, ?)
            ''', [
                data['location'],
                f"Issue reported at {data['location']}: {data['issue_type']}",
                "issue"
            ])
            
            db.commit()
            return jsonify({"message": "Issue reported successfully"}), 201
        except Exception as e:
            db.rollback()
            return jsonify({"error": str(e)}), 500
        finally:
            db.close()
        


    @app.route("/report_event", methods=["POST"])
    def report_event():
        data = request.get_json()
        db = get_db()
        
        try:
            # Insert into events table
            db.execute('''
                INSERT INTO events (location, event_type, description)
                VALUES (?, ?, ?)
            ''', [data['location'], data['event_type'], data.get('description', '')])
            
            # Create corresponding alert
            db.execute('''
                INSERT INTO alerts (location, message, alert_type)
                VALUES (?, ?, ?)
            ''', [
                data['location'],
                f"Event scheduled at {data['location']}: {data['event_type']}",
                "event"
            ])
            
            db.commit()
            return jsonify({"message": "Event reported successfully"}), 201
        except Exception as e:
            db.rollback()
            return jsonify({"error": str(e)}), 500
        finally:
            db.close()

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=2244, threaded=True)