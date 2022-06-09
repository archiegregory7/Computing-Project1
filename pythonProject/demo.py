from tkinter import *
import time


class AppWindow:

    def __init__(self, master):
        self.master = master

        # create a toplevel menu
        menubar = Menu(self.master)

        # create a pulldown menu
        main_menu = Menu(menubar, tearoff=0)
        # add a command to the pulldown
        main_menu.add_command(label="Exit", command=root.quit)
        # add the pulldown to the menu bar
        menubar.add_cascade(label="Menu", menu=main_menu)

        menubar.add_command(label="Start", command=self.start)
        menubar.add_command(label="Stop", command=self.stop)

        # display the menu
        self.master.config(menu=menubar)

        # frame for the text widget
        frame = Frame(self.master)
        frame.pack(fill=BOTH, expand=1)

        # text widget and scrollbar
        self.text_widget = Text(frame)
        self.text_widget.config(state=DISABLED)

        scroll_bar = Scrollbar(frame)
        scroll_bar.pack(side=RIGHT, fill=Y, expand=1)
        self.text_widget.pack(fill=BOTH, expand=1, side=RIGHT)

        self.text_widget.configure(yscrollcommand=scroll_bar.set)
        scroll_bar.config(command=self.text_widget.yview)
        self.stop = True
        self.last_time = time.time()

    def print_text(self, string):
        self.text_widget.config(state=NORMAL)
        self.text_widget.insert(END, string + "\n")
        self.text_widget.yview("moveto", 1.0)
        self.text_widget.config(state=DISABLED)

    def update_text(self):
        now = time.time()
        self.print_text("%.2f" % ((now - self.last_time) * 1000))
        self.last_time = now

        if self.stop == False:
            self.master.after(25, self.update_text)

    def stop(self):
        self.stop = True

    def start(self):
        if self.stop == True:
            self.stop = False
            self.last_time = time.time()
            self.master.after(25, self.update_text)


root = Tk()
root.geometry("%dx%d%+d%+d" % (600, 400, 0, 0))
root.title(string="Test")
window = AppWindow(root)

root.mainloop()