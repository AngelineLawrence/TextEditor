'''
Created on May 8, 2017

@author: AngelineAlex
'''
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfile
from tkinter.messagebox import showerror
filename = None


def newFile():
    global filename
    filename = "Untitled"
    text.delete(0.0, END)

def saveFile():
    global filename
    t = str(text.get(0.0, END))
    f = open(filename, 'w')
    f.write(t)
    f.close()
    
def saveAs():
    f = asksaveasfile(mode ='w', defaultextension='.txt')
    t = text.get(0.0, END)
    try:
        f.write(t.rstrip())
    except:
        showerror(title="Oops!!", message="Unable to save file...")
        
        
def openFile():
    global filename
    file = askopenfile(parent=root, title='Select a File')
    filename = file.name
    t = file.read()
    text.delete(0.0, END)
    text.insert(0.0, t)
    noteBookTabFunction()
    file.close()
    
def noteBookTabFunction():
    n=ttk.Notebook(root)
    frame1 = ttk.Frame(n)
    n.add(frame1, text = filename)
    
root = Tk() 
root.title("**Text Editor**")
root.minsize(width=800, height=700)
root.maxsize(width=800, height=700)

text = Text(root, width=800, height=700)
text.pack()

menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save As..", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)
root.mainloop()

        
        
        
