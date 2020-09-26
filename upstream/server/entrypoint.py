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
    host = args.get('host_flag', "127.0.0.1")

    LOGGER.debug(
        f"__server_cli_entrypoint__() - parsed arguments : "
        f"host={host} "
        f"port={port} ")
    try:
        server = Server(host, port)
        server.run()

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
        '--host',
        type=str,
        default="127.0.0.1",
        dest='host_flag',
        help='Default ip address the server binds to.(default: 127.0.0.1)',
    )
    # setting function to execute once 'server' subcommand is called
    server_parser.set_defaults(func=__server_cli_entrypoint__)
