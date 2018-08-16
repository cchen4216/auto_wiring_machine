import tkinter as tk 
from tkinter import ttk 
from tkinter import scrolledtext

class CodePanel:
    def __init__(self, master):
        self.master = master 
        self.codePanel = ttk.Frame(master)
        master.add(self.codePanel, text="G-Code 编辑器")

        self.codeEntry = scrolledtext.ScrolledText(self.codePanel, width=100, height=40)
        # self.codeEntry = scrolledtext.ScrolledText(self.codePanel)
        self.codeEntry.grid(row=0,column=0,sticky="NEWS")