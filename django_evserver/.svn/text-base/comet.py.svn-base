#!/usr/bin/python
# -*- coding: utf-8 -*-
# pylint: disable-msg=C0301
from functools import wraps
from django.http import HttpResponse
import django_evserver.json as json
from django_evserver.server import defer_for_fifo, EVENT_CLOSED


def comet_start(transport, callback, domain):
    ''' Produce headers content for comet conection. '''
    if transport == 'sse':
        data     = '''Event: sessionid\ndata: p4sq1n8b$EGcGnKpwW7yNw\n\n\r\n'''
        mimetype = 'application/x-dom-event-stream'
    elif transport == 'iframe' or transport == 'htmlfile':
        fill = '<span></span>'*80 # fill for safari, 1024 bytes of padding
        domain = '''<script>try{document.domain='%s';}catch(e){}</script>''' % domain

        data     = '''<html><body onLoad="try{parent.%s_reconnect(true);}catch(e){};">%s\n%s\n''' % \
                      (callback, domain, fill)
        mimetype = 'text/html; charset=utf-8'
    else: # if transport == 'xhr':
        ## application/xml based on: http://lists.macosforge.org/pipermail/webkit-dev/2007-June/002041.html
        ## must be some message here, at least one byte long...
        data     = ' '
        mimetype = 'application/xml; charset=utf-8'

    return (data, mimetype)

def comet_continue(transport, data, callback):
    ''' Create data wrapper on comet conection. '''
    if transport == 'sse':
        content = '''Event: comet\ndata: %s\n\n''' % data
    elif transport == 'iframe' or transport == 'htmlfile':
        content = '''<script>parent.%s("%s");</script>\r\n''' % \
            (callback, data.replace(r'"', r'\"'))
    else:    #elif transport == 'xhr':
        content = '''%s\r\n''' % data
    return content



def comet_fifo_json(fifo_name='', time_delta=30.0):
   def decorator(function):
       @wraps(function)
       def _wrapper(request, *args, **kwargs):
           return json_comet_wrapper(request, function, fifo_name, time_delta, *args, **kwargs)
       return _wrapper
   return decorator


def json_comet_wrapper(request, user_view, fifo_name, time_delta, *args, **kwargs):
    response_prev = request.META.get('response_prev', None)
    event_flags   = request.META.get('event_flags', None)
    event_type    = request.META.get('event_type', None)

    if not response_prev:
        transport = request.GET.get('transport', None)
        callback  = request.GET.get('callback', 'c').replace("'", "").replace('"', '')
        domain    = request.GET.get('domain', request.META['SERVER_NAME']).replace("'", "").replace('"', '')
        view_data = {}
        first_request = True
    else:
        transport = response_prev.transport
        callback  = response_prev.callback
        view_data = response_prev.view_data
        first_request = False
       
    
    # run callback if first request or event (not on timeout)
    if event_flags != 1:
        keepalive = False
    else: # keepalive
        keepalive = True
    
        
    #kwargs.setdefault('response_prev', response_prev)
    #kwargs.setdefault('event_flags', event_flags)
    kwargs.setdefault('view_data', view_data) # that's going to be changed by callback
    kwargs.setdefault('keepalive', keepalive)
    kwargs.setdefault('event_type', event_type)
    
    payload = user_view(request, *args, **kwargs)
    if not keepalive or payload: # not keepalive or something returned
        payload = json.write(payload)
    else: #keepalive and empty response
        payload = ' '
    
    # produce Response object, for comet application
    # first request, not continuation
    if event_type == EVENT_CLOSED:
        return HttpResponse()
    elif first_request:
        content, mimetype = comet_start(transport, callback, domain)
        response = HttpResponse(content, mimetype=mimetype)
        response['Cache-Control'] = 'no-cache'

        # append user data
        content = comet_continue(transport, payload, callback)
        response.write(content)
    # if not first_request: -> continue previous request
    else: 
        content  = comet_continue(transport, payload, callback)
        response = HttpResponse(content)

    
    response.transport = transport
    response.callback  = callback
    response.view_data = view_data
    
    
    return defer_for_fifo(
        response,
        fifo_name, time_delta,
        request.META['PATH_INFO'])
































"""    
    

#
# as told in: http://cometdaily.com/2007/12/11/the-future-of-comet-part-1-comet-today/
# we're doing a variant called 'XHR long-polling'
#
def defcon_event(request):
    ''' wait for events on fifo 
        first return 256 bytes of shit.
    '''
    transport = request.GET.get('transport', None)
    callback = 'c'
    if transport == 'sse':
        response = HttpResponse('''Event: sessionid\ndata: p4sq1n8b$EGcGnKpwW7yNw\n\n\r\n''', 
                                    mimetype='application/x-dom-event-stream' )#; charset=utf-8'
    elif transport == 'iframe' or transport == 'htmlfile':
        # fill for safari, 1024 bytes of padding # 
        #if transport == 'iframe':
        fill = '<span></span>'*80
        #else:
        #    fill = ''
        domain   = request.GET.get('domain', request.META['SERVER_NAME'])
        domain = domain.replace("'", "").replace('"', '')
        callback = request.GET.get('callback', 'c').replace("'", "").replace('"', '')
        
        if transport != 'iframe':
            domain = '''<script>try{document.domain='%s';}catch(e){}</script>''' % domain
        else:
            domain = ''
        
        response = HttpResponse(
            '''<html><body onLoad="try{parent.%s_reconnect(true);}catch(e){};">%s<script>try {parent.%s(" ")} catch(e) {}</script>\n%s\n''' %
                 (callback, domain, callback, fill),
            mimetype='text/html; charset=utf-8')
    #elif transport == 'xhr':# <body onLoad="parent.server_reconnect(true);">
    else:
        ## application/xml based on: http://lists.macosforge.org/pipermail/webkit-dev/2007-June/002041.html
        ## must be some message here, at least one byte long...
        response = HttpResponse(' ', mimetype='application/xml; charset=utf-8')
        
    response.transport = transport
    response.callback  = callback
    
    response['Cache-Control'] = 'no-cache'
    return defer_for_fifo(
            response,
            'events_fifo', 5.0,
            '/defcon_event_continue/')



indexer = 0
@deferred_view()
def defcon_event_continue(request, response_prev=None, event_flags=None):
    ''' wait for events on fifo
    '''
    global indexer
    transport = response_prev.transport
    callback  = response_prev.callback
    
    
    if event_flags != 1:
        indexer += 1
        data = indexer
        
        data = json.write(data)
    else:
        data = ' '  # keepalive
    
    if transport == 'sse':
        response = HttpResponse('''Event: comet\ndata: %s\n\n\r\n''' % data)
    elif transport == 'iframe' or transport == 'htmlfile':
        response = HttpResponse('''<script>parent.%s("%s");</script>\r\n''' % 
            (callback, data.replace(r'"', r'\"')) )
    #elif transport == 'xhr':
    else:
        response = HttpResponse('''%s\n''' % data)
    
    response.transport = transport
    response.callback  = callback
    
    return defer_for_fifo(
            response,
            'events_fifo', 5.0,
            '/defcon_event_continue/')


"""