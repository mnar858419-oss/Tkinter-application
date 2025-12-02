import tkinter as tk
from tkinter import messagebox
from auth import login_user

def open_login(switch_to_register, switch_to_dashboard):
    window = tk.Tk()
    window.title("Login")
    window.geometry("300x200")

    tk.Label(window, text="Username:").pack(pady=5)
    username_entry = tk.Entry(window)
    username_entry.pack(pady=5)

    tk.Label(window, text="Password:").pack(pady=5)
    password_entry = tk.Entry(window, show="*")
    password_entry.pack(pady=5)

    def attempt_login():
        username = username_entry.get()
        password = password_entry.get()
        success, role = login_user(username, password)
        if success:
            messagebox.showinfo("Success", f"Welcome, {username}!")
            window.destroy()
            switch_to_dashboard(username, role)
        else:
            messagebox.showerror("Error", "Invalid username or password.")

    tk.Button(window, text="Login", command=attempt_login).pack(pady=10)
    tk.Button(window, text="Register", command=lambda: [window.destroy(), switch_to_register()]).pack()

    window.mainloop()
