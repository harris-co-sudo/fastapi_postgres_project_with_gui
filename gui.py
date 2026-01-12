import tkinter as tk
from tkinter import messagebox
import requests

API_URL = "http://13.220.93.41:8000/users/"

def add_user():
    name = entry_name.get()
    email = entry_email.get()
    if not name or not email:
        messagebox.showwarning("Input Error", "Name and Email are required")
        return

    payload = {"name": name, "email": email}
    try:
        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            messagebox.showinfo("Success", f"User added! ID: {response.json()['id']}")
            entry_name.delete(0, tk.END)
            entry_email.delete(0, tk.END)
            load_users()  # refresh list
        else:
            messagebox.showerror("Error", response.json().get("detail", "Failed to add user"))
    except Exception as e:
        messagebox.showerror("Error", str(e))

def load_users():
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            users_listbox.delete(0, tk.END)
            for user in response.json():
                users_listbox.insert(tk.END, f"{user['id']}: {user['name']} ({user['email']})")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# -------- GUI Layout --------
root = tk.Tk()
root.title("User Management")

tk.Label(root, text="Name").grid(row=0, column=0, padx=5, pady=5)
tk.Label(root, text="Email").grid(row=1, column=0, padx=5, pady=5)

entry_name = tk.Entry(root)
entry_email = tk.Entry(root)

entry_name.grid(row=0, column=1, padx=5, pady=5)
entry_email.grid(row=1, column=1, padx=5, pady=5)

btn_add = tk.Button(root, text="Add User", command=add_user)
btn_add.grid(row=2, column=0, columnspan=2, pady=5)

users_listbox = tk.Listbox(root, width=50)
users_listbox.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

btn_refresh = tk.Button(root, text="Show Users", command=load_users)
btn_refresh.grid(row=4, column=0, columnspan=2, pady=5)

# Load users on startup
load_users()

root.mainloop()
