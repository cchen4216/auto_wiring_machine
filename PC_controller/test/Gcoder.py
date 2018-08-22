
import re 
# import dxf2gcode
from Utils import toAsc 

from SerialPort import cmdQueue 

class Gcoder:
    def __init__(self):
        self.fname = None 
        # self.queue = cmdQueue
    
    def readFile(self, fname):
        self.fname = fname
        fo = open(fname, 'r')
        for line in fo:
            line = re.sub(r"\s|\(.*?\)", '', line).upper() 
            # print('gcode:', line)
            # self.queue.put(toAsc(line+'\n'))
            cmdQueue.put(toAsc(line+'\n'))


    