import tkinter as tk
from tkinter import simpledialog, messagebox

tasks = ["Go to gym"]

def refresh_tasks():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

def add_task():
    task = simpledialog.askstring("Lisa ülesanne", "Sisesta ülesanne:")
    if task:
        tasks.append(task)
        refresh_tasks()

def delete_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        task = tasks.pop(index)
        refresh_tasks()
        messagebox.showinfo("Kustutatud", f"Ülesanne \"{task}\" kustutatud.")
    else:
        messagebox.showwarning("Valik puudub", "Palun vali ülesanne kustutamiseks.")

def update_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        old_task = tasks[index]
        new_task = simpledialog.askstring("Uuenda ülesanne", f"Uus tekst ülesandele:\n\"{old_task}\"")
        if new_task:
            tasks[index] = new_task
            refresh_tasks()
    else:
        messagebox.showwarning("Valik puudub", "Palun vali ülesanne uuendamiseks.")

# --- GUI setup ---
root = tk.Tk()
root.title("Ülesannete nimekiri")

listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)
refresh_tasks()

btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

tk.Button(btn_frame, text="➕ Lisa", width=12, command=add_task).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="✏️ Uuenda", width=12, command=update_task).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="❌ Kustuta", width=12, command=delete_task).grid(row=0, column=2, padx=5)

root.mainloop()
