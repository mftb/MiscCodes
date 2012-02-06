#!/usr/bin/env python
# -*- coding: latin1 -*-
# script de cronometro
# por matheus boy

from datetime import *

class stopwatch:
    def  __init__(self):
        self.a = datetime.today()

    def stop(self):
        self.b = datetime.today()
        return self.b - self.a 
        
sw = stopwatch()

print "Pressione enter para parar o cronômetro: "
raw_input()

print sw.stop()
