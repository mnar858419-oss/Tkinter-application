import tkinter as tk
from database import create_connection

def get_user_info(username):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT role, created_at FROM users WHERE username = ?", (username,))
    row = cursor.fetchone()
    conn.close()
    if row:
        role, created_at = row
        return role, created_at
    return None, None

def open_dashboard(username, role):
    role, created_at = get_user_info(username)
    
    window = tk.Tk()
    window.title(f"Dashboard - {username}")
    window.geometry("500x400")

    tk.Label(window, text=f"Welcome, {username}!").pack(pady=5)
    tk.Label(window, text=f"Role: {role}").pack(pady=5)
    tk.Label(window, text=f"Account created at: {created_at}").pack(pady=5)

    # نمونه پنل‌ها
    panel_frame = tk.Frame(window)
    panel_frame.pack(pady=20)

    tk.Label(panel_frame, text="Panel 1: Notes").grid(row=0, column=0, padx=10, pady=10)
    tk.Label(panel_frame, text="Panel 2: Tasks").grid(row=0, column=1, padx=10, pady=10)
    tk.Label(panel_frame, text="Panel 3: Settings").grid(row=0, column=2, padx=10, pady=10)

    # اگر کاربر admin است، دکمه مدیریت کاربران نمایش داده شود
    if role == "admin":
        tk.Button(window, text="Manage Users", command=lambda: tk.messagebox.showinfo("Admin", "Admin panel")).pack(pady=10)

    window.mainloop()
