import tkinter as tk
from datetime import datetime
from database import (
    get_user_info,
    add_note_for_user,
    get_notes_for_user,
    get_all_users,
    delete_user,
    update_user_role
)

def open_dashboard(username, role):

    user_id, role, created_at = get_user_info(username)

    window = tk.Tk()
    window.title("Dashboard")
    window.geometry("700x500")

    tk.Label(window, text=f"Welcome, {username}", font=("Arial", 14)).pack()
    tk.Label(window, text=f"Role: {role}").pack()
    tk.Label(window, text=f"Created: {created_at}").pack()


    if role == "admin":
        tk.Button(
            window,
            text="Open Admin Panel",
            bg="#444",
            fg="white",
            command=lambda: open_admin_panel(window)
        ).pack(pady=10)


    notes_frame = tk.Frame(window)
    notes_frame.pack(pady=20)

    tk.Label(notes_frame, text="Your Notes:").pack()

    notes_list = tk.Listbox(notes_frame, width=70)
    notes_list.pack()

    for n in get_notes_for_user(user_id):
        notes_list.insert(tk.END, f"{n[2][:19]}: {n[1]}")

    entry = tk.Entry(notes_frame, width=50)
    entry.pack()

    def add_note():
        text = entry.get()
        if text.strip():
            add_note_for_user(user_id, text)
            notes_list.insert(tk.END, f"{datetime.now().isoformat()[:19]}: {text}")
            entry.delete(0, tk.END)

    tk.Button(notes_frame, text="Add Note", command=add_note).pack(pady=5)

    window.mainloop()



def open_admin_panel(parent):
    admin = tk.Toplevel(parent)
    admin.title("Admin Panel")
    admin.geometry("600x400")

    tk.Label(admin, text="User Management Panel", font=("Arial", 14)).pack(pady=10)

    user_list = tk.Listbox(admin, width=60)
    user_list.pack()

    def load_users():
        user_list.delete(0, tk.END)
        for u in get_all_users():
            user_list.insert(tk.END, f"ID={u[0]} | {u[1]} | role={u[2]} | created={u[3][:10]}")

    load_users()

    tk.Label(admin, text="User ID:").pack(pady=5)
    user_id_entry = tk.Entry(admin)
    user_id_entry.pack()

    def remove_user():
        uid = user_id_entry.get().strip()
        if uid.isdigit():
            delete_user(int(uid))
            load_users()

    tk.Button(admin, text="Delete User", bg="red", fg="white", command=remove_user).pack(pady=5)

    tk.Label(admin, text="New Role (admin/user):").pack()
    new_role_entry = tk.Entry(admin)
    new_role_entry.pack()

    def update_role():
        uid = user_id_entry.get().strip()
        new_role = new_role_entry.get().strip()

        if uid.isdigit() and new_role in ("admin", "user"):
            update_user_role(int(uid), new_role)
            load_users()

    tk.Button(admin, text="Update Role", command=update_role).pack(pady=5)
