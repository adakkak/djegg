#!/bin/sh
#
# generate ctypes_event.py
# 
# needs: ctypeslib, gccxml
#
LIBEVENT="$HOME/plucha/src/libevent"

cd /tmp
cp /usr/include/event.h event.h
cp $LIBEVENT/http-internal.h .

cat > evhttp.h << EOF
#ifndef TAILQ_ENTRY
#define _EVENT_DEFINED_TQENTRY
#define TAILQ_ENTRY(type)                                               \
struct {                                                                \
        struct type *tqe_next;  /* next element */                      \
        struct type **tqe_prev; /* address of previous next element */  \
}
#endif /* !TAILQ_ENTRY */
EOF
cat /usr/include/evhttp.h >> evhttp.h



cat > d.h << EOF
extern "C" {
#import <stdlib.h>
#import <sys/queue.h>
#import <sys/socket.h>
#import "event.h"
#import "evhttp.h"
#import "http-internal.h"
}
EOF
h2xml.py d.h -o d.xml -q -c
cat >ctypes_event.py << EOF
import ctypes
c_longdouble = ctypes.c_double
EOF
xml2py.py -levent -d d.xml -r "(event_|signal_|evbuffer_|evhttp|evtimer|EV).*" >> ctypes_event.py

