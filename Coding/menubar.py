from tkinter import *
root = Tk()
root.geometry("500x500")

f1 = Frame(root, width = 6 , height = 5 ,relief = SUNKEN)
f1.pack(side = LEFT)
b1 = Button(root, text = "Maths")
b1.pack()



root.mainloop()