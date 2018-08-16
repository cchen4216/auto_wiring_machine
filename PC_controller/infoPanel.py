import tkinter as tk 
from tkinter import ttk 
from tkinter import scrolledtext 

class InfoPanel:
    def __init__(self, master):
        self.master = master
        self.infoPanel = ttk.LabelFrame(master, text=" 日志信息 ")
        self.infoPanel.grid(row=5, column=0, sticky="NEWS") 

        # self.messageStr = tk.StringVar() 
        # self.messageStr.set("Ready...")
        self.message = scrolledtext.ScrolledText(self.infoPanel, width=37, heigh=8, wrap=tk.WORD,state='disabled')
        self.message.grid(row=0, column=0, sticky='NEWS')
        # self.message = tk.Message(self.infoPanel, textvariable=self.messageStr, width=250, height=40)
        # self.message.grid(row=0, column=0, sticky="EW")

        self.versionLabel = ttk.Label(self.infoPanel, text='版本号：0.01')
        self.versionLabel.grid(row=6,column=0,sticky='NEWS')