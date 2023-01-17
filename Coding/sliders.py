from tkinter import *
root = Tk()
root.geometry("500x500")
v1 =  DoubleVar()
def Show1():
    scl = "The horizontel scale value is " + str(v1.get())
    l1.configure(text = scl)
s1 = Scale(root, variable = v1, from_= 1,to= 200, orient = HORIZONTAL)
b1 = Button(root, text = "Display", command= Show1)
b1.pack()
s1.pack()
l1 = Label(root)
l1.pack() 


root.mainloop()