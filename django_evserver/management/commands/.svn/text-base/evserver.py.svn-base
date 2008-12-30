# -*- coding: utf-8 -*-
# pylint: disable-msg=C0301

from optparse import make_option
import sys
import os

import django
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('-v', '--verbosity', action='count', dest='verbosity', default=0,
            help='Verbosity. Add more -v to be more verbose [default: %default]'),
        make_option('--noreload', action='store_false', dest='use_reloader', default=True,
            help='Tells Django to NOT use the auto-reloader.'),
    )
    help = 'Starts Libevent based web server for your project.'
    args = '[options] [optional port number, or ipaddr:port]'

    requires_model_validation = True

    def handle(self, addrport='', *args, **options):
        verbosity    = options['verbosity']
        use_reloader = options['use_reloader']
        
        if args:
            raise CommandError('Usage is evserver %s' % self.args)
        
        if not addrport:
            addr = ''
            port = '8000'
        else:
            try:
                addr, port = addrport.split(':')
            except ValueError:
                addr, port = '', addrport
        if not addr:
            addr = '127.0.0.1'
        
        if not port.isdigit():
            raise CommandError("%r is not a valid port number." % port)
        
        port = int(port)
        
        quit_command = (sys.platform == 'win32') and 'CTRL-BREAK' or 'CONTROL-C'

        def inner_run():
            from django.conf import settings
            print "Validating models..."
            self.validate(display_num_errors=True)
            print "\nDjango version %s, using settings %r" % (django.get_version(), settings.SETTINGS_MODULE)
            print "Development server is running at http://%s:%s/" % (addr, port)
            print "Quit the server with %s." % quit_command
            try:
                import django_evserver.server
                django_evserver.server.main(addr, port)
                os._exit(1)
            except KeyboardInterrupt:
                sys.exit(0)
        
        if use_reloader:
            from django.utils import autoreload
            autoreload.main(inner_run)
        else:
            inner_run()
