from os import kill

import tkinter as tk
from tkinter import *

def drop_down_menu():
    root = Tk()
    root.geometry("300x300")

    mb = Menubutton(root, text="This is Admin Menu")
    mb.menu = Menu(mb)
    mb["menu"] = mb.menu

    mb.menu.add_command(label="Bookings", command=lambda: Bookings(root))
    mb.menu.add_command(label="Availability", command=lambda: Availability())
    mb.menu.add_command(label="Exit", command=quit)
    mb.pack()
    root.mainloop()





def Bookings(win):
    import Bookings
    print(Bookings.Calendar())
    win.destroy()






def Availability():
    print("Availability will show")