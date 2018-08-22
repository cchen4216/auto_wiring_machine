import tkinter as tk 
from tkinter import ttk 
from tkinter import messagebox as mBox

try:
	from serial.tools.list_ports import comports
except:
    pass 
	# from lib.serial import comports

from lib.sender import Sender#, NOT_CONNECTED, STATECOLOR, STATECOLORDEF


class ConnectPanel:
    def __init__(self, master):
        self.master = master 
        self.connectPanel = ttk.LabelFrame(self.master, text=" 设备连接 ")
        self.connectPanel.grid(row=1, sticky='NEWS')
        ttk.Label(self.connectPanel, text="状态: ").grid(row=0,column=0,sticky='E')
        ttk.Label(self.connectPanel, text="端口: ").grid(row=1,column=0,sticky='E')
        ttk.Label(self.connectPanel, text="波特率: ").grid(row=2,column=0,sticky='E')
        
        self.stateLabel = ttk.Label(self.connectPanel,text="已断开",foreground='darkred')
        self.stateLabel.grid(row=0,column=1,sticky='E')

        self.portVar = tk.StringVar() 
        self.portCombo = ttk.Combobox(self.connectPanel,width=14, textvariable=self.portVar, state='readonly')
        self.getSerialPorts()
        self.portCombo.grid(row=1, column=1)
        # self.portCombo.bind("<<ComboboxSelected>>", self.getSerialPorts)
        # 我希望每次点击下拉列表的时候，都能够更新端口列表

        self.baudVar = tk.IntVar() 
        baudCombo = ttk.Combobox(self.connectPanel, width=14, textvariable=self.baudVar, state='readonly')
        baudCombo['values'] = (2400, 4800, 9600, 19200, 38400, 57600, 115200, 230400)
        baudCombo.grid(row=2, column=1)
        baudCombo.current(6)

        self.connectBTN = ttk.Button(self.connectPanel, text="连接", command=self.openClose)
        self.connectBTN.grid(row=0,column=2,rowspan=3,sticky='NEWS')

        self.serial = None 

    def getSerialPorts(self):
        devices = sorted([x[0] for x in comports()])
        self.portCombo['values'] = devices
        # print(len(devices),'\n', devices)
        self.portCombo.current(len(devices)-1)
        
    
    def openClose(self):
        if self.serial is not None:
            self.close() 
            self.connectBTN.configure(text="连接")
            self.stateLabel.configure(text="已断开",foreground='darkred')
        else:
            device = self.portVar.get() 
            baudrate = self.baudVar.get()
            if self.open(device, baudrate):
                self.connectBTN.configure(text="断开")
                self.stateLabel.configure(text="已连接",foreground='darkgreen')
                # self.enable() ##############################
    def open(self, device, baudrate):
        try:
            return Sender.open(self, device, baudrate)
        except:
            self.serial = None 
            self.thread = None 
            mBox.showerror("连接错误", "串口连接失败！")

        return False 
    def close(self):
        Sender.close(self)
        # try:
        #     self.dro.updateState() 
        # except TclError:
        #     pass 