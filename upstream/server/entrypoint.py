#!/usr/bin/env python3
import pkg_resources
import sys
import logging
# [TODO] remove ...
import os

from functools import lru_cache
from flask import Flask, redirect, Response
from flasgger import Swagger

from .server import Server
from ..util.cli import *
from ..util.log import *
from .config import SWAGGER_CONFIG

LOGGER = logging.getLogger(__name__)


@lru_cache(maxsize=1)
def tos():
    # license = \
    # pkg_resources.resource_string(__name__, '../LICENSE')
    license = os.path.abspath('../LICENSE')
    return Response(license, mimetype='text/plain')


def create_endpoints(flask_app: Flask) -> None:
    LOGGER.info("Creating API Endpoints")
    flask_app.add_url_rule('/', 'index', lambda: redirect('apidocs'))
    flask_app.add_url_rule('/tos', 'tos', tos)


def __server_cli_entrypoint__(args):
    """
    this it the main function that uses Server class to start a new server
    """
    LOGGER.debug("__server_cli_entrypoint__() - function called")
    port = args.get('port_flag', 9090)
    try:
        port = int(port)
    except ValueError:
        LOOGER.error(
            "parsed 'port' value ('{}') cannot be converted to int.".format(port))
        sys.exit(-1)

    LOGGER.debug(
        f"__server_cli_entrypoint__() - parsed arguments : "
        f"port={port} ")
    try:
        server = Server(port)
        server.run
    except Exception as e:
        # handling exception
        LOGGER.error("cannot start server to error : {}".format(e))
        sys.exit(-1)
    flask_app = Flask(__name__)
    flask_app.config['SWAGGER'] = SWAGGER_CONFIG
    Swagger(flask_app)
    create_endpoints(flask_app)
    flask_app.run()


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
    # setting function to execute once 'server' subcommand is called
    server_parser.set_defaults(func=__server_cli_entrypoint__)
