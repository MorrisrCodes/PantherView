from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__, static_folder="static")

def get_db():
    conn = sqlite3.connect("login_db.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    return render_template("buildings.html")

@app.route("/get_alerts", methods=["GET"])
def get_alerts():
    db = get_db()
    try:
        cursor = db.execute("SELECT timestamp, type FROM alerts ORDER BY timestamp DESC LIMIT 10")
        alerts = [
            {
                "message": row["type"],
                "timestamp": row["timestamp"]
            } for row in cursor.fetchall()
        ]
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
        db.execute("""
            INSERT INTO alerts (time_alive, timestamp, type)
            VALUES (?, ?, ?)
        """, [
            "24h",
            datetime.now().isoformat(),
            f"issue:{data['issue_type']}:{data['location']}"
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
        db.execute("""
            INSERT INTO alerts (time_alive, timestamp, type)
            VALUES (?, ?, ?)
        """, [
            "24h",
            datetime.now().isoformat(),
            f"event:{data['event_type']}:{data['location']}"
        ])
        db.commit()
        return jsonify({"message": "Event reported successfully"}), 201
    except Exception as e:
        db.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        db.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=2244)
