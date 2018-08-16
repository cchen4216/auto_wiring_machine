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

    #-----------------------------------------------------------------------
	# Send enabled gcode file to the CNC machine
	#-----------------------------------------------------------------------
	def cbExecuteAll(self, lines=None):
		if self.serial is None:
			tkMessageBox.showerror(_("Serial Error"),
				_("Serial is not connected"),
				parent=self)
			return
		# if self.running:
        if False: 
			if self._pause:
				self.resume()
				return
			tkMessageBox.showerror(_("Already running"),
				_("Please stop before"),
				parent=self)
			return

		# self.editor.selectClear()
		# self.selectionChange()
		# CNC.vars["errline"] = ""

		# the buffer of the machine should be empty?
		# self.initRun()
        self.sender.initRun()
		# self.canvas.clearSelection()
		# self._runLines = sys.maxint	# temporary WARNING this value is used
						# by Sender._serialIO to check if we
						# are still sending or we finished
		self._gcount   = 0		# count executed lines
		self._selectI  = 0		# last selection pointer in items
		self._paths    = None		# temporary
		CNC.vars["running"]    = True	# enable running status
		CNC.vars["_OvChanged"] = True	# force a feed change if any
		if self._onStart:
			try:
				os.system(self._onStart)
			except:
				pass

		if lines is None:
			#if not self.gcode.probe.isEmpty() and not self.gcode.probe.zeroed:
			#	tkMessageBox.showerror(_("Probe is not zeroed"),
			#		_("Please ZERO any location of the probe before starting a run"),
			#		parent=self)
			#	return
			self.statusbar.setLimits(0, 9999)
			self.statusbar.setProgress(0,0)

			#class MyQueue:
			#	def put(self,line):
			#		print ">>>",line
			#self._paths = self.gcode.compile(MyQueue(), self.checkStop)
			#return

			self._paths = self.gcode.compile(self.queue, self.checkStop)
			if self._paths is None:
				self.emptyQueue()
				self.purgeController()
				return
			elif not self._paths:
				tkMessageBox.showerror(_("Empty gcode"),
					_("Not gcode file was loaded"),
					parent=self)
				return

			# reset colors
			before = time.time()
			for ij in self._paths:	# Slow loop
				if not ij: continue
				path = self.gcode[ij[0]].path(ij[1])
				if path:
					color = self.canvas.itemcget(path, "fill")
					if color != CNCCanvas.ENABLE_COLOR:
						self.canvas.itemconfig(
							path,
							width=1,
							fill=CNCCanvas.ENABLE_COLOR)
					# Force a periodic update since this loop can take time
					if time.time() - before > 0.25:
						self.update()
						before = time.time()

			# the buffer of the machine should be empty?
			self._runLines = len(self._paths) + 1	# plus the wait
		else:
			n = 1		# including one wait command
			for line in CNC.compile(lines):
				if line is not None:
					if isinstance(line,str) or isinstance(line,unicode):
						self.queue.put(line+"\n")
					else:
						self.queue.put(line)
					n += 1
			self._runLines = n	# set it at the end to be sure that all lines are queued
		self.queue.put((WAIT,))		# wait at the end to become idle 

		self.setStatus(_("Running..."))
		self.statusbar.setLimits(0, self._runLines)
		self.statusbar.configText(fill="White")
		self.statusbar.config(background="DarkGray")

		self.bufferbar.configText(fill="White")
		self.bufferbar.config(background="DarkGray")
		self.bufferbar.setText("")
        

if __name__ == "__main__":
    global mainFrame 
    root = tk.Tk()
    root.resizable(width=False, height=False) 
    mainFrame = MainGUI(root) 
    root.mainloop() 

