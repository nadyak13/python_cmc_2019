from tkinter import *
from tkinter import ttk

def exit(*args):
    sys.exit(0)

def print_hello(*args):
    text.set("Hello!")

def print_bye(*args):
    text.set("Bye!")

root = Tk()
root.title("Window with one button")

mainframe = ttk.Frame(root, padding="10 10 30 30")
mainframe.grid(column=0, row=0)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

text = StringVar()

ttk.Label(mainframe, textvariable=text).grid(column=0, row=1)

ttk.Button(mainframe, text="Exit", command=exit).grid(column=0, row=2)
ttk.Button(mainframe, text="Hello!", command=print_hello).grid(column=0, row=0)
ttk.Button(mainframe, text="Bye!", command=print_bye).grid(column=1, row=0)



for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.mainloop()
