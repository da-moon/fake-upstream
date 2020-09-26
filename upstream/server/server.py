#!/usr/bin/env python3

from ..util.log import *
from ..util.file import get_file
import logging
from flask import Flask, redirect, Response, url_for
from .config import SWAGGER_CONFIG
from flasgger import Swagger
from functools import lru_cache
import sys
import pkg_resources
import os

from flask import request
from flasgger import LazyString, LazyJSONEncoder


LOGGER = logging.getLogger(__name__)
# use logger to print flask run messages
cli = sys.modules['flask.cli']
cli.show_server_banner = lambda *x: LOGGER.debug(x)


class Server():
    def __init__(self, host: str = "127.0.0.1", port: int = 9090):
        """
        Server class
        Keyword arguments:  
        `port`  -- Default port the server binds to. (default: 9090)
        `host`  -- Default host IP the server binds to. (default: 127.0.0.1)
        """
        LOGGER.debug(
            "Server : constructor called")
        self.__host = host
        self.__port = port
        flask_app = Flask(__name__)
        flask_app.logger = LOGGER
        flask_app.config['SWAGGER'] = SWAGGER_CONFIG
        # swagger = Swagger(flask_app)

        flask_app.json_encoder = LazyJSONEncoder

        template = dict(swaggerUiPrefix=LazyString(
            lambda: request.environ.get('HTTP_X_SCRIPT_NAME', '')))
        swagger = Swagger(flask_app, template=template)

        self.__server = flask_app

    @lru_cache(maxsize=1)
    def tos(self):
        # if request.method == 'POST':
        self.__server.logger.debug("Server -> tos() : handler called")
        content = get_file('../../LICENSE')
        return Response(content, mimetype="text/html")

    def run(self):
        """
        this function runs the server
        """
        self.__server.logger.debug("Server -> run() : function called")

        self.__server.logger.debug("Binding API Endpoints")
        # apidocs

        self.__server.add_url_rule(
            '/', view_func=lambda: redirect(url_for('tos')))
        self.__server.add_url_rule(
            '/tos', 'tos', self.tos, methods=['GET'])
        self.__server.run()
        # host=self.__host,
        # self.__server.run(port=self.__port, debug=True)
