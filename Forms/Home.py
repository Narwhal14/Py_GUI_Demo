import tkinter
from tkinter.ttk import Label


class MyFirstGUI:
    LABEL_TEXT = [
        "This is our first GUI!",
        "Actually, this is our second GUI.",
        "We made it more interesting...",
        "..by making this label interactive.",
    ]

    def __init__(self, master):
        self.master = master
        master.title("a simple GUI")

        self.label_index = 0
        self.label_text = tkinter.StringVar()
        self.label_text.set(self.LABEL_TEXT[self.label_index])
        self.label = Label(master, textvariable=(self.label_text))
        self.label.bind("<Button-1>", self.cycle_label_text)
        self.label.grid(columnspan=2, sticky=W)

        self.greet_button = tkinter.Button(master, text="Greet", command=self.greet)
        self.greet_button.grid(row=1)

        self.close_button = tkinter.Button(master, text="close", command=master.quit)
        self.close_button.grid(row=1, column=1)

    def greet(selfself):
        print("greetings")

    def cycle_label_text(self,event):
        self.label_index += 1
        self.label_index %= len(self.LABEL_TEXT)
        self.label_text.set(self.LABEL_TEXT[self.label_index])