import tkinter as tk
from tkinter import messagebox
from auth import register_user

def open_register(switch_to_login):
    window = tk.Tk()
    window.title("Register")
    window.geometry("300x200")

    tk.Label(window, text="Username:").pack(pady=5)
    username_entry = tk.Entry(window)
    username_entry.pack(pady=5)

    tk.Label(window, text="Password:").pack(pady=5)
    password_entry = tk.Entry(window, show="*")
    password_entry.pack(pady=5)

    def attempt_register():
        username = username_entry.get()
        password = password_entry.get()
        register_user(username, password)
        messagebox.showinfo("Success", "User registered!")
        window.destroy()
        switch_to_login()

    tk.Button(window, text="Register", command=attempt_register).pack(pady=10)
    tk.Button(window, text="Back to Login", command=lambda: [window.destroy(), switch_to_login()]).pack()

    window.mainloop()
