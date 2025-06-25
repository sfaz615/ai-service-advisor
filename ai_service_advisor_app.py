from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DB_NAME = 'devices.db'

# Create table if not exists
def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS devices (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                type TEXT,
                notes TEXT
            );
        ''')

@app.route('/add_device', methods=['POST'])
def add_device():
    data = request.json
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO devices (name, type, notes) VALUES (?, ?, ?)",
                       (data['name'], data.get('type', ''), data.get('notes', '')))
        conn.commit()
    return jsonify({'status': 'success'}), 200

@app.route('/get_devices', methods=['GET'])
def get_devices():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM devices")
        rows = cursor.fetchall()
    return jsonify(rows), 200

@app.route("/")
def home():
    return "Device Bot API is live! Use /add_device or /get_devices"

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
