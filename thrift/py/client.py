#!/usr/bin/env python

import sys
sys.path.append('../gen-py')

from edf import Request

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

try:
    transport = TSocket.TSocket('localhost', 9091)

    transport = TTransport.TBufferedTransport(transport)

    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    client = Request.Client(protocol)

    transport.open()

    print 'setting file_name'
    client.set_file("sleep.edf")

    print 'getting header'
    header = client.get_header()
    print header

    print 'getting sample'
    for i in xrange(10):
        s = client.get_sample()
        print s

    transport.close()
except Thrift.TException, tx:
    print '%s' % (tx.message)
