import ctypes
c_longdouble = ctypes.c_double
from ctypes import *

_libraries = {}
_libraries['libevent-1.4.so.2'] = CDLL('libevent-1.4.so.2')
STRING = c_char_p


# def EVBUFFER_INPUT(x): return (x)->input # macro
def EVUTIL_CLOSESOCKET(s): return close(s) # macro
# def EVBUFFER_OUTPUT(x): return (x)->output # macro
# def EVUTIL_SET_SOCKET_ERROR(errcode): return do { errno = (errcode); } while (0) # macro
EVCON_HTTP_TIMEOUT = 0
def EVUTIL_SOCKET_ERROR(): return (errno) # macro
EVHTTP_RESPONSE = 1
EVCON_HTTP_INVALID_HEADER = 2
def signal_set(ev,x,cb,arg): return event_set(ev, x, EV_SIGNAL|EV_PERSIST, cb, arg) # macro
def signal_add(ev,tv): return event_add(ev, tv) # macro
def evtimer_del(ev): return event_del(ev) # macro
# def event_initialized(ev): return ((ev)->ev_flags & EVLIST_INIT) # macro
EVCON_DISCONNECTED = 0
def evtimer_set(ev,cb,arg): return event_set(ev, -1, 0, cb, arg) # macro
# def EVBUFFER_LENGTH(x): return (x)->off # macro
EVHTTP_REQUEST = 0
EVCON_CONNECTED = 2
# def EVBUFFER_DATA(x): return (x)->buffer # macro
EVHTTP_REQ_HEAD = 2
EVHTTP_REQ_GET = 0
EVHTTP_REQ_POST = 1
def signal_del(ev): return event_del(ev) # macro
def evtimer_add(ev,tv): return event_add(ev, tv) # macro
def evtimer_pending(ev,tv): return event_pending(ev, EV_TIMEOUT, tv) # macro
# def EVENT_SIGNAL(ev): return (int)(ev)->ev_fd # macro
# def signal_initialized(ev): return ((ev)->ev_flags & EVLIST_INIT) # macro
EVCON_CONNECTING = 1
EVCON_HTTP_EOF = 1
def signal_pending(ev,tv): return event_pending(ev, EV_SIGNAL, tv) # macro
# def EVENT_FD(ev): return (int)(ev)->ev_fd # macro
# def evtimer_initialized(ev): return ((ev)->ev_flags & EVLIST_INIT) # macro
class event_base(Structure):
    pass
event_base._fields_ = [
]
class event_list(Structure):
    pass
class event(Structure):
    pass
event_list._fields_ = [
    ('tqh_first', POINTER(event)),
    ('tqh_last', POINTER(POINTER(event))),
]
event_base_new = _libraries['libevent-1.4.so.2'].event_base_new
event_base_new.restype = POINTER(event_base)
event_base_new.argtypes = []
event_base_new.__doc__ = \
"""event_base * event_base_new()
/tmp/event.h:269"""
event_init = _libraries['libevent-1.4.so.2'].event_init
event_init.restype = POINTER(event_base)
event_init.argtypes = []
event_init.__doc__ = \
"""event_base * event_init()
/tmp/event.h:280"""
event_reinit = _libraries['libevent-1.4.so.2'].event_reinit
event_reinit.restype = c_int
event_reinit.argtypes = [POINTER(event_base)]
event_reinit.__doc__ = \
"""int event_reinit(event_base * base)
/tmp/event.h:292"""
event_dispatch = _libraries['libevent-1.4.so.2'].event_dispatch
event_dispatch.restype = c_int
event_dispatch.argtypes = []
event_dispatch.__doc__ = \
"""int event_dispatch()
/tmp/event.h:303"""
event_base_dispatch = _libraries['libevent-1.4.so.2'].event_base_dispatch
event_base_dispatch.restype = c_int
event_base_dispatch.argtypes = [POINTER(event_base)]
event_base_dispatch.__doc__ = \
"""int event_base_dispatch(event_base * p1)
/tmp/event.h:312"""
event_base_free = _libraries['libevent-1.4.so.2'].event_base_free
event_base_free.restype = None
event_base_free.argtypes = [POINTER(event_base)]
event_base_free.__doc__ = \
"""void event_base_free(event_base * p1)
/tmp/event.h:323"""
event_log_cb = CFUNCTYPE(None, c_int, STRING)
event_set_log_callback = _libraries['libevent-1.4.so.2'].event_set_log_callback
event_set_log_callback.restype = None
event_set_log_callback.argtypes = [event_log_cb]
event_set_log_callback.__doc__ = \
"""void event_set_log_callback(event_log_cb cb)
/tmp/event.h:338"""
event_base_set = _libraries['libevent-1.4.so.2'].event_base_set
event_base_set.restype = c_int
event_base_set.argtypes = [POINTER(event_base), POINTER(event)]
event_base_set.__doc__ = \
"""int event_base_set(event_base * p1, event * p2)
/tmp/event.h:346"""
event_loop = _libraries['libevent-1.4.so.2'].event_loop
event_loop.restype = c_int
event_loop.argtypes = [c_int]
event_loop.__doc__ = \
"""int event_loop(int p1)
/tmp/event.h:365"""
event_base_loop = _libraries['libevent-1.4.so.2'].event_base_loop
event_base_loop.restype = c_int
event_base_loop.argtypes = [POINTER(event_base), c_int]
event_base_loop.__doc__ = \
"""int event_base_loop(event_base * p1, int p2)
/tmp/event.h:377"""
class timeval(Structure):
    pass
event_loopexit = _libraries['libevent-1.4.so.2'].event_loopexit
event_loopexit.restype = c_int
event_loopexit.argtypes = [POINTER(timeval)]
event_loopexit.__doc__ = \
"""int event_loopexit(timeval * p1)
/tmp/event.h:392"""
event_base_loopexit = _libraries['libevent-1.4.so.2'].event_base_loopexit
event_base_loopexit.restype = c_int
event_base_loopexit.argtypes = [POINTER(event_base), POINTER(timeval)]
event_base_loopexit.__doc__ = \
"""int event_base_loopexit(event_base * p1, timeval * p2)
/tmp/event.h:409"""
event_loopbreak = _libraries['libevent-1.4.so.2'].event_loopbreak
event_loopbreak.restype = c_int
event_loopbreak.argtypes = []
event_loopbreak.__doc__ = \
"""int event_loopbreak()
/tmp/event.h:423"""
event_base_loopbreak = _libraries['libevent-1.4.so.2'].event_base_loopbreak
event_base_loopbreak.restype = c_int
event_base_loopbreak.argtypes = [POINTER(event_base)]
event_base_loopbreak.__doc__ = \
"""int event_base_loopbreak(event_base * p1)
/tmp/event.h:438"""
event_set = _libraries['libevent-1.4.so.2'].event_set
event_set.restype = None
event_set.argtypes = [POINTER(event), c_int, c_short, CFUNCTYPE(None, c_int, c_short, c_void_p), c_void_p]
event_set.__doc__ = \
"""void event_set(event * p1, int p2, short int p3, unknown * p4, void * p5)
/tmp/event.h:531"""
event_once = _libraries['libevent-1.4.so.2'].event_once
event_once.restype = c_int
event_once.argtypes = [c_int, c_short, CFUNCTYPE(None, c_int, c_short, c_void_p), c_void_p, POINTER(timeval)]
event_once.__doc__ = \
"""int event_once(int p1, short int p2, unknown * p3, void * p4, timeval * p5)
/tmp/event.h:551"""
event_base_once = _libraries['libevent-1.4.so.2'].event_base_once
event_base_once.restype = c_int
event_base_once.argtypes = [POINTER(event_base), c_int, c_short, CFUNCTYPE(None, c_int, c_short, c_void_p), c_void_p, POINTER(timeval)]
event_base_once.__doc__ = \
"""int event_base_once(event_base * p1, int p2, short int p3, unknown * p4, void * p5, timeval * p6)
/tmp/event.h:572"""
event_add = _libraries['libevent-1.4.so.2'].event_add
event_add.restype = c_int
event_add.argtypes = [POINTER(event), POINTER(timeval)]
event_add.__doc__ = \
"""int event_add(event * p1, timeval * p2)
/tmp/event.h:593"""
event_del = _libraries['libevent-1.4.so.2'].event_del
event_del.restype = c_int
event_del.argtypes = [POINTER(event)]
event_del.__doc__ = \
"""int event_del(event * p1)
/tmp/event.h:607"""
event_active = _libraries['libevent-1.4.so.2'].event_active
event_active.restype = None
event_active.argtypes = [POINTER(event), c_int, c_short]
event_active.__doc__ = \
"""void event_active(event * p1, int p2, short int p3)
/tmp/event.h:609"""
event_pending = _libraries['libevent-1.4.so.2'].event_pending
event_pending.restype = c_int
event_pending.argtypes = [POINTER(event), c_short, POINTER(timeval)]
event_pending.__doc__ = \
"""int event_pending(event * p1, short int p2, timeval * p3)
/tmp/event.h:623"""
event_get_version = _libraries['libevent-1.4.so.2'].event_get_version
event_get_version.restype = STRING
event_get_version.argtypes = []
event_get_version.__doc__ = \
"""unknown * event_get_version()
/tmp/event.h:648"""
event_get_method = _libraries['libevent-1.4.so.2'].event_get_method
event_get_method.restype = STRING
event_get_method.argtypes = []
event_get_method.__doc__ = \
"""unknown * event_get_method()
/tmp/event.h:656"""
event_priority_init = _libraries['libevent-1.4.so.2'].event_priority_init
event_priority_init.restype = c_int
event_priority_init.argtypes = [c_int]
event_priority_init.__doc__ = \
"""int event_priority_init(int p1)
/tmp/event.h:679"""
event_base_priority_init = _libraries['libevent-1.4.so.2'].event_base_priority_init
event_base_priority_init.restype = c_int
event_base_priority_init.argtypes = [POINTER(event_base), c_int]
event_base_priority_init.__doc__ = \
"""int event_base_priority_init(event_base * p1, int p2)
/tmp/event.h:692"""
event_priority_set = _libraries['libevent-1.4.so.2'].event_priority_set
event_priority_set.restype = c_int
event_priority_set.argtypes = [POINTER(event), c_int]
event_priority_set.__doc__ = \
"""int event_priority_set(event * p1, int p2)
/tmp/event.h:703"""
class event_watermark(Structure):
    pass
size_t = c_uint
event_watermark._fields_ = [
    ('low', size_t),
    ('high', size_t),
]
class evbuffer(Structure):
    pass
evbuffer_new = _libraries['libevent-1.4.so.2'].evbuffer_new
evbuffer_new.restype = POINTER(evbuffer)
evbuffer_new.argtypes = []
evbuffer_new.__doc__ = \
"""evbuffer * evbuffer_new()
/tmp/event.h:911"""
evbuffer_free = _libraries['libevent-1.4.so.2'].evbuffer_free
evbuffer_free.restype = None
evbuffer_free.argtypes = [POINTER(evbuffer)]
evbuffer_free.__doc__ = \
"""void evbuffer_free(evbuffer * p1)
/tmp/event.h:919"""
evbuffer_expand = _libraries['libevent-1.4.so.2'].evbuffer_expand
evbuffer_expand.restype = c_int
evbuffer_expand.argtypes = [POINTER(evbuffer), size_t]
evbuffer_expand.__doc__ = \
"""int evbuffer_expand(evbuffer * p1, size_t p2)
/tmp/event.h:931"""
evbuffer_add = _libraries['libevent-1.4.so.2'].evbuffer_add
evbuffer_add.restype = c_int
evbuffer_add.argtypes = [POINTER(evbuffer), c_void_p, size_t]
evbuffer_add.__doc__ = \
"""int evbuffer_add(evbuffer * p1, unknown * p2, size_t p3)
/tmp/event.h:941"""
evbuffer_remove = _libraries['libevent-1.4.so.2'].evbuffer_remove
evbuffer_remove.restype = c_int
evbuffer_remove.argtypes = [POINTER(evbuffer), c_void_p, size_t]
evbuffer_remove.__doc__ = \
"""int evbuffer_remove(evbuffer * p1, void * p2, size_t p3)
/tmp/event.h:953"""
evbuffer_readline = _libraries['libevent-1.4.so.2'].evbuffer_readline
evbuffer_readline.restype = STRING
evbuffer_readline.argtypes = [POINTER(evbuffer)]
evbuffer_readline.__doc__ = \
"""char * evbuffer_readline(evbuffer * p1)
/tmp/event.h:965"""
evbuffer_add_buffer = _libraries['libevent-1.4.so.2'].evbuffer_add_buffer
evbuffer_add_buffer.restype = c_int
evbuffer_add_buffer.argtypes = [POINTER(evbuffer), POINTER(evbuffer)]
evbuffer_add_buffer.__doc__ = \
"""int evbuffer_add_buffer(evbuffer * p1, evbuffer * p2)
/tmp/event.h:978"""
evbuffer_add_printf = _libraries['libevent-1.4.so.2'].evbuffer_add_printf
evbuffer_add_printf.restype = c_int
evbuffer_add_printf.argtypes = [POINTER(evbuffer), STRING]
evbuffer_add_printf.__doc__ = \
"""int evbuffer_add_printf(evbuffer * p1, unknown * fmt)
/tmp/event.h:993"""
__gnuc_va_list = STRING
va_list = __gnuc_va_list
evbuffer_add_vprintf = _libraries['libevent-1.4.so.2'].evbuffer_add_vprintf
evbuffer_add_vprintf.restype = c_int
evbuffer_add_vprintf.argtypes = [POINTER(evbuffer), STRING, va_list]
evbuffer_add_vprintf.__doc__ = \
"""int evbuffer_add_vprintf(evbuffer * p1, unknown * fmt, va_list ap)
/tmp/event.h:1004"""
evbuffer_drain = _libraries['libevent-1.4.so.2'].evbuffer_drain
evbuffer_drain.restype = None
evbuffer_drain.argtypes = [POINTER(evbuffer), size_t]
evbuffer_drain.__doc__ = \
"""void evbuffer_drain(evbuffer * p1, size_t p2)
/tmp/event.h:1014"""
evbuffer_write = _libraries['libevent-1.4.so.2'].evbuffer_write
evbuffer_write.restype = c_int
evbuffer_write.argtypes = [POINTER(evbuffer), c_int]
evbuffer_write.__doc__ = \
"""int evbuffer_write(evbuffer * p1, int p2)
/tmp/event.h:1027"""
evbuffer_read = _libraries['libevent-1.4.so.2'].evbuffer_read
evbuffer_read.restype = c_int
evbuffer_read.argtypes = [POINTER(evbuffer), c_int, c_int]
evbuffer_read.__doc__ = \
"""int evbuffer_read(evbuffer * p1, int p2, int p3)
/tmp/event.h:1039"""
__u_char = c_ubyte
u_char = __u_char
evbuffer_find = _libraries['libevent-1.4.so.2'].evbuffer_find
evbuffer_find.restype = POINTER(u_char)
evbuffer_find.argtypes = [POINTER(evbuffer), POINTER(u_char), size_t]
evbuffer_find.__doc__ = \
"""u_char * evbuffer_find(evbuffer * p1, unknown * p2, size_t p3)
/tmp/event.h:1050"""
evbuffer_setcb = _libraries['libevent-1.4.so.2'].evbuffer_setcb
evbuffer_setcb.restype = None
evbuffer_setcb.argtypes = [POINTER(evbuffer), CFUNCTYPE(None, POINTER(evbuffer), c_uint, c_uint, c_void_p), c_void_p]
evbuffer_setcb.__doc__ = \
"""void evbuffer_setcb(evbuffer * p1, unknown * p2, void * p3)
/tmp/event.h:1059"""
class evhttp(Structure):
    pass
evhttp_new = _libraries['libevent-1.4.so.2'].evhttp_new
evhttp_new.restype = POINTER(evhttp)
evhttp_new.argtypes = [POINTER(event_base)]
evhttp_new.__doc__ = \
"""evhttp * evhttp_new(event_base * base)
/tmp/evhttp.h:77"""
__u_short = c_ushort
u_short = __u_short
evhttp_bind_socket = _libraries['libevent-1.4.so.2'].evhttp_bind_socket
evhttp_bind_socket.restype = c_int
evhttp_bind_socket.argtypes = [POINTER(evhttp), STRING, u_short]
evhttp_bind_socket.__doc__ = \
"""int evhttp_bind_socket(evhttp * http, unknown * address, u_short port)
/tmp/evhttp.h:91"""
evhttp_free = _libraries['libevent-1.4.so.2'].evhttp_free
evhttp_free.restype = None
evhttp_free.argtypes = [POINTER(evhttp)]
evhttp_free.__doc__ = \
"""void evhttp_free(evhttp * http)
/tmp/evhttp.h:101"""
class evhttp_request(Structure):
    pass
evhttp_set_cb = _libraries['libevent-1.4.so.2'].evhttp_set_cb
evhttp_set_cb.restype = None
evhttp_set_cb.argtypes = [POINTER(evhttp), STRING, CFUNCTYPE(None, POINTER(evhttp_request), c_void_p), c_void_p]
evhttp_set_cb.__doc__ = \
"""void evhttp_set_cb(evhttp * p1, unknown * p2, unknown * p3, void * p4)
/tmp/evhttp.h:105"""
evhttp_del_cb = _libraries['libevent-1.4.so.2'].evhttp_del_cb
evhttp_del_cb.restype = c_int
evhttp_del_cb.argtypes = [POINTER(evhttp), STRING]
evhttp_del_cb.__doc__ = \
"""int evhttp_del_cb(evhttp * p1, unknown * p2)
/tmp/evhttp.h:108"""
evhttp_set_gencb = _libraries['libevent-1.4.so.2'].evhttp_set_gencb
evhttp_set_gencb.restype = None
evhttp_set_gencb.argtypes = [POINTER(evhttp), CFUNCTYPE(None, POINTER(evhttp_request), c_void_p), c_void_p]
evhttp_set_gencb.__doc__ = \
"""void evhttp_set_gencb(evhttp * p1, unknown * p2, void * p3)
/tmp/evhttp.h:113"""
evhttp_set_timeout = _libraries['libevent-1.4.so.2'].evhttp_set_timeout
evhttp_set_timeout.restype = None
evhttp_set_timeout.argtypes = [POINTER(evhttp), c_int]
evhttp_set_timeout.__doc__ = \
"""void evhttp_set_timeout(evhttp * p1, int timeout_in_secs)
/tmp/evhttp.h:121"""
evhttp_send_error = _libraries['libevent-1.4.so.2'].evhttp_send_error
evhttp_send_error.restype = None
evhttp_send_error.argtypes = [POINTER(evhttp_request), c_int, STRING]
evhttp_send_error.__doc__ = \
"""void evhttp_send_error(evhttp_request * req, int error, unknown * reason)
/tmp/evhttp.h:133"""
evhttp_send_reply = _libraries['libevent-1.4.so.2'].evhttp_send_reply
evhttp_send_reply.restype = None
evhttp_send_reply.argtypes = [POINTER(evhttp_request), c_int, STRING, POINTER(evbuffer)]
evhttp_send_reply.__doc__ = \
"""void evhttp_send_reply(evhttp_request * req, int code, unknown * reason, evbuffer * databuf)
/tmp/evhttp.h:144"""
evhttp_send_reply_start = _libraries['libevent-1.4.so.2'].evhttp_send_reply_start
evhttp_send_reply_start.restype = None
evhttp_send_reply_start.argtypes = [POINTER(evhttp_request), c_int, STRING]
evhttp_send_reply_start.__doc__ = \
"""void evhttp_send_reply_start(evhttp_request * p1, int p2, unknown * p3)
/tmp/evhttp.h:147"""
evhttp_send_reply_chunk = _libraries['libevent-1.4.so.2'].evhttp_send_reply_chunk
evhttp_send_reply_chunk.restype = None
evhttp_send_reply_chunk.argtypes = [POINTER(evhttp_request), POINTER(evbuffer)]
evhttp_send_reply_chunk.__doc__ = \
"""void evhttp_send_reply_chunk(evhttp_request * p1, evbuffer * p2)
/tmp/evhttp.h:148"""
evhttp_send_reply_end = _libraries['libevent-1.4.so.2'].evhttp_send_reply_end
evhttp_send_reply_end.restype = None
evhttp_send_reply_end.argtypes = [POINTER(evhttp_request)]
evhttp_send_reply_end.__doc__ = \
"""void evhttp_send_reply_end(evhttp_request * p1)
/tmp/evhttp.h:149"""
evhttp_start = _libraries['libevent-1.4.so.2'].evhttp_start
evhttp_start.restype = POINTER(evhttp)
evhttp_start.argtypes = [STRING, u_short]
evhttp_start.__doc__ = \
"""evhttp * evhttp_start(unknown * address, u_short port)
/tmp/evhttp.h:160"""

# values for enumeration 'evhttp_cmd_type'
evhttp_cmd_type = c_int # enum

# values for enumeration 'evhttp_request_kind'
evhttp_request_kind = c_int # enum
class N14evhttp_request4DOT_27E(Structure):
    pass
N14evhttp_request4DOT_27E._fields_ = [
    ('tqe_next', POINTER(evhttp_request)),
    ('tqe_prev', POINTER(POINTER(evhttp_request))),
]
class evhttp_connection(Structure):
    pass
class evkeyvalq(Structure):
    pass
evhttp_request._fields_ = [
    ('next', N14evhttp_request4DOT_27E),
    ('evcon', POINTER(evhttp_connection)),
    ('flags', c_int),
    ('input_headers', POINTER(evkeyvalq)),
    ('output_headers', POINTER(evkeyvalq)),
    ('remote_host', STRING),
    ('remote_port', u_short),
    ('kind', evhttp_request_kind),
    ('type', evhttp_cmd_type),
    ('uri', STRING),
    ('major', c_char),
    ('minor', c_char),
    ('got_firstline', c_int),
    ('response_code', c_int),
    ('response_code_line', STRING),
    ('input_buffer', POINTER(evbuffer)),
    ('ntoread', c_int),
    ('chunked', c_int),
    ('output_buffer', POINTER(evbuffer)),
    ('cb', CFUNCTYPE(None, POINTER(evhttp_request), c_void_p)),
    ('cb_arg', c_void_p),
    ('chunk_cb', CFUNCTYPE(None, POINTER(evhttp_request), c_void_p)),
]
evhttp_request_new = _libraries['libevent-1.4.so.2'].evhttp_request_new
evhttp_request_new.restype = POINTER(evhttp_request)
evhttp_request_new.argtypes = [CFUNCTYPE(None, POINTER(evhttp_request), c_void_p), c_void_p]
evhttp_request_new.__doc__ = \
"""evhttp_request * evhttp_request_new(unknown * cb, void * arg)
/tmp/evhttp.h:233"""
evhttp_request_set_chunked_cb = _libraries['libevent-1.4.so.2'].evhttp_request_set_chunked_cb
evhttp_request_set_chunked_cb.restype = None
evhttp_request_set_chunked_cb.argtypes = [POINTER(evhttp_request), CFUNCTYPE(None, POINTER(evhttp_request), c_void_p)]
evhttp_request_set_chunked_cb.__doc__ = \
"""void evhttp_request_set_chunked_cb(evhttp_request * p1, unknown * cb)
/tmp/evhttp.h:237"""
evhttp_request_free = _libraries['libevent-1.4.so.2'].evhttp_request_free
evhttp_request_free.restype = None
evhttp_request_free.argtypes = [POINTER(evhttp_request)]
evhttp_request_free.__doc__ = \
"""void evhttp_request_free(evhttp_request * req)
/tmp/evhttp.h:240"""
evhttp_connection_new = _libraries['libevent-1.4.so.2'].evhttp_connection_new
evhttp_connection_new.restype = POINTER(evhttp_connection)
evhttp_connection_new.argtypes = [STRING, c_ushort]
evhttp_connection_new.__doc__ = \
"""evhttp_connection * evhttp_connection_new(unknown * address, short unsigned int port)
/tmp/evhttp.h:248"""
evhttp_connection_free = _libraries['libevent-1.4.so.2'].evhttp_connection_free
evhttp_connection_free.restype = None
evhttp_connection_free.argtypes = [POINTER(evhttp_connection)]
evhttp_connection_free.__doc__ = \
"""void evhttp_connection_free(evhttp_connection * evcon)
/tmp/evhttp.h:251"""
evhttp_connection_set_local_address = _libraries['libevent-1.4.so.2'].evhttp_connection_set_local_address
evhttp_connection_set_local_address.restype = None
evhttp_connection_set_local_address.argtypes = [POINTER(evhttp_connection), STRING]
evhttp_connection_set_local_address.__doc__ = \
"""void evhttp_connection_set_local_address(evhttp_connection * evcon, unknown * address)
/tmp/evhttp.h:255"""
evhttp_connection_set_timeout = _libraries['libevent-1.4.so.2'].evhttp_connection_set_timeout
evhttp_connection_set_timeout.restype = None
evhttp_connection_set_timeout.argtypes = [POINTER(evhttp_connection), c_int]
evhttp_connection_set_timeout.__doc__ = \
"""void evhttp_connection_set_timeout(evhttp_connection * evcon, int timeout_in_secs)
/tmp/evhttp.h:259"""
evhttp_connection_set_retries = _libraries['libevent-1.4.so.2'].evhttp_connection_set_retries
evhttp_connection_set_retries.restype = None
evhttp_connection_set_retries.argtypes = [POINTER(evhttp_connection), c_int]
evhttp_connection_set_retries.__doc__ = \
"""void evhttp_connection_set_retries(evhttp_connection * evcon, int retry_max)
/tmp/evhttp.h:263"""
evhttp_connection_set_closecb = _libraries['libevent-1.4.so.2'].evhttp_connection_set_closecb
evhttp_connection_set_closecb.restype = None
evhttp_connection_set_closecb.argtypes = [POINTER(evhttp_connection), CFUNCTYPE(None, POINTER(evhttp_connection), c_void_p), c_void_p]
evhttp_connection_set_closecb.__doc__ = \
"""void evhttp_connection_set_closecb(evhttp_connection * evcon, unknown * p2, void * p3)
/tmp/evhttp.h:267"""
evhttp_connection_set_base = _libraries['libevent-1.4.so.2'].evhttp_connection_set_base
evhttp_connection_set_base.restype = None
evhttp_connection_set_base.argtypes = [POINTER(evhttp_connection), POINTER(event_base)]
evhttp_connection_set_base.__doc__ = \
"""void evhttp_connection_set_base(evhttp_connection * evcon, event_base * base)
/tmp/evhttp.h:274"""
evhttp_connection_get_peer = _libraries['libevent-1.4.so.2'].evhttp_connection_get_peer
evhttp_connection_get_peer.restype = None
evhttp_connection_get_peer.argtypes = [POINTER(evhttp_connection), POINTER(STRING), POINTER(u_short)]
evhttp_connection_get_peer.__doc__ = \
"""void evhttp_connection_get_peer(evhttp_connection * evcon, char * * address, u_short * port)
/tmp/evhttp.h:278"""
evhttp_make_request = _libraries['libevent-1.4.so.2'].evhttp_make_request
evhttp_make_request.restype = c_int
evhttp_make_request.argtypes = [POINTER(evhttp_connection), POINTER(evhttp_request), evhttp_cmd_type, STRING]
evhttp_make_request.__doc__ = \
"""int evhttp_make_request(evhttp_connection * evcon, evhttp_request * req, evhttp_cmd_type type, unknown * uri)
/tmp/evhttp.h:283"""
evhttp_request_uri = _libraries['libevent-1.4.so.2'].evhttp_request_uri
evhttp_request_uri.restype = STRING
evhttp_request_uri.argtypes = [POINTER(evhttp_request)]
evhttp_request_uri.__doc__ = \
"""unknown * evhttp_request_uri(evhttp_request * req)
/tmp/evhttp.h:285"""
class evkeyval(Structure):
    pass
evkeyvalq._fields_ = [
    ('tqh_first', POINTER(evkeyval)),
    ('tqh_last', POINTER(POINTER(evkeyval))),
]
evhttp_find_header = _libraries['libevent-1.4.so.2'].evhttp_find_header
evhttp_find_header.restype = STRING
evhttp_find_header.argtypes = [POINTER(evkeyvalq), STRING]
evhttp_find_header.__doc__ = \
"""unknown * evhttp_find_header(unknown * p1, unknown * p2)
/tmp/evhttp.h:289"""
evhttp_remove_header = _libraries['libevent-1.4.so.2'].evhttp_remove_header
evhttp_remove_header.restype = c_int
evhttp_remove_header.argtypes = [POINTER(evkeyvalq), STRING]
evhttp_remove_header.__doc__ = \
"""int evhttp_remove_header(evkeyvalq * p1, unknown * p2)
/tmp/evhttp.h:290"""
evhttp_add_header = _libraries['libevent-1.4.so.2'].evhttp_add_header
evhttp_add_header.restype = c_int
evhttp_add_header.argtypes = [POINTER(evkeyvalq), STRING, STRING]
evhttp_add_header.__doc__ = \
"""int evhttp_add_header(evkeyvalq * p1, unknown * p2, unknown * p3)
/tmp/evhttp.h:291"""
evhttp_clear_headers = _libraries['libevent-1.4.so.2'].evhttp_clear_headers
evhttp_clear_headers.restype = None
evhttp_clear_headers.argtypes = [POINTER(evkeyvalq)]
evhttp_clear_headers.__doc__ = \
"""void evhttp_clear_headers(evkeyvalq * p1)
/tmp/evhttp.h:292"""
evhttp_encode_uri = _libraries['libevent-1.4.so.2'].evhttp_encode_uri
evhttp_encode_uri.restype = STRING
evhttp_encode_uri.argtypes = [STRING]
evhttp_encode_uri.__doc__ = \
"""char * evhttp_encode_uri(unknown * uri)
/tmp/evhttp.h:305"""
evhttp_decode_uri = _libraries['libevent-1.4.so.2'].evhttp_decode_uri
evhttp_decode_uri.restype = STRING
evhttp_decode_uri.argtypes = [STRING]
evhttp_decode_uri.__doc__ = \
"""char * evhttp_decode_uri(unknown * uri)
/tmp/evhttp.h:316"""
evhttp_parse_query = _libraries['libevent-1.4.so.2'].evhttp_parse_query
evhttp_parse_query.restype = None
evhttp_parse_query.argtypes = [STRING, POINTER(evkeyvalq)]
evhttp_parse_query.__doc__ = \
"""void evhttp_parse_query(unknown * uri, evkeyvalq * p2)
/tmp/evhttp.h:324"""
evhttp_htmlescape = _libraries['libevent-1.4.so.2'].evhttp_htmlescape
evhttp_htmlescape.restype = STRING
evhttp_htmlescape.argtypes = [STRING]
evhttp_htmlescape.__doc__ = \
"""char * evhttp_htmlescape(unknown * html)
/tmp/evhttp.h:338"""

# values for enumeration 'evhttp_connection_error'
evhttp_connection_error = c_int # enum

# values for enumeration 'evhttp_connection_state'
evhttp_connection_state = c_int # enum
class N17evhttp_connection4DOT_28E(Structure):
    pass
N17evhttp_connection4DOT_28E._fields_ = [
    ('tqe_next', POINTER(evhttp_connection)),
    ('tqe_prev', POINTER(POINTER(evhttp_connection))),
]
class N5event4DOT_23E(Structure):
    pass
N5event4DOT_23E._fields_ = [
    ('tqe_next', POINTER(event)),
    ('tqe_prev', POINTER(POINTER(event))),
]
class N5event4DOT_24E(Structure):
    pass
N5event4DOT_24E._fields_ = [
    ('tqe_next', POINTER(event)),
    ('tqe_prev', POINTER(POINTER(event))),
]
class N5event4DOT_25E(Structure):
    pass
N5event4DOT_25E._fields_ = [
    ('tqe_next', POINTER(event)),
    ('tqe_prev', POINTER(POINTER(event))),
]
__time_t = c_long
__suseconds_t = c_long
timeval._fields_ = [
    ('tv_sec', __time_t),
    ('tv_usec', __suseconds_t),
]
event._fields_ = [
    ('ev_next', N5event4DOT_23E),
    ('ev_active_next', N5event4DOT_24E),
    ('ev_signal_next', N5event4DOT_25E),
    ('min_heap_idx', c_uint),
    ('ev_base', POINTER(event_base)),
    ('ev_fd', c_int),
    ('ev_events', c_short),
    ('ev_ncalls', c_short),
    ('ev_pncalls', POINTER(c_short)),
    ('ev_timeout', timeval),
    ('ev_pri', c_int),
    ('ev_callback', CFUNCTYPE(None, c_int, c_short, c_void_p)),
    ('ev_arg', c_void_p),
    ('ev_res', c_int),
    ('ev_flags', c_int),
]
class evcon_requestq(Structure):
    pass
evcon_requestq._fields_ = [
    ('tqh_first', POINTER(evhttp_request)),
    ('tqh_last', POINTER(POINTER(evhttp_request))),
]
evhttp_connection._fields_ = [
    ('next', N17evhttp_connection4DOT_28E),
    ('fd', c_int),
    ('ev', event),
    ('close_ev', event),
    ('input_buffer', POINTER(evbuffer)),
    ('output_buffer', POINTER(evbuffer)),
    ('bind_address', STRING),
    ('address', STRING),
    ('port', u_short),
    ('flags', c_int),
    ('timeout', c_int),
    ('retry_cnt', c_int),
    ('retry_max', c_int),
    ('state', evhttp_connection_state),
    ('http_server', POINTER(evhttp)),
    ('requests', evcon_requestq),
    ('cb', CFUNCTYPE(None, POINTER(evhttp_connection), c_void_p)),
    ('cb_arg', c_void_p),
    ('closecb', CFUNCTYPE(None, POINTER(evhttp_connection), c_void_p)),
    ('closecb_arg', c_void_p),
    ('base', POINTER(event_base)),
]
class evhttp_cb(Structure):
    pass
class N9evhttp_cb4DOT_29E(Structure):
    pass
N9evhttp_cb4DOT_29E._fields_ = [
    ('tqe_next', POINTER(evhttp_cb)),
    ('tqe_prev', POINTER(POINTER(evhttp_cb))),
]
evhttp_cb._fields_ = [
    ('next', N9evhttp_cb4DOT_29E),
    ('what', STRING),
    ('cb', CFUNCTYPE(None, POINTER(evhttp_request), c_void_p)),
    ('cbarg', c_void_p),
]
class httpcbq(Structure):
    pass
httpcbq._fields_ = [
    ('tqh_first', POINTER(evhttp_cb)),
    ('tqh_last', POINTER(POINTER(evhttp_cb))),
]
class evconq(Structure):
    pass
evconq._fields_ = [
    ('tqh_first', POINTER(evhttp_connection)),
    ('tqh_last', POINTER(POINTER(evhttp_connection))),
]
evhttp._fields_ = [
    ('bind_ev', event),
    ('callbacks', httpcbq),
    ('connections', evconq),
    ('timeout', c_int),
    ('gencb', CFUNCTYPE(None, POINTER(evhttp_request), c_void_p)),
    ('gencbarg', c_void_p),
    ('base', POINTER(event_base)),
]
evhttp_connection_reset = _libraries['libevent-1.4.so.2'].evhttp_connection_reset
evhttp_connection_reset.restype = None
evhttp_connection_reset.argtypes = [POINTER(evhttp_connection)]
evhttp_connection_reset.__doc__ = \
"""void evhttp_connection_reset(evhttp_connection * p1)
/tmp/http-internal.h:107"""
evhttp_connection_connect = _libraries['libevent-1.4.so.2'].evhttp_connection_connect
evhttp_connection_connect.restype = c_int
evhttp_connection_connect.argtypes = [POINTER(evhttp_connection)]
evhttp_connection_connect.__doc__ = \
"""int evhttp_connection_connect(evhttp_connection * p1)
/tmp/http-internal.h:110"""
evhttp_connection_fail = _libraries['libevent-1.4.so.2'].evhttp_connection_fail
evhttp_connection_fail.restype = None
evhttp_connection_fail.argtypes = [POINTER(evhttp_connection), evhttp_connection_error]
evhttp_connection_fail.__doc__ = \
"""void evhttp_connection_fail(evhttp_connection * p1, evhttp_connection_error error)
/tmp/http-internal.h:114"""
class sockaddr(Structure):
    pass
__socklen_t = c_uint
socklen_t = __socklen_t
evhttp_get_request = _libraries['libevent-1.4.so.2'].evhttp_get_request
evhttp_get_request.restype = None
evhttp_get_request.argtypes = [POINTER(evhttp), c_int, POINTER(sockaddr), socklen_t]
evhttp_get_request.__doc__ = \
"""void evhttp_get_request(evhttp * p1, int p2, sockaddr * p3, socklen_t p4)
/tmp/http-internal.h:116"""
evhttp_hostportfile = _libraries['libevent-1.4.so.2'].evhttp_hostportfile
evhttp_hostportfile.restype = c_int
evhttp_hostportfile.argtypes = [STRING, POINTER(STRING), POINTER(u_short), POINTER(STRING)]
evhttp_hostportfile.__doc__ = \
"""int evhttp_hostportfile(char * p1, char * * p2, u_short * p3, char * * p4)
/tmp/http-internal.h:118"""
evhttp_parse_lines = _libraries['libevent-1.4.so.2'].evhttp_parse_lines
evhttp_parse_lines.restype = c_int
evhttp_parse_lines.argtypes = [POINTER(evhttp_request), POINTER(evbuffer)]
evhttp_parse_lines.__doc__ = \
"""int evhttp_parse_lines(evhttp_request * p1, evbuffer * p2)
/tmp/http-internal.h:120"""
evhttp_start_read = _libraries['libevent-1.4.so.2'].evhttp_start_read
evhttp_start_read.restype = None
evhttp_start_read.argtypes = [POINTER(evhttp_connection)]
evhttp_start_read.__doc__ = \
"""void evhttp_start_read(evhttp_connection * p1)
/tmp/http-internal.h:122"""
evhttp_read_header = _libraries['libevent-1.4.so.2'].evhttp_read_header
evhttp_read_header.restype = None
evhttp_read_header.argtypes = [c_int, c_short, c_void_p]
evhttp_read_header.__doc__ = \
"""void evhttp_read_header(int p1, short int p2, void * p3)
/tmp/http-internal.h:123"""
evhttp_make_header = _libraries['libevent-1.4.so.2'].evhttp_make_header
evhttp_make_header.restype = None
evhttp_make_header.argtypes = [POINTER(evhttp_connection), POINTER(evhttp_request)]
evhttp_make_header.__doc__ = \
"""void evhttp_make_header(evhttp_connection * p1, evhttp_request * p2)
/tmp/http-internal.h:124"""
evhttp_write_buffer = _libraries['libevent-1.4.so.2'].evhttp_write_buffer
evhttp_write_buffer.restype = None
evhttp_write_buffer.argtypes = [POINTER(evhttp_connection), CFUNCTYPE(None, POINTER(evhttp_connection), c_void_p), c_void_p]
evhttp_write_buffer.__doc__ = \
"""void evhttp_write_buffer(evhttp_connection * p1, unknown * p2, void * p3)
/tmp/http-internal.h:127"""
evhttp_response_code = _libraries['libevent-1.4.so.2'].evhttp_response_code
evhttp_response_code.restype = None
evhttp_response_code.argtypes = [POINTER(evhttp_request), c_int, STRING]
evhttp_response_code.__doc__ = \
"""void evhttp_response_code(evhttp_request * p1, int p2, unknown * p3)
/tmp/http-internal.h:130"""
evhttp_send_page = _libraries['libevent-1.4.so.2'].evhttp_send_page
evhttp_send_page.restype = None
evhttp_send_page.argtypes = [POINTER(evhttp_request), POINTER(evbuffer)]
evhttp_send_page.__doc__ = \
"""void evhttp_send_page(evhttp_request * p1, evbuffer * p2)
/tmp/http-internal.h:131"""
EVLOOP_NONBLOCK = 2 # Variable c_int
EV_TIMEOUT = 1 # Variable c_int
EVBUFFER_READ = 1 # Variable c_int
EVHTTP_CON_INCOMING = 1 # Variable c_int
EVLIST_ACTIVE = 8 # Variable c_int
EVLIST_ALL = 61599 # Variable c_int
EVHTTP_CON_CLOSEDETECT = 4 # Variable c_int
EV_PERSIST = 16 # Variable c_int
EVLIST_SIGNAL = 4 # Variable c_int
EV_WRITE = 4 # Variable c_int
EV_READ = 2 # Variable c_int
EVLIST_INSERTED = 2 # Variable c_int
EVHTTP_PROXY_REQUEST = 2 # Variable c_int
EVLIST_INIT = 128 # Variable c_int
EVHTTP_REQ_OWN_CONNECTION = 1 # Variable c_int
EV_SIGNAL = 8 # Variable c_int
EVBUFFER_ERROR = 32 # Variable c_int
EVBUFFER_TIMEOUT = 64 # Variable c_int
EVLIST_INTERNAL = 16 # Variable c_int
EVLOOP_ONCE = 1 # Variable c_int
EVHTTP_CON_OUTGOING = 2 # Variable c_int
EVBUFFER_WRITE = 2 # Variable c_int
EVBUFFER_EOF = 16 # Variable c_int
EVLIST_TIMEOUT = 1 # Variable c_int
class N8evkeyval4DOT_26E(Structure):
    pass
N8evkeyval4DOT_26E._fields_ = [
    ('tqe_next', POINTER(evkeyval)),
    ('tqe_prev', POINTER(POINTER(evkeyval))),
]
evkeyval._fields_ = [
    ('next', N8evkeyval4DOT_26E),
    ('key', STRING),
    ('value', STRING),
]
evbuffer._fields_ = [
    ('buffer', POINTER(u_char)),
    ('orig_buffer', POINTER(u_char)),
    ('misalign', size_t),
    ('totallen', size_t),
    ('off', size_t),
    ('cb', CFUNCTYPE(None, POINTER(evbuffer), c_uint, c_uint, c_void_p)),
    ('cbarg', c_void_p),
]
sa_family_t = c_ushort
sockaddr._fields_ = [
    ('sa_family', sa_family_t),
    ('sa_data', c_char * 14),
]
__all__ = ['EVLIST_INTERNAL', 'evhttp_write_buffer', 'evhttp_del_cb',
           'evhttp_connection_connect', 'EVLOOP_NONBLOCK',
           'signal_del', 'N5event4DOT_24E', 'socklen_t', 'evbuffer',
           'evhttp_send_page', 'EVHTTP_PROXY_REQUEST', 'size_t',
           'evhttp_request', 'evhttp_read_header',
           'event_priority_init', 'EVCON_CONNECTED', 'evbuffer_free',
           'evhttp_htmlescape', 'evbuffer_setcb', 'event_get_version',
           'N8evkeyval4DOT_26E', 'evhttp_connection_new',
           'signal_set', 'evhttp_response_code',
           'evhttp_connection_get_peer',
           'evhttp_connection_set_retries', 'evhttp_add_header',
           'EV_WRITE', 'event_get_method', 'evhttp_connection',
           'EVHTTP_RESPONSE', 'event_dispatch',
           'N14evhttp_request4DOT_27E',
           'evhttp_request_set_chunked_cb', 'EVCON_DISCONNECTED',
           'N5event4DOT_25E', 'u_char', 'EVCON_HTTP_EOF',
           'evbuffer_drain', 'EVLOOP_ONCE', 'evhttp_connection_error',
           'EVBUFFER_READ', '__time_t', 'event_base_priority_init',
           'EV_PERSIST', 'evhttp_encode_uri', 'event_list',
           'evtimer_pending', 'EVCON_HTTP_INVALID_HEADER',
           'evhttp_decode_uri', 'event_base_free', 'event_pending',
           'evhttp_connection_set_base', 'evhttp_start_read',
           'EVLIST_ACTIVE', 'evhttp_send_reply_end',
           'event_base_loop', 'evhttp_hostportfile', 'sa_family_t',
           'EVHTTP_REQ_HEAD', 'event', 'evhttp_bind_socket',
           'evhttp_connection_fail', 'evcon_requestq',
           'evhttp_send_reply', 'evhttp_request_uri',
           'event_base_loopbreak', 'evhttp_remove_header', 'evkeyval',
           'EVUTIL_CLOSESOCKET', 'EVBUFFER_WRITE', 'va_list',
           'evtimer_set', 'evhttp_set_gencb', 'event_base_new',
           'EVBUFFER_TIMEOUT', 'event_base_dispatch', 'event_del',
           'evbuffer_add_buffer', '__gnuc_va_list', 'evbuffer_write',
           'event_base_loopexit', 'EV_SIGNAL', 'evhttp_request_new',
           'EVHTTP_REQ_OWN_CONNECTION', 'evtimer_add', 'event_log_cb',
           'evhttp_connection_state', 'evbuffer_new',
           'evhttp_request_kind', 'evhttp_find_header', 'httpcbq',
           'EVBUFFER_EOF', 'event_priority_set', 'event_once',
           'EVLIST_INIT', 'evhttp_parse_query', 'evbuffer_read',
           'evhttp_connection_set_closecb', 'evhttp_send_reply_chunk',
           'evbuffer_remove', 'EVLIST_INSERTED',
           'EVHTTP_CON_CLOSEDETECT', 'evhttp_connection_set_timeout',
           'evhttp_send_reply_start', 'event_watermark',
           'evbuffer_expand', 'evkeyvalq', 'N5event4DOT_23E',
           'EVCON_HTTP_TIMEOUT', 'event_add', 'EVHTTP_CON_INCOMING',
           'event_base_once', '__u_char', 'EV_TIMEOUT',
           'evbuffer_add_vprintf', 'N17evhttp_connection4DOT_28E',
           'evhttp_connection_free', '__suseconds_t',
           'evhttp_set_timeout', 'evhttp_make_header',
           'evbuffer_find', 'evhttp_get_request', 'event_loopexit',
           'event_reinit', 'event_init', 'event_base_set', 'sockaddr',
           'evhttp_clear_headers', 'evhttp_request_free',
           'N9evhttp_cb4DOT_29E', 'EVLIST_TIMEOUT', 'event_loop',
           'evhttp_parse_lines', 'evhttp_start', 'evtimer_del',
           'evhttp', 'u_short', 'evhttp_cmd_type', 'signal_pending',
           'evbuffer_add', 'event_set', 'event_set_log_callback',
           'EV_READ', 'EVLIST_SIGNAL', 'timeval', '__u_short',
           'evconq', 'evhttp_set_cb', 'EVBUFFER_ERROR', 'EVLIST_ALL',
           'EVUTIL_SOCKET_ERROR', 'event_base', 'evhttp_new',
           'EVHTTP_CON_OUTGOING', 'evbuffer_readline',
           'evhttp_send_error', 'evhttp_connection_set_local_address',
           'event_active', 'evhttp_connection_reset', 'evhttp_free',
           'EVHTTP_REQ_GET', 'EVCON_CONNECTING', 'event_loopbreak',
           '__socklen_t', 'EVHTTP_REQ_POST', 'evhttp_make_request',
           'signal_add', 'evhttp_cb', 'evbuffer_add_printf',
           'EVHTTP_REQUEST']
