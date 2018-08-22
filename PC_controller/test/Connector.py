
import time 
import serial
from serial.tools.list_ports import comports
from Machine import Machine 

BAUD_RATE = 115200

class Connector:
    def __init__(self):
        self.devices = self.getSerialPorts() 
        self.defaultDevice = self.devices[-1] if len(self.devices)>0 else None 

        self.serial = None 
        self.isOpen = False # True for connected, False for unconnected
    
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

###################################################################
#                         CODE TEST
###################################################################
if __name__ == "__main__":
    connector = Connector()
    print(connector.devices)
    print(connector.defaultDevice)

    connector.openPort() 

    if connector.isOpen == True:
        print("Port opened")
    else:
        print("Port closed")

    time.sleep(5)
    connector.closePort() 

    if connector.isOpen == True:
        print("Port opened")
    else:
        print("Port closed")

