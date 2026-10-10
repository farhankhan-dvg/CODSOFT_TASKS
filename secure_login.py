import sqlite3
import hashlib

def secure_login_user(username, password):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    # Remediations: SHA-256 hash and parameterized queries
    hashed_pw = hashlib.sha256(password.encode()).hexdigest()
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    cursor.execute(query, (username, hashed_pw))
    return cursor.fetchone()