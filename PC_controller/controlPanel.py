import tkinter as tk 
from tkinter import ttk 

class ControlPanel:
    def __init__(self, master):
        self.master = master
        self.controlPanel = ttk.LabelFrame(self.master, text=" 手动控制 ")
        self.controlPanel.grid(row=3, sticky='NEW') 

        ttk.Label(self.controlPanel,text="X").grid(row=0, column=0,sticky='NEWS')
        ttk.Button(self.controlPanel,text="复位",width=3).grid(row=0, column=1, sticky="NEWS")
        ttk.Button(self.controlPanel,text="-",width=1).grid(row=0, column=2, sticky="NEWS")
        ttk.Button(self.controlPanel,text="+",width=1).grid(row=0, column=3, sticky="NEWS")
        ttk.Label(self.controlPanel,text="步长:").grid(row=0, column=4,sticky='NEWS')
        self.stepX = tk.IntVar() 
        self.stepX.set(1)
        ttk.Entry(self.controlPanel,textvariable=self.stepX,width=4).grid(row=0,column=5,sticky="NEWS")
        ttk.Label(self.controlPanel,text="mm").grid(row=0, column=6,sticky='NEWS')

        ttk.Label(self.controlPanel,text="Y").grid(row=1, column=0,sticky='NEWS')
        ttk.Button(self.controlPanel,text="复位",width=3).grid(row=1, column=1, sticky="NEWS")
        ttk.Button(self.controlPanel,text="-",width=1).grid(row=1, column=2, sticky="NEWS")
        ttk.Button(self.controlPanel,text="+",width=1).grid(row=1, column=3, sticky="NEWS")
        ttk.Label(self.controlPanel,text="步长:").grid(row=1, column=4,sticky='NEWS')
        self.stepY = tk.IntVar() 
        self.stepY.set(1)
        ttk.Entry(self.controlPanel,textvariable=self.stepY,width=4).grid(row=1,column=5,sticky="NEWS")
        ttk.Label(self.controlPanel,text="mm").grid(row=1, column=6,sticky='NEWS')

        ttk.Label(self.controlPanel,text="Z").grid(row=2, column=0,sticky='NEWS')
        ttk.Button(self.controlPanel,text="复位",width=3).grid(row=2, column=1, sticky="NEWS")
        ttk.Button(self.controlPanel,text="-",width=1).grid(row=2, column=2, sticky="NEWS")
        ttk.Button(self.controlPanel,text="+",width=1).grid(row=2, column=3, sticky="NEWS")
        ttk.Label(self.controlPanel,text="步长:").grid(row=2, column=4,sticky='NEWS')
        self.stepZ = tk.IntVar()
        self.stepZ.set(1)  
        ttk.Entry(self.controlPanel,textvariable=self.stepZ,width=4).grid(row=2,column=5,sticky="NEWS")
        ttk.Label(self.controlPanel,text="mm").grid(row=2, column=6,sticky='NEWS')
        