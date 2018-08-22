import serial
import time 
import threading
import sys
# from CNC import WAIT, MSG, UPDATE, WCS, CNC, GCode

try:
	from Queue import *
except ImportError:
	from queue import *

class Sender:
    # Messages types for log Queue
    MSG_BUFFER  =  0	# write to buffer one command
    MSG_SEND    =  1	# send message
    MSG_RECEIVE =  2	# receive message from controller
    MSG_OK	    =  3	# ok response from controller, move top most command to terminal
    MSG_ERROR   =  4	# error message or exception
    MSG_RUNEND  =  5	# run ended
    MSG_CLEAR   =  6	# clear buffer

    def __init__(self):
        # Global variables
        self.history	 = []
        self._historyPos = None
        # CNC.loadConfig(Utils.config)
        # self.gcode = GCode()
        # self.cnc   = self.gcode.cnc

        self.log	 = Queue()	    # Log queue returned from GRBL
        self.queue	 = Queue()	    # Command queue to be send to GRBL
        # self.pendant    = Queue()	# Command queue to be executed from Pendant
        self.serial	 = None
        self.thread	 = None
        # self.controller  = Utils.CONTROLLER["Grbl"]

        self._posUpdate  = False	# Update position
        self._probeUpdate= False	# Update probe
        self._gUpdate	 = False	# Update $G
        self._update	 = None		# Generic update

        self.running	 = False
        self._runLines	 = 0
        self._quit	 = 0		# Quit counter to exit program
        self._stop	 = False	# Raise to stop current run
        self._pause	 = False	# machine is on Hold
        self._alarm	 = True		# Display alarm message if true
        self._msg	 = None
        self._sumcline	 = 0
        self._lastFeed	 = 0
        self._newFeed	 = 0

        self._onStart    = ""
        self._onStop     = ""
    
    #----------------------------------------------------------------------
	# Open serial port
	#----------------------------------------------------------------------
    def open(self, device, baudrate):
        self.serial = serial.Serial(device, baudrate)
		# Toggle DTR to reset Arduino
        try:
            self.serial.setDTR(0)
        except IOError:
            pass
        time.sleep(1)
        # CNC.vars["state"] = CONNECTED
        # CNC.vars["color"] = STATECOLOR[CNC.vars["state"]]
        self.serial.flushInput()
        try:
            self.serial.setDTR(1)
        except IOError:
            pass
        time.sleep(1)
        self.serial.write(b"\n\n")
        self._gcount = 0
        self._alarm  = True
        # self.thread  = threading.Thread(target=self.serialIO)
        # self.thread.start()
        # print("Serial Connect Successfully!")
        return True
         

	#----------------------------------------------------------------------
	# Close serial port
	#----------------------------------------------------------------------
    def close(self):
        if self.serial is None: return
        try:
            self.stopRun()
        except:
            pass
        self._runLines = 0
        self.thread = None
        time.sleep(1)
        try:
            self.serial.close()
        except:
            pass
        self.serial = None
		# CNC.vars["state"] = NOT_CONNECTED
		# CNC.vars["color"] = STATECOLOR[CNC.vars["state"]]
    
    #----------------------------------------------------------------------
	# Stop the current run
	#----------------------------------------------------------------------
    def stopRun(self, event=None):
        self.feedHold()
        self._stop = True
        # if we are in the process of submitting do not do anything
        self.purgeController()

    #----------------------------------------------------------------------
    # `!` feedhold 是 grbl 的一个实时指令。这个指令会让 grbl 进入 suspend/hold 状态.
    # 运动中的平台会减速停止，执行了一半的命令会被缓存起来。
    def feedHold(self, event=None):
        if event is not None : 
            return
        if self.serial is None: 
            return
        self.serial.write(b"!")
        self.serial.flush()
        self._pause = True
    
    #----------------------------------------------------------------------
	# Purge the buffer of the controller. Unfortunately we have to perform
	# a reset to clear the buffer of the controller
	#---------------------------------------------------------------------
    def purgeController(self):
        self.serial.write(b"!")
        self.serial.flush()
        time.sleep(1)
        # # remember and send all G commands
        # G = " ".join([x for x in CNC.vars["G"] if x[0]=="G"])	# remember $G
        # TLO = CNC.vars["TLO"]
        # self.softReset(False)			# reset controller
        # if self.controller in (Utils.GRBL0, Utils.GRBL1):
        #     time.sleep(1)
        #     self.unlock(False)
        # self.runEnded()
        # self.stopProbe()
        # if G: self.sendGCode(G)			# restore $G
        # self.sendGCode("G43.1Z%s"%(TLO))	# restore TLO
        # self.sendGCode("$G")
        pass 
    
    #----------------------------------------------------------------------
    def initRun(self):
        self._quit   = 0
        self._pause  = False
        self._paths  = None
        self.running = True
        self.disable()
        self.emptyQueue()
        time.sleep(1)

    #----------------------------------------------------------------------
	# thread performing I/O on serial line
	#----------------------------------------------------------------------
    def serialIO(self):
        pass 