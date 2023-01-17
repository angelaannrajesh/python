from tkinter import *
root = Tk()
root.geometry("500x500")
v1 = DoubleVar

def Show1():
    sel = "The verticle scale value is " + str(v1.get())
    l1.configure(text = sel, font = ("Italic",14))

s1 = Scale(root, variable = v1, from_ = 1, to = 100,orient = VERTICAL)
l3 = Label(root, text = "Vertical Scaler")
b1 = Button(root, text = "Display Horizontal", command = Show1 ,bg = "purple")

l1 = Label(root)
s1.pack(anchor = CENTER)
l3.pack()
b1.pack(anchor = CENTER)
l1.pack()

root.mainloop()

