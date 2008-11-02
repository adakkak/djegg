#!/usr/bin/env python

import sys
sys.path.append('../gen-py')

from edf import Request
from edf_file_reader import EdfFileReader

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

class RequestHandler:
    def __init__(self):
        self.log = {}
        self.samples = []
        self.header = []
        self.edf = None

    def set_file(self, file_name):
        self.edf = EdfFileReader(file_name)
        print 'set file name to %s' % file_name

    def get_header(self):
        edf_header = self.edf.header
        h = Request.Header()
        
        h.version = edf_header["version"]
        h.patient_id = edf_header["patient_id"]
        h.record_id = edf_header["record_id"]
        h.startdate = edf_header["startdate"]
        h.starttime = edf_header["starttime"]
        h.header_length = edf_header["header_length"]

        h.num_of_records = edf_header["num_of_records"]
        h.record_duratioin = edf_header["record_duration"]
        h.num_of_signals = edf_header["num_of_signals"]

        h.labels = edf_header["labels"]
        h.transducer_types = edf_header["transducer_types"]
        h.physical_dims = edf_header["physical_dims"]
        h.physical_mins = edf_header["physical_mins"]
        h.phyical_maxs = edf_header["physical_maxs"]
        h.dig_mins = edf_header["dig_mins"]
        h.dig_maxs = edf_header["dig_maxs"]
        h.prefilterings = edf_header["prefilterings"]
        h.nrs = edf_header["nrs"]

#        for key in edf_header:
#            exec 'h.%s = edf_header[%s]' % (key,key)

        return h

    def get_sample(self):
        return self.edf.next_sample()

handler = RequestHandler()
processor = Request.Processor(handler)
transport = TSocket.TServerSocket(9091)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

print 'starting server...'
server.serve()
print 'done.'
