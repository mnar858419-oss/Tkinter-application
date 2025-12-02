from database import create_connection
from utils import hash_password, check_password
from datetime import datetime

def register_user(username: str, password: str, role="user"):
    conn = create_connection()
    cursor = conn.cursor()
    password_hashed = hash_password(password)
    try:
        cursor.execute(
            "INSERT INTO users (username, password_hash, role, created_at) VALUES (?, ?, ?, ?)",
            (username, password_hashed, role, datetime.now().isoformat())
        )
        conn.commit()
        print("User registered successfully!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()

def login_user(username: str, password: str):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT password_hash, role FROM users WHERE username = ?", (username,))
    row = cursor.fetchone()
    conn.close()
    if row:
        password_hashed, role = row
        if check_password(password, password_hashed):
            print(f"Login successful! Role: {role}")
            return True, role
    print("Invalid username or password.")
    return False, None
