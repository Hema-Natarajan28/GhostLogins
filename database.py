import sqlite3
DB_NAME = "ghostlogin.db"
def get_connection():
    return sqlite3.connect(DB_NAME)
def initialize_database():
    connection = get_connection()
    connection.execute("""
        CREATE TABLE IF NOT EXISTS login_events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            timestamp TEXT NOT NULL,
            success INTEGER NOT NULL,
            ip_address TEXT,
            location TEXT,
            risk_score INTEGER DEFAULT 0,
            risk_level TEXT DEFAULT 'LOW',
            reasons TEXT DEFAULT ''
        )
    """)
    connection.commit()
    connection.close()
def save_login(event, analysis):
    connection = get_connection()
    connection.execute("""
        INSERT INTO login_events (
            username, timestamp, success, ip_address,
            location, risk_score, risk_level, reasons
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        event["username"],
        event["timestamp"],
        int(event["success"]),
        event.get("ip_address", ""),
        event.get("location", ""),
        analysis["risk_score"],
        analysis["risk_level"],
        ", ".join(analysis["reasons"])
    ))
    connection.commit()
    connection.close()
def get_all_logins():
    connection = get_connection()
    connection.row_factory = sqlite3.Row
    rows = connection.execute("""
        SELECT * FROM login_events
        ORDER BY id DESC
    """).fetchall()
    connection.close()
    return [dict(row) for row in rows]