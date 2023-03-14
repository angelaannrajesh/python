from tkinter import *
root = Tk()
root.geometry("500x500")
def Select():
    if v.get() == "Pepperoni":
        mylabel = Label(root, text = "You want Pepperoni")
    else:
        mylabel = Label(root, text = "You don't want Pepperoni")
    mylabel = Label(root,text = v.get())
    mylabel.pack()

v = StringVar()
checkbutton1 = Checkbutton(root, text = "Pepperoni", variable = v , onvalue =  "Pepperoni", offvalue = "No Pepperoni")
checkbutton1.deselect()
checkbutton1.pack()
b1 = Button(root, text = "choose", command = Select)
b1.pack()

root.mainloop()
