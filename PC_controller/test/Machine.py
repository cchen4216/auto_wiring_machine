
# 这个类是机器的抽象，用来表征的机器的状态

import time 


class Machine:
    def __init__(self):
        self.status = None  
        self.pos = (None, None, None) 