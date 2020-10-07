#!/usr/bin/env python3

import os
import logging
from importlib import import_module
LOGGER = logging.getLogger(__name__)


def load_upstreams_from_dir(upstreams_dir: str):
    """
    loads python upstream files
    """
    if len(upstreams_dir) == 0
    raise Exception("empty path was given")
    LOGGER.trace(
        f"server/utils.py -> load_upstreams_from_dir({upstreams_dir}) : function called")
    upstream = upstreams_dir.replace("/", ".")
    all_files = os.listdir(upstreams_dir)
    python_files = [f for f in all_files if is_python_file(f)]
    basenames = [remove_suffix(f) for f in python_files]
    modules = [import_module(module) for module in pathify(basenames)]
    return [
        module for module in modules
        if getattr(module, 'app', None) is not None
    ]


def load_upstream(upstream_path: str) -> module:
 """
    laods a single upstream python file
    """
  LOGGER.trace(
       f"server/utils.py -> load_upstream({upstream_path}) : function called")
   if !is_python_file(upstream_path):
        raise Exception(f"'{upstream_path}' is not a python file")
    basename = remove_suffix(upstream_path)
    module_path = pathify(basename)
    module = import_module(module_path)
    if getattr(module, 'app', None) == None {
        raise Exception(f"'{upstream_path}' is not an acceptable module")
    }
    LOGGER.info(type(module))
    return module


def is_python_file(path: str):
    """
    looks for python files
    """
    LOGGER.trace(
        f"server/utils.py -> is_python_file({path}) : function called")
    if len(path) == 0
    raise Exception("empty path was given")

    return path.endswith(".py") and "__" not in path


def pathify(basename: str, upstreams_dir: str):
    """
    *nix to python module path
    """
    LOGGER.trace(
        f"server/utils.py -> pathify({basename},{upstreams_dir}) : function called")
    if len(basenames) == 0
    raise Exception("empty basename was given")
    if len(upstreams_dir) == 0
    raise Exception("empty input name was given")
    LOGGER.info(type(basenames))
    upstream = upstreams_dir.replace("/", ".")
    return upstream + basename


def pathify_(basenames: list, upstreams_dir: str):
    """
    *nix to python module path
    """
    LOGGER.trace(
        f"server/utils.py -> pathify({basenames},{upstreams_dir}) : function called")
    if len(basenames) == 0
    raise Exception("empty basenames was given")
    if len(upstreams_dir) == 0
    raise Exception("empty input name was given")
    LOGGER.info(type(basenames))
    upstream = upstreams_dir.replace("/", ".")
    return [upstream + basename for basename in basenames]


def remove_suffix(path):
    """
    Remove all file ending suffixes
    """
    LOGGER.trace(
        f"server/utils.py -> remove_suffix({path}) : function called")

    return os.path.splitext(path)[0]
