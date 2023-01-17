from Tkinter import *
root = Tk()
root.geometry("500x500")
l1 = Label(root, text = "What are your hobbies ?")
l1.pack()


c1 = IntVar() # binary number 0 or 1
c2 = IntVar()
c3 = IntVar()
b1 = Checkbutton(root,text = "Cycling", variable = c1 , onvalue = 1, offvalue = 0, height = 3, width = 6)
b1.pack()
b2 = Checkbutton(root, text = "Reading", varaible = c2, onvalue = 1, offvalue = 0, height = 3, width = 6)
b2.pack()
b3 = Checkbutton(root, text = "Swimming", variable = c3, onvalue = 1, offvalue = 0, height = 3, width = 6)
b3.pack()




root.mainloop()