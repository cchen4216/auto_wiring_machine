# from tkinter import Tk, Label, Button, Entry, IntVar, END

# class Calculator:
#     def __init__(self, master):
#         self.master = master 
#         master.title("Calculator")

#         self.total = 0 
#         self.entered_number = 0 

#         self.total_label_text = IntVar() 
#         self.total_label_text.set(self.total)
#         self.total_label = Label(master, textvariable=self.total_label_text)

#         self.label = Label(master, text="Total:")

#         vcmd = master.register(self.validate)
#         self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))

#         self.add_btn = Button(master, text="+", width=4, command=lambda: self.update("add"))
#         self.subtract_btn = Button(master, text="-", width=4, command=lambda: self.update("subtract"))
#         self.reset_btn = Button(master, text="Reset", command=lambda: self.update("reset"))

#         # LAYOUT 
#         self.label.grid(row=0, column=0, sticky='W') 
#         self.total_label.grid(row=0, column=1, columnspan=2, sticky='E')

#         self.entry.grid(row=1, column=0, columnspan=3, sticky='WE')

#         self.add_btn.grid(row=2, column=0) 
#         self.subtract_btn.grid(row=2, column=1) 
#         self.reset_btn.grid(row=2, column=2, sticky='WE')

#     def validate(self, new_text):
#         if not new_text:  # the fielf is being cleared
#             self.entered_number = 0 
#             return True 

#             try: 
#                 self.entered_number = int(new_text) 
#                 return True 
#             except ValueError:
#                 return False 
    
#     def update(self, method):
#         if method == "add":
#             self.total += self.entered_number 
#         elif method == "subtract":
#             self.total -= self.entered_number 
#         else: # reset 
#             self.total = 0 

#         self.total_label_text.set(self.total)
#         self.entry.delete(0, END)

# root = Tk() 
# my_gui = Calculator(root)
# root.mainloop() 

###########################################################################################
from tkinter import *  
from PIL import ImageTk,Image  
root = Tk()  
canvas = Canvas(root, width = 300, height = 300)  
canvas.pack()  
img = ImageTk.PhotoImage(Image.open("./images/logo.png"))  
canvas.create_image(20, 20, anchor=NW, image=img)  
root.mainloop()  