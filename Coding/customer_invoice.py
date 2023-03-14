from tkinter import *
from openpyxl import *

wb = load_workbook("Documents:\\invoice.xlsx")
sheet = wb.active
def excel():
    sheet.cell(row = 1, column = 1).value = "Angela"
    wb.save("Documents:\\invoice.xlsx")
excel()

    
    
    
