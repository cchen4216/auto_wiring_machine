import tkinter as tk 
from tkinter import ttk 
from PIL import ImageTk, Image

class AdPanel:
    def __init__(self, master):
        self.master = master 
        self.adPanel = ttk.LabelFrame(self.master)
        self.adPanel.grid(row=0, sticky='WE') 

        # self.canvas = tk.Canvas(self.adPanel, width=277, heigh=100)
        self.canvas = tk.Canvas(self.adPanel, height=100)
        # self.canvas.grid(row=0, column=0, sticky="NEWS")
        
        self.img = ImageTk.PhotoImage(Image.open("./images/logo.png"))
        self.canvas.create_image(140, 50, image=self.img)
        # self.canvas.create_text(40, 20, text="航天极创")
        # coord = 10, 50, 240, 210
        # arc = self.canvas.create_arc(coord, start=0, extent=150, fill="red")
        self.canvas.grid(row=0, column=0, sticky='NEWS') 

