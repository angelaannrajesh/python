from tkinter import *
root = Tk()
root.geometry("500x500")
var = StringVar(root)
var.set("Monday")
option = OptionMenu(root, var, "Tuesday", "Wendnesday", "Thursday", "Friday","Saturday", "Sunday")
option.pack()
def Select():
    print("You have selected",var.get())
    root.quit()
b1 = Button(root, command = Select, text = "Choose")
b1.pack()



root.mainloop()

from tkinter import *
root = Tk()
root.geometry("500x500")
l1 = Label(root, text = "What are your hobbies ?")
l1.pack()

checkbutton1 = IntVar() # binary number 0 or 1
checkbutton2 = IntVar()
checkbutton3 = IntVar()
b1 = Checkbutton(root,text = "Cycling", variable = checkbutton1 , onvalue = 1, offvalue = 0, height = 3, width = 6)
b2 = Checkbutton(root, text = "Reading", variable = checkbutton2, onvalue = 1, offvalue = 0, height = 3, width = 6)
b3 = Checkbutton(root, text = "Swimming", variable = checkbutton3, onvalue = 1, offvalue = 0, height = 3, width = 6)
b1.pack()
b2.pack()
b3.pack()

root.mainloop()