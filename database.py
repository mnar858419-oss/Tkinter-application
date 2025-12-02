import sqlite3
from datetime import datetime

DB_NAME = "app.db"

def create_connection():
    return sqlite3.connect(DB_NAME)

def create_tables():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            role TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def create_notes_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            content TEXT NOT NULL,
            created_at TEXT NOT NULL,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    """)
    conn.commit()
    conn.close()

def get_user_info(username):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, role, created_at FROM users WHERE username = ?", (username,))
    row = cursor.fetchone()
    conn.close()
    return row  # (id, role, created_at)

def delete_user(user_id):
    """حذف کامل کاربر از دیتابیس"""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()


def update_user_role(user_id, new_role):
    """تغییر نقش کاربر: admin / user"""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET role = ? WHERE id = ?", (new_role, user_id))
    conn.commit()
    conn.close()


def get_all_users():
    """دریافت لیست همه کاربرها (فقط برای پنل ادمین)"""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, username, role, created_at FROM users")
    rows = cursor.fetchall()
    conn.close()
    return rows

def add_note_for_user(user_id, content):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO notes (user_id, content, created_at) VALUES (?, ?, ?)",
        (user_id, content, datetime.now().isoformat())
    )
    conn.commit()
    conn.close()

def get_notes_for_user(user_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, content, created_at FROM notes WHERE user_id = ?", (user_id,))
    rows = cursor.fetchall()
    conn.close()
    return rows

if __name__ == "__main__":
    create_tables()
    create_notes_table()
