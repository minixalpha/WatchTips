#!/usr/bin/env python
#coding: utf-8

# SSL support

from web.wsgiserver import CherryPyWSGIServer
import config


def enable_ssl(enable):
    if enable == True:
        CherryPyWSGIServer.ssl_certificate = config.ssl_certificate_path
        CherryPyWSGIServer.ssl_private_key = config.ssl_private_key_path
