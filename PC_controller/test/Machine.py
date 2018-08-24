
# 这个类是机器的抽象，用来表征的机器的状态

import time 


class Machine:

    status = {
        'wx'    : 0.0,
        'wy'    : 0.0,
        'wz'    : 0.0,
        'mx'    : 0.0,
        'my'    : 0.0,
        'mz'    : 0.0,
        'feed'  : 0.0,
    }
    def __init__(self):
        self.status = None  
        self.pos = (None, None, None) 