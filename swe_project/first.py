from flask import Flask, render_template, request, jsonify, g 
import sqlite3
import os

def create_app():
    app = Flask(__name__, static_folder="static")

    DATABASE = "login_db.db"

    def connect_db():
        return sqlite3.connect(DATABASE)
    
    def get_db():
        db = getattr(g, "_database", None)
        if db is None:
            db = g._database = connect_db()
            db.row_factory = sqlite3.Row
        return db
    
    @app.teardown_appcontext
    def close_db(exception):
        db = getattr(g, "_database", None)
        if db is not None:
            db.close()

    def init_db():
        db = get_db()
        with app.app_context():
            try:
                # Create users table
                db.execute('''
                    CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                ''')

                # Create alerts table with more comprehensive fields
                db.execute('''
                    CREATE TABLE IF NOT EXISTS alerts (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        location TEXT NOT NULL,
                        message TEXT NOT NULL,
                        alert_type TEXT NOT NULL,
                        user_id INTEGER,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        FOREIGN KEY(user_id) REFERENCES users(id)
                    )
                ''')

                # Create posts table
                db.execute('''
                    CREATE TABLE IF NOT EXISTS posts (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        content TEXT NOT NULL,
                        user_id INTEGER,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        FOREIGN KEY(user_id) REFERENCES users(id)
                    )
                ''')

                # Create buildings table with coordinates
                db.execute('''
                    CREATE TABLE IF NOT EXISTS buildings (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL UNIQUE,
                        longitude REAL NOT NULL,
                        latitude REAL NOT NULL,
                        description TEXT
                    )
                ''')

                # Create issues table
                db.execute('''
                    CREATE TABLE IF NOT EXISTS issues (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        building_id INTEGER,
                        issue_type TEXT NOT NULL,
                        description TEXT,
                        status TEXT DEFAULT 'reported',
                        user_id INTEGER,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        FOREIGN KEY(building_id) REFERENCES buildings(id),
                        FOREIGN KEY(user_id) REFERENCES users(id)
                    )
                ''')

                # Create events table
                db.execute('''
                    CREATE TABLE IF NOT EXISTS events (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        location TEXT NOT NULL,
                        event_type TEXT NOT NULL,
                        description TEXT,
                        user_id INTEGER,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        FOREIGN KEY(user_id) REFERENCES users(id)
                    )
                ''')

                db.commit()
                print("Database tables initialized successfully")
            except sqlite3.Error as e:
                print(f"Error initializing database: {str(e)}")
                db.rollback()
            finally:
                db.close()
        

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