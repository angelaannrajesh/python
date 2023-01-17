from tkinter import *
import PIL
from PIL import ImageTk,Image
root = Tk()
root.geometry("500x500")
image1 = ImageTk.PhotoImage(Image.open("dog_picture.png"))
l1 = Label(image = image1)
l1.pack()

root.mainloop()