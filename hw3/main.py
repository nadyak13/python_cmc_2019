from tkinter import *
from tkinter import ttk

def exit(*args):
    sys.exit(0)

root = Tk()
root.title("Window with one button")

mainframe = ttk.Frame(root, padding="10 10 30 30")
mainframe.grid(column=0, row=0)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Button(mainframe, text="Exit", command=exit).grid(column=0, row=0)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.mainloop()
