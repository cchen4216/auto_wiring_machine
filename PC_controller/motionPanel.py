from tkinter import ttk 

class MotionPanel:
    def __init__(self, master):
        self.master = master 
        self.motionPanel = ttk.LabelFrame(self.master, text=" 运动状态 ")
        self.motionPanel.grid(row=2, pady=4, sticky='NEW') 

        ttk.Label(self.motionPanel,text="位置",width=12).grid(row=0, column=1,sticky='NEWS')
        ttk.Label(self.motionPanel,text="速度",width=12).grid(row=0, column=2,sticky='NEWS')
        ttk.Label(self.motionPanel,text='X',width=4).grid(row=1, column=0,sticky='NEWS')
        ttk.Label(self.motionPanel,text='Y',width=4).grid(row=2, column=0,sticky='NEWS')
        ttk.Label(self.motionPanel,text="Z",width=4).grid(row=3, column=0,sticky='NEWS')

        ttk.Label(self.motionPanel,text='0'+' mm').grid(row=1, column=1,sticky='NEWS')
        ttk.Label(self.motionPanel,text='0'+' mm/s').grid(row=1,column=2,sticky='NEWS')
        ttk.Label(self.motionPanel,text='0'+' mm').grid(row=2, column=1,sticky='NEWS')
        ttk.Label(self.motionPanel,text='0'+' mm/s').grid(row=2,column=2,sticky='NEWS')
        ttk.Label(self.motionPanel,text='0'+' mm').grid(row=3, column=1,sticky='NEWS')
        ttk.Label(self.motionPanel,text='0'+' mm/s').grid(row=3,column=2,sticky='NEWS')
        

