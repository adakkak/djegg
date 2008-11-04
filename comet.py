from multiprocessing import Process
from stompservice import StompClientFactory
from twisted.internet import reactor
from twisted.internet.task import LoopingCall
from orbited import json

from random import random

from edf_reader import *

class CometFactory(StompClientFactory):
    def recv_connected(self, msg):
        print 'Connected; producing data'
        self.edf = EDF("test_data/st7132j0.rec")
        self.timer = LoopingCall(self.send_data)
        self.timer.start(0.2)

    def recv_message(self,msg):
        pass
        
    def send_data(self):
#        print 'sent data'
        self.data = self.edf.next_sample()
        self.send("/comet/plot", json.encode(self.data))

reactor.connectTCP("localhost", 61613, CometFactory())
#reactor.run()
p = Process(target=reactor.run)
p.start()

