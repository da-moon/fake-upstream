#!/usr/bin/env python3
import pbr.version

version_info = pbr.version.VersionInfo('upstream')
__version__ = version_info.release_string()
