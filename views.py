from django.http import HttpResponse
from django.core.serializers import serialize
from django.utils import simplejson

import datetime
from edf import *

def current_datetime(request):
    now = datetime.datetime.now( )
    html = "<html><body>It's now %s.</body></html>" % now
    return HttpResponse(html)

def plot(request, n):
    edf = EDF("test_data/st7132j0.rec")
    header = edf.header
#    json = simplejson.dumps(header)
#    json = simplejson.dumps(edf.samples)
    n = int(n)
#    for i in range(n):
#        edf.next_sample()
    
    s = map(lambda x: x[:n], edf.samples)

    samples = []
    for i in range(len(s)):
        samples.append({"label":[edf.header["labels"][i]],
                        "data": zip(range(n), s[i])})

    json = simplejson.dumps({"header":header,  "samples":samples})
    return HttpResponse(json, mimetype='application/json')
