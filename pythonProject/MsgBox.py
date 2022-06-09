from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo



def show_info_Message(myMessage,root):

    messagebox.showinfo(message = myMessage, parent = root)

    root.destroy()

    root.mainloop()


def show_error_Message(myMessage):
    root = Tk()
    messagebox.showerror(message = myMessage, parent = root)

    root.destroy()

    root.mainloop()

def show_warning_Message(myMessage):
    root = Tk()
    messagebox.showwarning(message = myMessage, parent = root)

    root.destroy()

    root.mainloop()
    root.mainloop()



def combo():
    app = tk.Tk()
    app.geometry('300x200')

    labelTop = Label(app,text="Main Menu")
    labelTop.grid(column=0, row=0)

    comboExample = ttk.Combobox(app,
                                values=[
                                    "Available Bookings",
                                    "Edit Booking Time",
                                    "Cancel Booking",
                                    "Enquire"])

    comboExample.grid(column=0, row=1)
    comboExample.current(1)


    app.mainloop()

def notebook():
    root = tk.Tk()
    root.geometry('400x300')
    root.title('Notebook Demo')

    # create a notebook
    notebook = ttk.Notebook(root)
    notebook.pack(pady=10, expand=True)

    # create frames
    frame1 = ttk.Frame(notebook, width=400, height=280)
    frame2 = ttk.Frame(notebook, width=400, height=280)

    frame1.pack(fill='both', expand=True)
    frame2.pack(fill='both', expand=True)

    # add frames to notebook

    notebook.add(frame1, text='General Information')
    notebook.add(frame2, text='Profile')

    root.mainloop()

def menu():
    root = tk.Tk()
    root.title('Menu Demo')

    # create a menubar
    menubar = Menu(root)
    root.config(menu=menubar)

    # create a menu
    file_menu = Menu(menubar)

    # add a menu item to the menu
    file_menu.add_command(label='Exit',command=root.destroy)

    # add the File menu to the menubar
    menubar.add_cascade(label="File",menu=file_menu)

    root.mainloop()