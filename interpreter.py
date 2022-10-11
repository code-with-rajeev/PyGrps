# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 19:01:57 2020

@author: ACER
"""

import time



from tkinter.filedialog import askopenfile
from tkinter import *

from grps import start_GUI as start



root = Tk() 
root.geometry("1000x600") 
root.title(" __Welcome to Grapes__ ")

scrollbar1 = Scrollbar(root)

scrollbar1.pack( side = RIGHT, fill = Y )

result1 = ''
def new_file():
    inputtxt.delete(1.0, END)
def Take_input(file =None,dir_ = None): 
    global result1
    INPUT = inputtxt.get("1.0", "end-1c") 
    output = ""
    START = time.time()
    result,to_print = "",[]
    result1 = ""
    to_print,result = start(dir_ ,file,INPUT)
    END = time.time()
    SPAN = END-START
    print(SPAN)
    if to_print:
        for i in to_print:
            output += i
    result1 = result1 + f"\n{output}\n {result}  {SPAN}  seconds ;)\n"
    result = f"running....  file_name = {file}.grps \nat wdir = {dir_}"
    running.insert(1.0 , result)
    Output.insert(1.0, result1)

    
def open_file():
    filename = askopenfile(
        defaultextension=".grps",
        filetypes=[("All Files", "*.*"),
                   ("Text Files", "*.txt"),
                   ("Python Scripts", "*.py"),
                   ("Markdown Documents", "*.md"),
                   ("JavaScript Files", "*.js"),
                   ("HTML Documents", "*.html"),
                   ("CSS Documents", "*.css")])
    if filename: 
        text = filename.read()
        inputtxt.delete(1.0, END)
        inputtxt.insert(1.0, text)
       # set_window_title(filename)
def save():
    if filename:
        try:
            textarea_content = inputtxt.get(1.0, END)
            with open(filename, "w") as f:
                f.write(textarea_content)
        except Exception as e:
            print(e)
    else:
        save_as()
def save_as():
    file_name = input("Enter the filename  :")
    save()
font_specs = ("ubuntu", 14)

menubar = Menu(root, font=font_specs)
root.config(menu=menubar)
file_dropdown = Menu(menubar, font=font_specs, tearoff=0)
file_dropdown.add_command(label="New File",command = new_file)
file_dropdown.add_command(label="Open File",command = open_file)
file_dropdown.add_command(label="Save",command = save)
file_dropdown.add_command(label="Save As",command = save_as)
file_dropdown.add_command(label="Run")
file_dropdown.add_separator()
file_dropdown.add_command(label="Exit")
menubar.add_cascade(label="File", menu=file_dropdown)
print("      ___Welcome to Grapes____ \n \nIf you are beginer with this language then please read the syntax first")
print("\n 1 : __Example of skipline__ \n use \";\" to skip line\nfor example : x,y = 10,20;  PRINT(x,y)")
print("\n 2 : __Example of comments__ \n code should be in between \"--\" or \"---\"\n for exampe : --single line comment--")
print("\n             ---\n              multiple line comment\n             ---\n")
print("3 : __Example of print__ \n statement should be in between show(  )\n for exampe : PRINT(\"hello\")")
print("\n________Hope you read it carefully_______\n \n \n")

choice = int(input("Enter 1 to continue  :"))
if choice == 1:
    filename = input("Enter the File name to create   :")
    dir_ = __file__
l = Label(text = f"{filename}.grps") 
running = Text(root ,height = 2,
               width = 500,
               bg = "light cyan")
inputtxt = Text(root, height = 25, 
                width = 500, 
                bg = "light yellow",
              yscrollcommand = scrollbar1.set)
Output = Text(root, height = 10,  
              width = 500,  
              bg = "light blue") 
  
Display = Button(root, height = 2, 
                 width = 20,  
                 text ="Run", 
                 command = lambda:Take_input(filename,dir_)) 


l.pack()
scrollbar1.config( command = inputtxt.yview ) 
inputtxt.pack()


Display.pack() 
running.pack()
Output.pack() 
mainloop()
