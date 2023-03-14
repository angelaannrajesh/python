from openpyxl import *
from tkinter import *
wb = load_workbook("Documents:\\invoice.xlsx") 
sheet = wb.active
if __name__ == "__main__":
    root = Tk()
root.configure(background="green")
root.title("mydata")
root.geometry(width = 8, height = 5)

root.mainloop()
    
