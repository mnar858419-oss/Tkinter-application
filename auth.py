from database import create_connection
from utils import hash_password, check_password
from datetime import datetime

def register_user(username, password, role="user"):
    conn = create_connection()
    cursor = conn.cursor()
    password_hash = hash_password(password)

    cursor.execute("""
        INSERT INTO users (username, password_hash, role, created_at)
        VALUES (?, ?, ?, ?)
    """, (username, password_hash, role, datetime.now().isoformat()))

    conn.commit()
    conn.close()

def login_user(username, password):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT password_hash, role FROM users WHERE username = ?", (username,))
    row = cursor.fetchone()
    conn.close()

    if row:
        password_hash, role = row
        if check_password(password, password_hash):
            return True, role

    return False, None
