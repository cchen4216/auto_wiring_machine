
import time 
import tkinter as tk 
from tkinter import ttk 
from tkinter import Menu
from tkinter import messagebox as mbox 
from tkinter import filedialog as fdial 
from queue import Queue 

from Machine import Machine 
# from Connector import Connector 
from SerialPort import SerialPort  
from Gcoder import Gcoder   

class MainApp(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self)
        master.geometry(set_size(master, 520, 450))
        master.resizable(False, True)
        master.title("自动布线机 v1.0")

        self.machine = Machine() 
        self.gcoder = Gcoder() 
        self.serialPort = SerialPort()  # Initialized when the connector opened 
        

def set_size(win, w=0, h=0, absolute=True, win_ratio=None):
    winw = win.winfo_screenwidth() 
    winh = win.winfo_screenheight()
    if not absolute:
        w = int(winw * win_ratio)
        h = int(winh * win_ratio)
        screen = "{0}x{1}+{2}+{3}".format(w, h, int(winw * 0.1), int(winh * 0.05))
    else:
        screen = "{0}x{1}+{2}+{3}".format(w, h, int((winw-w)/2), int((winh-h)/2))
    return screen


##############################################
#                Program Entry 
##############################################
root = tk.Tk() 
app = MainApp(root)
# root.mainloop() 

if app.serialPort.openPort():
    print("Port opened")

app.gcoder.readFile('./test.gcode') 

# time.sleep(5) 
# while app.serialPort.status == 'Run':
#     time.sleep(1)
for i in range(30):
    print(app.serialPort.status)
    time.sleep(2)

app.serialPort.closePort() 

if app.serialPort.isOpen == False: 
    print("Port closed") 



