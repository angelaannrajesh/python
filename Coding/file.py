from tkinter import *
from tkinter.filedialog import asksaveasfile
from tkinter import ttk
root = Tk()
root.geometry("500x500")
def Save():
    files = [
        ("All Files", "*.*"),
        ("Python files","*.py"),
        ("test document","*.txt")
    ]
    file = asksaveasfile(filetypes = files, defaultextension = files)
b1 = ttk.Button(root, text = "Save", command = lambda : Save())
b1.pack()




root.mainloop()

