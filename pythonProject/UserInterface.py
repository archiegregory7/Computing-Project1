# Creating the Login Screen using TKINTER
from tkinter import *
import MsgBox

def check_pass_and_username(username, password, win):
    import validation

    if validation.is_valid_length(1, username,8) == True and validation.is_valid_length(2,password,8) == True:
        print("user ok")
        #call second form
        win.destroy()
        admin_menu()

    else:
        import MsgBox
        print(MsgBox.show_info_Message("Your password or username is wrong", win))
        Login()


def admin_menu():
    import Admin_Menu
    print(Admin_Menu.drop_down_menu())



def Login():
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

    exitButton = Button(form, text="Exit", width=12, command=quit)
    exitButton.grid(row=5, column=0, padx=10, pady=10)


    logButton = Button(form, text="Log In", width=12,command=lambda: check_pass_and_username(userEntry.get(), passEntry.get(), form))
    logButton.grid(row=5, column=1, padx=10, pady=10)

    mainloop()


if __name__ == "__main__":
    Login()