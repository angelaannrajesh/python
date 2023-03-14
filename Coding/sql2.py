import sqlite3
from tkinter import *
root=Tk()
connection=sqlite3.connect("contactDB")
crsr=connection.cursor()

sqlcommand="""CREATE TABLE if not exists contact(
ID_Number INTEGER,
Phone_Number INTEGER,
First_Name CHAR(24),
Last_Name CHAR(24),
Age INTEGER,
Address CHAR(5));"""




crsr.execute(sqlcommand)

connection.commit()
connection.close()



root.mainloop()