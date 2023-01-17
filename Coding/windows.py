from tkinter import *
root = Tk()

def Open():
    l1 = Label(root, text = "Top Window")
    top = Toplevel()
    top.geometry("500x500")
    b1 = Button(top, text = "close window", command = top.destroy)
    b1.pack()
    l1.pack()
root.geometry("500x500")
b2 = Button(root, text = "open second window", command = Open)
b2.pack()






root.mainloop()