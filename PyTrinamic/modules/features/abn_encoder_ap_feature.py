'''
Created on 01.10.2020

@author: ED
'''

from abc import ABC

class abn_encoder_ap_feature(ABC):
 
    def __init__(self, parent):
        self._motorInterface = parent
        
    def setResolution(self, steps):
        self._motorInterface.setAxisParameter(self._motorInterface.AP.EncoderSteps, steps)
                                             
    def resolution(self):
        return self._motorInterface.axisParameter(self._motorInterface.AP.EncoderSteps)

    def setDirection(self, direction):
        self._motorInterface.setAxisParameter(self._motorInterface.AP.EncoderDirection, direction)

    def direction(self):
        return self._motorInterface.axisParameter(self._motorInterface.AP.EncoderDirection)

    def setInitMode(self, mode):
        self._motorInterface.setAxisParameter(self._motorInterface.AP.EncoderInitMode, mode)

    def initMode(self):
        return self._motorInterface.axisParameter(self._motorInterface.AP.EncoderInitMode)

    def showConfiguration(self):
        print("ABN encoder configuration:")
        print("\tResolution: " + str(self.resolution()))
        print("\tDirection:  " + str(self.direction()))
        print("\tInit mode:  " + str(self.initMode()))
