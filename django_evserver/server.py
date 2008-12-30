#!/usr/bin/python
# -*- coding: utf-8 -*-
# pylint: disable-msg=C0301

import ctypes
import sys
import signal
import ctypes_event as libevent
import traceback
import time
import os
from functools import wraps
import StringIO
import datetime

ud_map = {}

FUNC  = ctypes.CFUNCTYPE(None, ctypes.POINTER(libevent.evhttp_request), ctypes.c_void_p)
FUNC2 = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_short, ctypes.c_void_p)
FUNC3 = ctypes.CFUNCTYPE(None, ctypes.POINTER(libevent.evhttp_connection), ctypes.c_void_p)


from django.core.handlers import wsgi
djhand=wsgi.WSGIHandler()


def django_handler(environ):
    g = {'response_headers':None}
    
    # We love closures
    def start_response(lstatus, lresponse_headers):
        g['response_headers'] = lresponse_headers
        return
    
    response = djhand(environ, start_response)
    
    assert(isinstance(response.content, list) or isinstance(response.content, str))
    
    status_code = response.status_code
    status_reason = wsgi.STATUS_CODE_TEXT.get(status_code, 'UNKNOWN STATUS CODE')
    
    return (status_code, status_reason, g['response_headers'], response.content, response)



def request_to_environ(req):
    ev = req.contents.input_headers.contents.tqh_first.contents
    headers = {}
    while ev:
        new_key = 'HTTP_' + ev.key.upper().replace('-','_')
        headers[new_key] = ev.value[:]
        if not ev or not ev.next or not ev.next.tqe_next:
            break
        ev = ev.next.tqe_next.contents
        
    headers['PATH_INFO'], _, headers['QUERY_STRING'] = req.contents.uri[:].partition('?')
    headers['SCRIPT_NAME'] = ''
    if req.contents.type == libevent.EVHTTP_REQ_GET:
        headers['REQUEST_METHOD'] = 'GET'
    elif req.contents.type == libevent.EVHTTP_REQ_POST:
        headers['REQUEST_METHOD'] = 'POST'
    elif req.contents.type == libevent.EVHTTP_REQ_HEAD:
        headers['REQUEST_METHOD'] = 'HEAD'
    else:
        #log warning
        headers['REQUEST_METHOD'] = 'UNKNOWN'
    
    host, _, port = headers.get('HTTP_HOST', '').rpartition(':')
    
    headers['SERVER_NAME'] = host
    headers['SERVER_PORT'] = port
    # major and minor is char, so it's treated as singlechar string. 
    # we could cast it to int, but ord is simpler.
    headers['SERVER_PROTOCOL'] = 'HTTP/%i.%i' % (ord(req.contents.major), ord(req.contents.minor))
    
    if 'HTTP_CONTENT_TYPE' in headers:
        headers['CONTENT_TYPE'] = headers['HTTP_CONTENT_TYPE']
    
    if 'HTTP_CONTENT_LENGTH' in headers:
        headers['CONTENT_LENGTH'] = headers['HTTP_CONTENT_LENGTH']
    
    
    # not in standard
    headers['REMOTE_HOST'] = req.contents.remote_host[:]
    headers['REMOTE_PORT'] = req.contents.remote_port
    
    headers['wsgi.version'] = (1, 0)
    # TODO: support https
    headers['wsgi.url_scheme'] = "http"
    
    # request body stream
    data = StringIO.StringIO() # only for POST?
    if req.contents.input_buffer and req.contents.input_buffer.contents.off:
        buf = ctypes.create_string_buffer(req.contents.input_buffer.contents.off)
        # Warning, warning. okay, this should work, but it's not the cleanest :)
        ctypes.memmove(buf, req.contents.input_buffer.contents.buffer, req.contents.input_buffer.contents.off)
        
        data.write(buf.raw)
        data.flush()
        data.seek(0)
        del buf
        
    headers['wsgi.input'] = data
    headers['wsgi.multithread'] = False
    headers['wsgi.multiprocess'] = True # ke?
    headers['wsgi.run_once'] = False
    headers['server_type'] = 'simple'
    
    #for k, v in headers.items():
    #    print "%r -> %r" % (k, v)
    
    return headers
    
    

EVENT_CLOSED = 1

def close_callback(conn, user_data_id):
    user_data, environ = yyyy(user_data_id, unset_event=True)
    
    if not user_data:
        print "no user data"
    else:
        os.close( user_data['fd'] )
        root_handler(user_data['response'].http_request, environ, event_type=EVENT_CLOSED)
    

    del user_data
    return 0

close_callback_ptr = FUNC3(close_callback)



req_type = ctypes.POINTER(libevent.evhttp_request)
buf_type = ctypes.POINTER(libevent.evbuffer)
def root_handler(req, environ, event_type=0):
    t0 = time.time()
    # force type conversion. I have no idea why it's needed but it is.
    req = ctypes.cast(req, req_type)
    
    if not environ:
        environ = request_to_environ(req)
        first_request = True
    else:
        first_request = False
        
    environ['event_type'] = event_type
    try:
        status_code, status_reason, response_headers, data, response = django_handler( environ.copy() )
    except Exception: # all exceptions...
        traceback.print_exc(file=sys.stdout)
        status_code, status_reason, response_headers, data, response = \
            500 , 'INTERNAL SERVER ERROR', (), '<h1>500 internal server error</h1>', object()

    if hasattr(response, 'continuation') and response.continuation:
        continuation = True
    else:
        continuation = False

    if first_request: # only on first request
        for key, value in response_headers:
            libevent.evhttp_add_header(req.contents.output_headers, str(key), str(value))

    
    content_length = 0
    content_type = ''
    
    # first_request, and we don't continue and string -> straight response
    if event_type == EVENT_CLOSED:
        if data:
            print "fuckoff, event is closed and you want to return data"
    elif first_request and isinstance(data, str) and not continuation:
        # libevent is broken, it's not sending content-length for http1.0
        libevent.evhttp_add_header(req.contents.output_headers, 'Content-Length', str(len(data)))
        
        assert(first_request)
        assert(isinstance(data, str))
        buf=libevent.evbuffer_new()
        libevent.evbuffer_add(buf, data, len(data))
        libevent.evhttp_send_reply(req, status_code, status_reason, buf)
        libevent.evbuffer_free(buf)
        content_length = len(data)
        content_type = ''
        
    # else: chunked:
    else: #force chunked
        if isinstance(data, str):   # yep, we need list
            data = [data]
        
        assert(isinstance(data, list))
        
        # first reqiest: open the chunkinkg mode
        if first_request:
            buf=libevent.evbuffer_new()
            libevent.evhttp_send_reply_start(req, status_code, status_reason)
        else:
            buf = environ['buf']
            buf = ctypes.cast(buf, buf_type)
        
        content_type = 'chunk'

        # for chunk in chunks...
        for data_chunk in data:
            if not data:
                continue
            assert(isinstance(data_chunk, str))
            libevent.evbuffer_add(buf,data_chunk, len(data_chunk))
            libevent.evhttp_send_reply_chunk(req, buf)
            content_length += len(data_chunk)
        
        # don't continue the answer in the future -> close
        if not continuation:
            libevent.evhttp_send_reply_end(req)
            libevent.evbuffer_free(buf)
            if 'buf' in environ:
                del environ['buf']
        else:
            # don't close the connection and save the request object and environ
            response.environ = environ
            response.http_request = req
            environ['buf'] = buf

    if getattr(response, 'schedule', None) and response.schedule and event_type != EVENT_CLOSED:
        libevent.evhttp_connection_set_closecb(req.contents.evcon, close_callback_ptr, response.schedule)
        response.schedule = None

    t1 = time.time()
    print '''%(date)s %(host)s "%(method)s %(url)s %(http)s" %(status_code)i %(content_length)i %(content_type)s %(continuation)s  (%(time).3fms)''' % {
        'date':datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]"),
        'method':environ['REQUEST_METHOD'],
        'url': environ['PATH_INFO'] + '?' + environ['QUERY_STRING'],
        'http': environ['SERVER_PROTOCOL'],
        'status_code': status_code,
        'content_length': content_length,
        'content_type': content_type,
        'continuation': '...<' if event_type==EVENT_CLOSED else '' if not continuation else '>...' if first_request else '...',
        'host': '%s:%i' % (environ['REMOTE_HOST'], environ['REMOTE_PORT']),
        'time': (t1-t0) * 1000, # in miliseconds
        }
    
    return 1




def signal_handler(req, nr, user_data):
    libevent.event_loopexit(None)
    return 1

references = {}
def inc_ref(obj):
    ''' make sure that the object will never be garbage-collected'''
    references.setdefault(id(obj), (0, obj))
    refcount, _ = references[id(obj)]
    references[id(obj)] = (refcount+1, obj)
    return obj

def dec_ref(obj):
    ''' make sure that the object will never be garbage-collected'''
    refcount, _ = references[id(obj)]
    refcount -= 1
    if refcount < 1:
        del references[id(obj)]
    else:
        references[id(obj)] = (refcount, obj)
    return obj


def main(host='0.0.0.0', port=8080):
    
    
    #We just initialise and give the server address and port
    libevent.event_init()
    print "listening on %s:%i" % (host,port)
    http = libevent.evhttp_start(host, port)
    
    libevent.evhttp_set_gencb(http, inc_ref(FUNC(root_handler)), None);
    # handle CTRL+C
    event = libevent.event()
    event_ref = ctypes.byref(event)
    libevent.signal_set(event_ref, signal.SIGINT, inc_ref(FUNC2(signal_handler)), None)
    libevent.signal_add(event_ref, None)
    
    
    libevent.event_dispatch()
    
    # end loop - id est Ctrl+c :P 
    libevent.evhttp_free(http)
    
    raise KeyboardInterrupt
    
if __name__=="__main__":
    main()



def yyyy(user_data_id, unset_event=False):
    ud_id =  ctypes.cast(user_data_id, ctypes.POINTER(ctypes.c_long))
    #print "DEL %i (%r)" % (ud_id.contents.value, ud_map.keys() )
    if not ud_id:
        return None, None
    user_data = ud_map[ud_id.contents.value]
    
    # use the same environ
    #return user_data['callback'](*user_data['args'], **user_data['kwargs'])
    environ = user_data['response'].environ
    environ['PATH_INFO'] = user_data['callback_url']
    environ['response_prev'] = user_data['response']
    
    
    del ud_map[ud_id.contents.value]
    if unset_event:
        libevent.event_del(user_data['byref(event)'])
        if 'buf' in environ and environ['buf']:
            libevent.evbuffer_free(environ['buf'])
            del environ['buf']

    del user_data['byref(event)']
    del user_data['byref(id)']
    del user_data['id']
    del user_data['event']
    return user_data, environ


def defer_in_time_handler(req, nr, user_data_id):
    user_data, environ = yyyy(user_data_id)
    environ['event_flags'] = nr
    root_handler(user_data['response'].http_request, environ )
    
    del user_data
    return 1

# this must be global (ie: never garbage-collect)
defer_in_time_hanlder_ptr = FUNC2(defer_in_time_handler)


def xxxx(response, callback_url, fd):
    #global ud_map
    #print ''.join(traceback.format_stack())
    
    event = libevent.event()
    user_data = {}
    user_data['response'] = response
    user_data['callback_url'] = callback_url
    user_data['event'] = event
    user_data['id'] = ctypes.c_long(id(user_data))
    user_data['byref(event)'] = ctypes.byref(event)
    user_data['byref(id)'] = ctypes.byref(user_data['id'])
    user_data['fd'] = fd


    ud_map[user_data['id'].value] = user_data
    #print "ADD %i (%r) %i" % (user_data['id'].value, ud_map.keys(), id(ud_map) )
    
    response.continuation = True
    # set in root_handler.
    response.environ = {}
    response.http_request = None
    
    return (user_data, event)


def defer_in_time(response, deltatime, callback_url):
    user_data, event = xxxx(response, callback_url, 0)
    
    timeval = libevent.timeval()
    timeval.tv_sec  = int(deltatime)
    timeval.tv_usec = 0
    
    # schedule!
    libevent.evtimer_set(user_data['byref(event)'], defer_in_time_hanlder_ptr, user_data['byref(id)'] )
    libevent.evtimer_add(user_data['byref(event)'], ctypes.byref(timeval))
    
    return response
    
    
    
    

    
    
def defer_for_fifo_handler(fd, nr, user_data_id):
    user_data, environ = yyyy(user_data_id)
    environ['event_flags'] = nr
    
    libevent.evhttp_connection_set_closecb(ctypes.cast(user_data['response'].http_request, req_type).contents.evcon, close_callback_ptr, None)
    
    req = ctypes.cast(user_data['response'].http_request, req_type)
    try:
        os.read( user_data['fd'], 4096)
        # if read was correct, than repeat the event request. 
        # you're going to receive yet new event with socket closed.
        
        #user_data, event = xxxx(user_data['response'], user_data['callback_url'], user_data['fd'])
        #libevent.event_set(user_data['byref(event)'], user_data['fd'], libevent.EV_READ, defer_for_fifo_hanlder_ptr, user_data['byref(id)'])
        #libevent.evtimer_add(user_data['byref(event)'], None)
        #return 1
    except OSError: # fuck the result
        pass
    
    os.close( user_data['fd'] )
    user_data['fd'] = 0
    root_handler(user_data['response'].http_request, environ )
    
    del user_data
    return 1

# this must be global (ie: never garbage-collect)
defer_for_fifo_hanlder_ptr = FUNC2(defer_for_fifo_handler)


def defer_for_fifo(response, file_name, deltatime, callback_url):
    fd = os.open(file_name, os.O_RDONLY | os.O_NONBLOCK)
    if not fd or fd < 0:
        print "open() ERROR"
    
    user_data, event = xxxx(response, callback_url, fd)
    
    timeval = libevent.timeval()
    timeval.tv_sec  = int(deltatime)
    timeval.tv_usec = int((deltatime - int(deltatime))* 1000000)
    
    
    
    # schedule!
    libevent.event_set(user_data['byref(event)'], fd, libevent.EV_READ, defer_for_fifo_hanlder_ptr, user_data['byref(id)'])
    libevent.evtimer_add(user_data['byref(event)'], ctypes.byref(timeval))
    
    response.schedule = user_data['byref(id)']
    
    return response
    
    
    
    
def deferred_view():
   ''' Needed to set response_prev var in the context '''
   def decorator(function):
       @wraps(function)
       def _wrapper(request, *args, **kwargs):
           kwargs['response_prev'] = request.META['response_prev']
           kwargs['event_flags'] = request.META['event_flags']
           return function(request, *args, **kwargs)
       return _wrapper
   return decorator
        
