#
# Inspired by the tutorial found at: https://www.geeksforgeeks.org/python-askopenfile-function-in-tkinter/
#

from tkinter import * 
from tkinter.ttk import *

from tkinter.filedialog import askopenfile 
  
root = Tk() 
root.geometry('200x100') 
  
# Open a file dialog 
# Only Python (.py) files will be shown
# Open the selected file in read mode and print its contents
def open_file(): 
    file = askopenfile(mode ='r', filetypes =[('Python Files', '*.py')]) 
    if file is not None: 
        content = file.read() 
        print(content) 
  
btn = Button(root, text ='Open a Python file', command = lambda:open_file()) 
btn.pack(side = TOP, pady = 10)

mainloop() 