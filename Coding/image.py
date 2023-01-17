from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
root = Tk()
root.geometry("500x500")
def Open():
    root.filename = filedialog.askopenfilename(initialdir = "Desktop\Python", title = "Open Image", filetypes = (("png file","*.png"),("all files","*.*")))
    global myimage
    myimage = ImageTk.PhotoImage(Image.open(root.filename))
    imagelabel = Label(root, image = myimage)
    imagelabel.pack()

b1 = Button(root, text = "Open Image", command = Open)
b1.pack()




root.mainloop()