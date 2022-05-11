#Creating the Login Screen using TKINTER
from tkinter import *


def Main():

    form = Tk()
    form.title("Main Menu")
    form.geometry("440x200")

    signLabel = Label(form, text="Please enter a username and password")
    signLabel.config(font=("courier", 14))
    signLabel.grid(row=0, column=0, columnspan=3, sticky="W", padx=10, pady=10)

    userEntry = Entry(form, width="30")
    userEntry.grid(row=2, column=1, padx=10, pady=10, sticky="E")
    userLabel = Label(form, text="Username")
    userLabel.grid(row=2, column=0, padx=10, pady=10, sticky="E")

    passEntry = Entry(form, width="30")
    passEntry.grid(row=3, column=1, padx=10, pady=10, sticky="E")
    passLabel = Label(form, text="Password")
    passLabel.grid(row=3, column=0, padx=10, pady=10, sticky="E")



    exitButton = Button(form, text="Exit", width=12,bg="blue", command=quit)
    exitButton.grid(row=5, column=0, padx=10, pady=10)

    logButton = Button(form, text="Log In", width=12,bg="red" )
    logButton.grid(row=5, column=1, padx=10, pady=10)


    mainloop()




if __name__ == "__main__":
    Main()


