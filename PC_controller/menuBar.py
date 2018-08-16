from tkinter import Menu 

class CMenuBar:
    def __init__(self, master):
        self.master = master 
        self.menuBar = Menu(master)
        master.config(menu=self.menuBar)
        
        self.fileMenu = Menu(self.menuBar, tearoff=0)
        self.fileMenu.add_command(label="新建脚本")
        self.fileMenu.add_command(label="导入脚本")
        self.fileMenu.add_command(label="基本设置")
        self.fileMenu.add_separator() 
        self.fileMenu.add_command(label="退出", command=self.exitApp)
        self.menuBar.add_cascade(label="文件", menu=self.fileMenu)
        
        self.editMenu = Menu(self.menuBar, tearoff=0)
        self.editMenu.add_command(label="重复")
        self.editMenu.add_command(label="撤销")
        self.menuBar.add_cascade(label="编辑", menu=self.editMenu)

        self.controlMenu = Menu(self.menuBar, tearoff=0)
        self.controlMenu.add_command(label="连接设备")
        self.controlMenu.add_command(label="断开连接")
        self.controlMenu.add_separator()
        self.controlMenu.add_command(label="执行脚本")
        self.controlMenu.add_command(label="暂停执行")
        self.controlMenu.add_command(label="终止执行")
        self.menuBar.add_cascade(label="控制", menu=self.controlMenu)

        self.helpMenu = Menu(self.menuBar, tearoff=0)
        self.helpMenu.add_command(label="文档")
        self.helpMenu.add_command(label="关于")
        self.menuBar.add_cascade(label="帮助", menu=self.helpMenu)

    def exitApp(self):
        # 做一些清理工作, 如断开串口
        self.master.quit()


