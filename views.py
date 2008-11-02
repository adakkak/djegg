from django.http import HttpResponse
from django.core.serializers import serialize
from django.utils import simplejson
import sys
sys.path.append('thrift/gen-py')

import datetime
from edf_reader import *

from edf import Request

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

def current_datetime(request):
    now = datetime.datetime.now( )
    html = "<html><body>It's now %s.</body></html>" % now
    return HttpResponse(html)

def remote_plot(request, n):

    print 'in remote plot...'
    n = int(n)

    try:
        print 'requesting header...'
        transport = TSocket.TSocket('localhost', 9091)
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = Request.Client(protocol)
        transport.open()

        client.set_file("../../test_data/st7132j0.rec")

        print 'requesting header...'
        header = client.get_header()

        print header
        samples_recieved = [[] for i in header.nrs]

        for i in xrange(n):
            sample = client.get_sample()
            for j, s in enumerate(sample):
                samples_recieved[j].append(s)

        samples = []
        for i in range(len(samples_recieved)):
            samples.append({"label":[header.labels[i]],
                            "data": zip(range(n), samples_recieved[i])})

        transport.close()

        return plot_data(header.__dict__, samples)
    except Thrift.TException, tx:
        print '%s' % (tx.message)
        return plot.data("Header not found", "Samples not found")

def plot(request, n):
    edf = EDF("test_data/st7132j0.rec")
    header = edf.header
#    json = simplejson.dumps(header)
#    json = simplejson.dumps(edf.samples)
    n = int(n)
#    for i in range(n):
#        edf.next_sample()
    

    request.session.setdefault('n', n)
    print request.session['n']
    request.session['n'] += 5

    s = map(lambda x: x[:request.session['n']], edf.samples)

    samples = []
    for i in range(len(s)):
        samples.append({"label":[edf.header["labels"][i]],
                        "data": zip(range(request.session['n']), s[i])})

    return plot_data(header, samples)


def plot_data(header, samples):
    json = simplejson.dumps({"header":header, "samples":samples})
    return HttpResponse(json, mimetype='application/json')
