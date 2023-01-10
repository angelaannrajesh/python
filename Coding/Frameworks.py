from Tkinter import *
root = Tk()
root.geometry("400x300")
def Button2():
    print("Grade 1")
def Button3():
    print("Grade 2")
f1 = Frame(root,bg = "red", borderwidth = 8, relief = SUNKEN)
f1.pack(side = LEFT)
l2 = Label(f1,text = "Teachers" )
l2.pack()
l3 = Label(f1, text = "Desk")
l3.pack()
f2 = Frame(root,bg = "green", borderwidth = 7, relief = SUNKEN)
f2.pack(side = RIGHT)
b2 = Button(f2, text = "Row 2",command = Button2)
b2.pack()
b3 = Button(f2, text = "Row 3",command = Button3)
b3.pack()


root.mainloop()