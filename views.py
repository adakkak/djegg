from django.http import HttpResponse
from django.core.serializers import serialize
from django.utils import simplejson

import datetime
from edf import *

def current_datetime(request):
    now = datetime.datetime.now( )
    html = "<html><body>It's now %s.</body></html>" % now
    return HttpResponse(html)

def plot(request):
    edf = EDF("test_data/st7132j0.rec")
    header = edf.header
#    json = simplejson.dumps(header)
#    json = simplejson.dumps(edf.samples)
    json = simplejson.dumps(map(lambda x: zip(range(len(x)), x), edf.samples))
    return HttpResponse(json, mimetype='application/json')
