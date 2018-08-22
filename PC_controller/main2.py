import os, sys 
import tkinter as tk 
from tkinter import ttk 
from tkinter import Menu 
from tkinter import messagebox as mbox 
from tkinter import filedialog as fdial 
from tkinter import scrolledtext as tkst

class MainFrame(tk.Frame):
    def __init__(self, master):
        pass 


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path).replace("\\", "/")

root = tk.Tk() 
app = MainFrame(root) 
try: 
    root.iconbitmap(default=resource_path('app.ico'))
except BaseException:
    pass 

root.mainloop() 
