import sqlite3

# Define database name
DB_NAME = 'devices.db'

# Function to create the table
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
        print("Database initialized.")

# Function to insert a device
def insert_device(name, type, notes):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute(
            "INSERT INTO devices (name, type, notes) VALUES (?, ?, ?)",
            (name, type, notes)
        )
        print(f"Inserted: {name}")

# Function to fetch all devices
def get_devices():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.execute("SELECT * FROM devices")
        for row in cursor:
            print(row)

if __name__ == '__main__':
    init_db()
    insert_device("MacBook Pro", "Laptop", "Primary work device")
    insert_device("iPhone 14", "Phone", "Used for device testing")
    get_devices()
