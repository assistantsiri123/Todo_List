from tkinter import *

def add_task():
    task = entry.get()
    if task:
        listbox.insert(END, task)
        entry.delete(0, END)

def delete_task():
    selected_task = listbox.curselection()
    if selected_task:
        listbox.delete(selected_task)

# Creating the main window
window = Tk()
window.title("Task List")

# Entry widget for adding tasks
entry = Entry(window, width=30)
entry.pack(pady=10)

# Button to add tasks
add_button = Button(window, text="Add Task", command=add_task)
add_button.pack()

# Listbox to display tasks
listbox = Listbox(window, selectmode=SINGLE)
listbox.pack(pady=10)

# Button to delete selected task
delete_button = Button(window, text="Delete Task", command=delete_task)
delete_button.pack()

# Running the main loop
window.mainloop()
