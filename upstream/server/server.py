#!/usr/bin/env python3

from ..util.log import *
import logging
LOGGER = logging.getLogger(__name__)


class Server():
    def __init__(self,  port: int = 9090):
        """
        Server class

        Keyword arguments:  
        `port`               -- Default port the server binds to. (default: 9090)
        """
        LOGGER.debug(
            "Server : constructor called")

    def run(self):
        """
        this function runs the server
        """
        LOGGER.debug("Server -> run() : function called")
