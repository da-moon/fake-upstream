#!/usr/bin/env python3
from upstream import __version__
from upstream.util.log import *
from upstream.util.cli import *
# from upstream.server.server import Server
from flasgger import Swagger
from flask import Flask, render_template
from werkzeug.serving import run_simple
try:
    from werkzeug.middleware.dispatcher import DispatcherMiddleware
except ImportError:
    from werkzeug.wsgi import DispatcherMiddleware

from functools import lru_cache
import os
import logging
import sys
from collections import OrderedDict
import upstream.defaults.loadbalancer.loadbalancer as default_upstream

LOGGER = logging.getLogger(__name__)
# use logger to print flask run messages
cli = sys.modules['flask.cli']
cli.show_server_banner = lambda *x: LOGGER.debug(x)

def __server_cli_entrypoint__(args):
    """
    this it the main function that uses starts the origin server
    """
    LOGGER.trace("__server_cli_entrypoint__() - function called")
    port = args.get('port_flag', 9090)
    try:
        port = int(port)
    except ValueError:
        LOOGER.error(
            "parsed 'port' value ('{}') cannot be converted to int.".format(port))
        sys.exit(-1)
    host = args.get('host_flag', "0.0.0.0")
    reloader = args.get('reloader_flag', False)
    try:
        reloader = bool(reloader)
    except ValueError:
        LOOGER.error(
            "parsed 'reloader' value ('{}') cannot be converted to bool.".format(reloader))
        sys.exit(-1)

    debug = args.get('debug_flag', False)
    try:
        debug = bool(debug)
    except ValueError:
        LOOGER.error(
            "parsed 'debug' value ('{}') cannot be converted to bool.".format(debug))
        sys.exit(-1)
    LOGGER.debug(
        f"__server_cli_entrypoint__() - parsed arguments : "
        f"host={host} "
        f"port={port} "
        f"reloader={reloader} "
        f"debug={debug} ")
    try:

        targets = [default_upstream]
        upstreams = OrderedDict({
            '/{0}'.format(mod.__name__.split('.')[-1]): mod
            for mod in sorted(targets, key=lambda x: x.__name__)
        })
        app = Flask(__name__)

        @app.route('/')
        def index():
            return render_template('flasgger.html',
                                   upstreams=upstreams,
                                   version=__version__)

        for upstream, mod in upstreams.items():
            if hasattr(mod.app, 'swag'):
                mod.app.swag.config['basePath'] = upstream
            LOGGER.warn(upstream)
        server = DispatcherMiddleware(
            app,
            {name: mod.app for name, mod in upstreams.items()}
        )

        run_simple(
            host,
            port,
            server,
            reloader,
            debug,
        )

    except Exception as e:
        # handling exception
        LOGGER.error("cannot start server to error : {}".format(e))
        sys.exit(-1)


def configure_parser(sub_parsers):
    """
    Get the argument parser for server subcommand
    this function customizes flags and parameters of server subcommand
    it assigns default function to each subcommand which gets executed when subcommand runs
    """
    server_parser = sub_parsers.add_parser(
        'server',
        description='starts mock upstream server',
        help='server subcommand')

    # setting server subcommand flags
    server_parser.add_argument(
        '-p',
        '--port',
        type=int,
        default=9090,
        dest='port_flag',
        help='Default port the server binds to.(default: 9090)',
    )

    # setting server subcommand flags
    server_parser.add_argument(
        '-i',
        '--host',
        type=str,
        default="0.0.0.0",
        dest='host_flag',
        help='Default ip address the server binds to.(default: 127.0.0.1)',
    )
    server_parser.add_argument(
        '-r',
        '--reloader',
        action='store_true',
        default=False,
        dest='reloader_flag',
        help='Turns reloader on.(default: False)',
    )
    server_parser.add_argument(
        '-d',
        '--debug',
        action='store_true',
        default=False,
        dest='debug_flag',
        help='Turns on debug mode.(default: False)',
    )
    # setting function to execute once 'server' subcommand is called
    server_parser.set_defaults(func=__server_cli_entrypoint__)
