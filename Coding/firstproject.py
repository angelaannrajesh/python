from tkinter import *
root = Tk()
root.geometry("400x300")
root.minsize(200,200)
root.maxsize(600,500)
l1 = Label(root,text = "Hello, I am Angela",font=("sans serif",25),bg = "blue",fg = "white",borderwidth = 4,relief= RIDGE)
l1.pack(side = LEFT, padx=50)
b1 = Button(root, text = "Click Me")
b1.pack()



root.mainloop()
