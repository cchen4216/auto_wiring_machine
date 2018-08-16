import tkinter as tk 
from tkinter import ttk 

class CanvasPanel:
    def __init__(self, master):
        self.master = master 
        self.canvasPanel = ttk.Frame(master)
        master.add(self.canvasPanel, text="运动监视器")

        self.canvas = tk.Canvas(self.canvasPanel, width=720, heigh=614, bg='lightblue')
        # self.canvas = tk.Canvas(self.canvasPanel, bg='lightblue')
        self.canvas.grid(row=0, column=0, sticky="EW")
        