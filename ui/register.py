import tkinter as tk
from tkinter import messagebox
from auth import register_user

def open_register(switch_to_login):
    window = tk.Tk()
    window.title("Register")
    window.geometry("300x200")

    tk.Label(window, text="Username").pack()
    username_entry = tk.Entry(window)
    username_entry.pack()

    tk.Label(window, text="Password").pack()
    password_entry = tk.Entry(window, show="*")
    password_entry.pack()

    def attempt():
        register_user(username_entry.get(), password_entry.get())
        messagebox.showinfo("Success", "Registered!")
        window.destroy()
        switch_to_login()

    tk.Button(window, text="Register", command=attempt).pack(pady=10)
    tk.Button(window, text="Back to login", command=lambda: [window.destroy(), switch_to_login()]).pack()

    window.mainloop()
