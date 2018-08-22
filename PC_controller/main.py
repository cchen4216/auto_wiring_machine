import tkinter as tk 
from tkinter import ttk 
from tkinter import Frame

from menuBar import CMenuBar 
from adPanel import AdPanel
from connectPanel import ConnectPanel
from motionPanel import MotionPanel
from controlPanel import ControlPanel
from codePanel import CodePanel 
from canvasPanel import CanvasPanel
from executePanel import ExecutePanel
from infoPanel import InfoPanel 
from lib.sender import Sender


class MainGUI:
    def __init__(self, master): 
        self.master = master
        master.title("自动布线机")

        # add menubar on the GUI
        self.menuBar = CMenuBar(master)
        
        # Add two pane on the GUI
        self.leftPanel = Frame(master)
        self.leftPanel.grid(row=0, column=0, sticky='NEWS')
        self.rightPanel = Frame(master)
        self.rightPanel.grid(row=0, column=1, sticky='NEWS')

        self.adPanel = AdPanel(self.leftPanel)
        self.connectPanel = ConnectPanel(self.leftPanel)
        self.motionPanel = MotionPanel(self.leftPanel)
        self.controlPanel = ControlPanel(self.leftPanel)
        self.executePanel = ExecutePanel(self.leftPanel, self)
        self.infoPanel = InfoPanel(self.leftPanel)
    
        self.rightTabs = ttk.Notebook(self.rightPanel)
        self.rightTabs.grid(row=0,column=0,sticky="NEWS")
        self.canvasPanel = CanvasPanel(self.rightTabs)
        self.codePanel = CodePanel(self.rightTabs)

        self.sender = Sender() 
    
    def cbExecuteAll(self):
        self.gcode = self.codePanel.codeEntry.get("1.0", "end-1c").split('\n')
        print(self.gcode) 
        print(type(self.gcode))
        

if __name__ == "__main__":
    global mainFrame 
    root = tk.Tk()
    root.resizable(width=False, height=False) 
    mainFrame = MainGUI(root) 
    root.mainloop() 

