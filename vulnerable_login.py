import sqlite3

def login_user(username, password):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    # Flaw: String formatting introduces SQL Injection risk
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    return cursor.fetchone()