from tkinter import *
import os #operating system
from tkinter.messagebox import *
from tkinter.filedialog import *
import tkinter

class Notepad:
    __root = Tk()
    __thiswidth = 400
    __thisheight = 600
    __thistextarea = Text(__root)
    __thismenubar = Menu(__root)
    __thisfilemenu = Menu(__thismenubar)
    __thiseditmenu = Menu(__thismenubar)
    __thishelpmenu = Menu(__thismenubar)
   # __thisscrolbar = Scrollbar(__thistextarea)
    __file = None
    def __init__(self, **kwargs):
        try:
            self.__thiswidth = kwargs["width"]
        except KeyError:
            pass
        try:
            self.__thisheight = kwargs["height"]
        except KeyError:
            pass
        
        self.__root.title("Untitled - Notepad")
        # centre the window exactly
        screenwidth = self.__root.winfo_screenwidth()
        screenheight = self.__root.winfo_screenheight()
        # for left alligning
        left = (screenwidth/2)-(self.__thiswidth/2)
        # for top
        top = (screenheight/2)-(self.__thisheight/2)
        # setting geometry
        self.__root.geometry("%dx%d+%d+%d"%(self.__thiswidth,self.__thisheight,left,top))
        # %d is a placeholder which returns the number
        self.__root.grid_rowconfigure(0)
        self.__root.grid_columnconfigure(0)
        self.__thistextarea.grid(sticky = N+E+S+W)
        self.__thisfilemenu.add_command(label = "New", command = self.__newfile)
        self.__thisfilemenu.add_command(label = "Open File", command = self.__openfile)
        self.__thisfilemenu.add_command(label = "Save File", command = self.__savefile)
        self.__thisfilemenu.add_command(label = "Exit", command = self.__exitfile)
        self.__thismenubar.add_cascade(label = "File", menu = self.__thisfilemenu)
        self.__thismenubar.add_cascade(label = "Edit", menu = self.__thiseditmenu)
        self.__thiseditmenu.add_command(label = "Copy", command = self.__copy)
        self.__thiseditmenu.add_command(label = "Paste", command = self.__paste)
        self.__thiseditmenu.add_command(label = "Cut", command = self.__cut)
        self.__thishelpmenu.add_cascade(label = "Help", menu = self.__thishelpmenu)
        self.__thishelpmenu.add_command(label = "About Notepad", command = self.__showabout)
        self.__root.config(menu = self.__thismenubar)
        #self.__thisscrolbar.config(command = self.__thistextarea.yview)
        #self.__thistextarea.config(yscrollcommand=self.__thisscrolbar.set)
    def __showabout(self):
        showinfo("This notepad was created by Angela on 2nd February. There are several options for\
            you like saving, cutting ,pasting ,etc.")
        
    def __exitfile(self):
        self.__root.destroy()
        
    def __cut(self):
        self.__thistextarea.event_generate("<<Cut>>")
        
    def __copy(self):
        self.__thistextarea.event_generate("<<Copy>>")
        
    def __paste(self):
        self.__thistextarea.event_generate("<<Paste>>")
        
    def __newfile(self):
        self.__root.title("Untitled Notepad")
        self.__file = None
        self.__thistextarea.delete(1.0,END)
        
    def __openfile(self):
        self.__file = askopenfilename(defaultextension= ".txt", filetypes= [("all files","*.*"),("text documents","*.txt")])
        if self.__file == "":
            self.__file = None
        else:
            self.__root.title(os.path.basename(self.__file) + "- Notepad")
            self.__thistextarea.delete(1.0,END)
            file = open(self.__file,"r")
            self.__thistextarea.insert(1.0,file.read())
            file.close()
    def __savefile(self):
        if self.__file == None:  
            self.__file= asksaveasfilename(initialfile = "Untitled.txt",defaultextension = ".txt", filetypes = [("allfiles","*.*"),("text documents","*.txt")])
            if self.__file == "":
                self.__file = None
            else:
                file = open(self.__file,"w")
                file.write(self.__thistextarea.get(1.0,END))
                file.close()
                self.__root.title(os.path.basename(self.__file) + "-Notepad")
        else:
            file = open(self.__file, "W")
            file.write(self.__thistextarea.get(1.0,END))
            file.close()
                            
                
                
            

            
            
    def Run(self):
        self.__root.mainloop()
        
n = Notepad(width = 600, height = 400)
n.Run()




        
    
        
    
        
        
        

    
        

        
    
        
        
    
        


            
            

    

    
    
    
    

