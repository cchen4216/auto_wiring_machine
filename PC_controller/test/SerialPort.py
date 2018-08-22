
import time 
import re 
import serial
from serial.tools.list_ports import comports
import threading 
from queue import Queue
from Connector import Connector
from Utils import toAsc 

BAUD_RATE = 115200
RX_BUFFER_SIZE = 128  # Byte 
LOG_INTERVAL = 0.5    # s

cmdQueue = Queue()

class SerialPort:
    def __init__(self):
        self.devices = self.getSerialPorts()
        self.defaultDevice = self.devices[-1] if len(self.devices)>0 else None
        self.serial = None 
        self.isOpen = False # True for connected, False for unconnected

        # self.cmdQueue = Queue()
        self.logQueue = Queue()
        self.status = 'Idle'     # Machine status
        self._stop = False       # raise to stop current run 

        self.thread  = threading.Thread(target = self.sendRecv)
        self.thread.daemon = True 
        self.thread.start()

        self.cline = []      # length of pipline commands
        self.sline = []      # pipeline commands
        self._gcount = 0     # number of processed commands


    #----------------------------------------------------------------------
	# Get serial ports
	#----------------------------------------------------------------------
    def getSerialPorts(self):
        devices = sorted([x[0] for x in comports()])
        return devices

    #----------------------------------------------------------------------
	# Open serial port
	#----------------------------------------------------------------------
    def openPort(self, device=None):
        if device == None:
            device = self.defaultDevice
        if device == None:
            print('No serial device connected')
            return False 

        self.serial = serial.Serial(device, BAUD_RATE)
        
		# Toggle DTR to reset Arduino
        try:
            self.serial.setDTR(0)
        except IOError:
            pass
        time.sleep(1)
        self.serial.flushInput()
        try:
            self.serial.setDTR(1)
        except IOError:
            pass
        time.sleep(1)

        # Wake up Firmware
        print("Initializing Firmware...") 
        self.serial.write(b"\r\n\r\n")
        # Wait for grbl to initialize and flush startup text in serial input
        time.sleep(2)
        self.serial.flushInput() 

        self.isOpen = True 
        return True

    #----------------------------------------------------------------------
	# Close serial port
	#----------------------------------------------------------------------
    def closePort(self):
        if self.serial is None: return
		# check the machine status
        # check the sender status
        # check the looger status
        time.sleep(1)
        try:
            self.serial.close()
            self.isOpen = False 
        except:
            pass
        self.serial = None

    #----------------------------------------------------------------------
    # Put commands, including gcode, in queue for sending
    #----------------------------------------------------------------------
    def queueCommand(self, cmd):
        if self.serial:
            # if tosend is not string (gcode), tuple or other thing
            # do some preprocessing here

            # Strip comments/spaces/new line and capitalize
            cmd = re.sub(r"\s|\(.*?\)", '', cmd).upper()
            cmdQueue.put(toAsc(cmd+'\n'))

    #----------------------------------------------------------------------
	# thread performing I/O on serial line 
	#----------------------------------------------------------------------
    def sendRecv(self):
        tosend = None   # next string to send
        t0 = time.time() # Last logging time 

        time.sleep(2)
        while self.thread:
            ## query status of machine
            t = time.time()
            if t-t0 > LOG_INTERVAL:
                self.serial.write(b"?")  
                t0 = t 
            ## Get command from the Queue 
            if tosend==None and cmdQueue.qsize()>0: 
                tosend = cmdQueue.get_nowait() 
                if tosend is not None:
                    # bookkeeping of the buffers
                    self.sline.append(tosend)
                    self.cline.append(len(tosend))
            
            ## Receive log/reports from serial port 
            if self.serial.inWaiting() :
                log = self.serial.readline().decode('utf-8').strip() 
                self.processLog(log) 
            
            if self._stop:
                print('To stop machine running')

            if tosend!=None and sum(self.cline)<RX_BUFFER_SIZE:  
                # command can be written now 
                self.serial.write(tosend) 
                
                self.logQueue.put(('MSG_BUFFER', tosend))
                # print('MSG_BUFFER', tosend)
                tosend = None 



    def processLog(self, log):
        if not log:
            pass 
        elif log[0] == '<':
            self.logQueue.put(log) 
            print('MSG:', log) 
            if log.find('Idle') >= 0:
                self.status = 'Idle'
            if log.find('Run') >= 0:
                self.status = 'Run'
        elif 'error:' in log or 'ALARM:' in log: 
            self.logQueue.put(log) 
            print('ERR:', log) 
            self._gcount += 1 
            if self.cline: 
                del self.cline[0]
            if self.sline: 
                print('err gcode:', self.sline.pop(0))
            if self.status == 'Run':
                self._stop = True 
        elif log.find('ok') >= 0:
            self._gcount += 1
            if self.cline:
                del self.cline[0]
            if self.sline:
                del self.sline[0]
        else:
            pass 
            
            
