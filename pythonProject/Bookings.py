from tkinter import *
from tkcalendar import *

def calendar():
    screen = Tk()
    screen.minsize(800,600)
    screen.title("Available dates")
    screen.configure(background= "black")

    myCal = Calendar(screen, setmde = 'day', date_pattern='d/m/yy')
    myCal.place(x= 350, y=100)

    openCal = Button(screen, text = "Select Date", command = selectDate)
    openCal.place(x = 425, y = 300)


    screen.mainloop()


def selectDate():
    pass

calendar()