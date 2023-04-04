

import sqlite3
from tkinter import messagebox
from tkinter import *
#connecting to the data base(DB)
root=Tk()
connection=sqlite3.connect("mystudentt.db")
crsr=connection.cursor()
#command to creat a table
sqlcommand="""CREATE TABLE if not exists students(
Roll_Number INTEGER,
First_Name CHAR(24),
Last_Name CHAR(24),
Grade INTEGER,
myaddress CHAR(5),
hobbies CHAR(10));"""

crsr.execute(sqlcommand)

connection.commit()
connection.close()
def submit():
    connection=sqlite3.connect("mystudentt.db")
    crsr=connection.cursor()
    #insert data into table
    crsr.execute("INSERT INTO students VALUES(:R_Number,:F_Name,:L_Name,:Grad,:my_adress,:myhobbies)",
        {
            'R_Number':R_Number.get(),
            'F_Name':F_Name.get(),
            'L_Name':L_Name.get(),
            'Grad':Grad.get(),
            'my_adress':my_adress.get(),
            'myhobbies':myhobbies.get()
        }
    )
    
    connection.commit()
    connection.close()
    #clear textboxes
    R_Number.delete(0,END)
    F_Name.delete(0,END)
    L_Name.delete(0,END)
    Grad.delete(0,END)
    my_adress.delete(0,END)
    myhobbies.delete(0,END)

def Show_Data():
    connection=sqlite3.connect("mystudentt.db")
    crsr=connection.cursor()
    crsr.execute("SELECT *, Roll_Number FROM students")
    ans=crsr.fetchall()
    records=" "
    for record in ans:
        records+=str(record[0]) + " " + record[1] + " " + record[2] + " " + str(record[3]) + " " + record[4] + " " + record[5] + "\n"
        
    Label(root,text = records, bg = "yellow").grid(row = 16,columnspan = 2)
    
def Delete_Data():
    connection = sqlite3.connect("mystudentt.db")
    crsr = connection.cursor()
    crsr.execute("DELETE FROM students WHERE Roll_Number = "+deli.get())
    deli.delete(0,END)
    connection.commit()
    connection.close()

def Edit():
    connection = sqlite3.connect("mystudentt.db")
    crsr = connection.cursor()
    crsr.execute("""UPDATE students SET 
                 Roll_Number = :R_Number,
                 First_Name = :F_Name,
                 Last_Name = :L_Name,
                 Grade = :Grad,
                 myaddress = :my_adress,
                 hobbies = :myhobbies
                 WHERE Roll_Number = :eid""",
                    {
                        'R_Number':rnumber_edit.get(),
                        'F_Name':fname_edit.get(),
                        'L_Name':lname_edit.get(),
                        'Grad':grade_edit.get(),
                        'my_adress':my_address_edit.get(),
                        'myhobbies':myhobbies_edit.get(),
                        'eid':edit.get()
                    })
    connection.commit()
    connection.close()

def Update():
    up = Tk()
    connection = sqlite3.connect("mystudentt.db")
    crsr = connection.cursor()
    record_id = edit.get()
    crsr.execute("SELECT * FROM students WHERE Roll_Number = " + record_id)
    records = crsr.fetchall()
    global rnumber_edit
    rnumber_edit = Entry(up,width = 30)
    rnumber_edit.grid(row = 0,column = 1)
    global fname_edit
    fname_edit = Entry(up,width = 30)
    fname_edit.grid(row = 1,column = 1)
    global lname_edit
    lname_edit = Entry(up,width = 30)
    lname_edit.grid(row = 2, column = 1)
    global grade_edit
    grade_edit = Entry(up,width = 30)
    grade_edit.grid(row = 3, column = 1)
    global my_address_edit
    my_address_edit = Entry(up,width = 30)
    my_address_edit.grid(row = 4, column = 1)
    global myhobbies_edit
    myhobbies_edit = Entry(up,width = 30)
    myhobbies_edit.grid(row = 5, column = 1)
    roll_number_edit_label = Label(up,text = "please enter roll number")
    roll_number_edit_label.grid(row = 0, column = 0)
    first_name_edit_label = Label(up, text ="please enter first name")
    first_name_edit_label.grid(row = 1, column = 0 )
    last_name_edit_label = Label(up, text = "please enter last name")
    last_name_edit_label.grid(row = 2, column = 0)
    grade_edit_label = Label(up, text = "please enter grade")
    grade_edit_label.grid(row = 3, column = 0)
    address_edit_label = Label(up, text = "please enter address")
    address_edit_label.grid(row = 4, column = 0)
    hobby_edit_label = Label(up, text = "please enter your hobby")
    hobby_edit_label.grid(row = 5, column = 0)
    for record in records :
        rnumber_edit.insert(0,record[0])
        fname_edit.insert(0,record[1])
        lname_edit.insert(0, record[2])
        grade_edit.insert(0,record[3])
        my_address_edit.insert(0,record[4])
        myhobbies_edit.insert(0,record[5])
    messagebox.askyesno(title="Save Changes")
    
    Button(up,text = "Save Changes",command = Edit).grid(row = 6,column = 0)
    Button(up,text = "Exit",command = up.destroy).grid(row = 6, column = 1)
    connection.commit()
    connection.close()
    
    
    
    
    
root=Tk()
R_Number=Entry(root,width=30)
R_Number.grid(row=1,column=1,padx=20)
F_Name=Entry(root,width=30)
F_Name.grid(row=2,column=1,padx=20)
L_Name=Entry(root,width=30)
L_Name.grid(row=3,column=1,padx=20)
Grad=Entry(root,width=30)
Grad.grid(row=4,column=1,padx=20)
my_adress=Entry(root,width=30)
my_adress.grid(row=5,column=1,padx=20)
myhobbies=Entry(root,width=30)
myhobbies.grid(row=6,column=1,padx=20)
deli = Entry(root, width = 30)
deli.grid(row = 7, column = 1, padx = 20)
edit = Entry(root,width = 30)
edit.grid(row = 8, column = 1,padx = 20)


#creating labels
Roll_Number_label=Label(root,text="Enter your roll number")
Roll_Number_label.grid(row=1,column=0)
First_Name_label=Label(root,text="Enter your First name")
First_Name_label.grid(row=2,column=0)
Last_Name_label=Label(root,text="Enter your Last name")
Last_Name_label.grid(row=3,column=0)
Grade_label=Label(root,text="Enter your grade")
Grade_label.grid(row=4,column=0)
my_adress_label=Label(root,text="Enter your adress")
my_adress_label.grid(row=5,column=0)
myhobbies_label=Label(root,text="Enter your hobbies")
myhobbies_label.grid(row=6,column=0)
deli_label = Label(root, text = "Enter the ID you want to delete")
deli_label.grid(row = 7,column = 0)
edit_label = Label(root, text = "Redo")
edit_label.grid(row = 8, column = 0)

b1=Button(root,command=submit,text="submit")
b1.grid(row=9,columnspan=2,padx=25,pady=10,ipadx=100)
b2=Button(root, text = "show data",command = Show_Data)
b2.grid(row = 10, columnspan = 2,ipadx = 100)
b3 = Button(root, command = Delete_Data, text = "delete data")
b3.grid(row = 13,columnspan = 2,ipadx = 100)
b4 = Button(root, text = "edit data",command = Update)
b4.grid(row = 14, columnspan = 2,ipadx = 100)


root.mainloop()


