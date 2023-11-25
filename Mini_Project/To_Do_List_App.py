from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox


def add_item():
    task_value = task_entry.get()
    if len(task_value) == 0:
        messagebox.showinfo('Error', 'Task is not entered.')
    else:
        task.append(task_value)
        task_list.delete(0, 'end')
        for x in task:
            task_list.insert('end', x)
        task_entry.delete(0, 'end')


def view_task():
    try:
        selected_task = task_list.get(task_list.curselection())
        if selected_task:
            messagebox.showinfo('Task Details', f'Task: {selected_task}')
    except TclError:
        messagebox.showinfo('Error', 'No Task Selected.')
        

def edit_task():
    try:
        selected_task_index = task_list.curselection()
        if selected_task_index:
            selected_task_index = selected_task_index[0]
            selected_task = task_list.get(selected_task_index)
            edited_task = simpledialog.askstring('Edit Task', 'Edit Task:', initialvalue=selected_task)
            if edited_task is not None:
                task[selected_task_index] = edited_task
                task_list.delete(0, 'end')
                for x in task:
                    task_list.insert('end', x)
        else:
            messagebox.showinfo('Error', 'No Task Selected.')
    except TclError:
        messagebox.showinfo('Error', 'No Task Selected.')


def delete_item():
    try:
        the_value = task_list.get(task_list.curselection())
        if the_value in task:
            message = messagebox.askyesno('Delete All', 'Are you sure?')
            if message is True:
                task.remove(the_value)
                task_list.delete(0, 'end')
                for x in task:
                    task_list.insert('end', x)
    except:
        messagebox.showinfo('Error', 'No Task Selected.')


def clear_item():
    if len(task) != 0:
        message = messagebox.askyesno('Delete All', 'Are you sure?')
        while len(task) != 0:
            if message is True:
                task.pop()
                task_list.delete(0, 'end')
                for x in task:
                    task_list.insert('end', x)
    else:
        messagebox.showinfo('Error', 'No Task Found')


if __name__ == "__main__":
    root = Tk()
    root.geometry("657x500")
    root.title("To Do List")
    root.minsize(350, 400)
    root.maxsize(800, 600)
    root.configure(bg="white")
    img = PhotoImage(file="E:\python\icon.png")
    root.iconphoto(False,img)

    task = []

    header_frame = Frame(root, bg="cyan")
    list_frame = Frame(root, bg="sky blue")
    button_frame = Frame(root, bg="light green")

    header_frame.pack(side="top", fill="both", pady=20)
    list_frame.pack(side="left", expand=True, fill="both")
    button_frame.pack(side="right", expand=True, fill="both")

    header = Label(header_frame, text="To Do List", bg="white", font=("Helvetica", "25", "bold"))

    task_list = Listbox(list_frame, width=30, height=15, selectmode='SINGLE', selectbackground="blue", selectforeground="white")

    item_label = Label(button_frame, text="Enter Tasks", bg="light green", font=("Arial", "15", "bold"))

    task_entry = Entry(button_frame, font=("Consolas", "12"), width=18)

    add_button = Button(button_frame, text="Add Task", width=20, bg="blue", fg="white", font=("arial", "10", "bold"), command=add_item)
    
    view_button = Button(button_frame, text="View Task", width=20, bg="blue", fg="white", font=("arial", "10", "bold"), command=view_task)
    
    edit_button = Button(button_frame, text="Edit Task", width=20, bg="blue", fg="white", font=("arial", "10", "bold"), command=edit_task)

    delete_button = Button(button_frame, text="Delete Task", width=20, bg="blue", fg="white", font=("arial", "10", "bold"), command=delete_item)

    clear_button = Button(button_frame, text="Delete All Task", width=20, bg="blue", fg="white", font=("arial", "10", "bold"), command=clear_item)

    exit_button = Button(button_frame, text="Exit", width=20, bg="red", fg="white", font=("arial", "10", "bold"), command=root.destroy)

    header.pack()
    task_list.pack(pady=10)
    item_label.pack()
    task_entry.pack(pady=10)
    add_button.pack(pady=10)
    view_button.pack(pady=10)
    edit_button.pack(pady=10)
    delete_button.pack(pady=10)
    clear_button.pack(pady=10)
    exit_button.pack(pady=10)

    root.mainloop()
