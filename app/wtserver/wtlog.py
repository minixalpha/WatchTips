#!/usr/bin/env python
#coding: utf-8

# Log System

from wsgilog import WsgiLog
import config


class Log(WsgiLog):
    def __init__(self, application):
        WsgiLog.__init__(
                self,
                application,
                log=config.log_enable,
                tofile=config.log_tofile,
                toprint=config.log_toprint,
                file=config.log_file
                )
