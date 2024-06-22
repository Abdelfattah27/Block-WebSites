# @Abdelfattah Hamdi

import os
import re
from urllib.parse import urlparse
import tkinter as tk
from tkinter import messagebox


initial_adult_ones = [
# add here your initial websites
]

def is_valid_hostname(hostname):
    if len(hostname) > 255:
        return False
    if hostname[-1] == ".":
        hostname = hostname[:-1]
    allowed = re.compile(r"(?!-)[A-Z\d-]{1,63}(?<!-)$", re.IGNORECASE)
    return all(allowed.match(x) for x in hostname.split("."))

def add_to_hosts(address, ip_address="192.168.1.1" , initial=False):
    address = address.strip() 
    parsed_url = urlparse(address)
    if parsed_url.scheme and parsed_url.hostname:
        hostname = parsed_url.hostname
    elif is_valid_hostname(address):
        hostname = address
    elif not initial :
        messagebox.showerror("Error", "Bad input. Please enter a valid URL or hostname.")
        return

    hosts_path = ""
    if os.name == 'nt':
        hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
    else:
        hosts_path = "/etc/hosts"

    if not os.path.isfile(hosts_path) and not initial :
        messagebox.showerror("Error", f"Error Happen")
        return

    with open(hosts_path, 'r') as file:
        lines = file.readlines()

    entry_exists = any(f"{ip_address} {hostname}" in line for line in lines)
    if entry_exists :
        if not initial :
            messagebox.showinfo("Info", f"Already Blocked.")
        return
    try: 
        with open(hosts_path, 'a') as file:
            file.write(f"\n{ip_address} {hostname}")
    except : 
        messagebox.showerror("Error", f"Please run the program as administrator")
        
    if not initial :
        messagebox.showinfo("Success",  f"{hostname} has been blocked successfully.")

for web in initial_adult_ones : 
    add_to_hosts(web , initial=True)

def on_submit():
    address = entry.get()
    add_to_hosts(address)

    
    
# Create the main window
root = tk.Tk()
root.title("Block Adult Websites")
root.geometry("400x200")
root.configure(bg="#2c3e50")

# Create and place the label, entry, and button
frame = tk.Frame(root, bg="#34495e", padx=10, pady=10)
frame.pack(pady=20)

tk.Label(frame, text="Enter the URL or hostname:", bg="#34495e", fg="#ecf0f1", font=("Arial", 12)).pack(pady=5)
entry = tk.Entry(frame, width=50, font=("Arial", 12), bg="#ecf0f1", fg="#2c3e50", insertbackground="#2c3e50")
entry.pack(pady=5)
tk.Button(frame, text="Block Website", command=on_submit, bg="#1abc9c", fg="#ecf0f1", font=("Arial", 12), relief="flat").pack(pady=10)

# Run the application
root.mainloop()