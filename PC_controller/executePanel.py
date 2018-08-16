import tkinter as tk 
from tkinter import ttk 

class ExecutePanel:
    def __init__(self, master, app):
        self.master = master 
        self.executePanel = ttk.LabelFrame(self.master, text=" 脚本执行 ")
        self.executePanel.grid(row=4, pady=4, sticky='NEWS')

        self.stepBTN = ttk.Button(self.executePanel,text='单步\n执行',width=4)
        self.stepBTN.grid(row=0,column=0,sticky='W')
        self.startBTN = ttk.Button(self.executePanel, text='全部\n执行',width=4,command=app.cbExecuteAll)
        self.startBTN.grid(row=0,column=1,sticky='W')
        self.pauseResumeBTN = ttk.Button(self.executePanel, text='暂停',width=4)
        self.pauseResumeBTN.grid(row=0,column=2,sticky='W')
        self.stopBTN = ttk.Button(self.executePanel, text="停止", width=4)
        self.stopBTN.grid(row=0, column=3,sticky='W')


        