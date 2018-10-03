# -*- coding: utf-8 -*-
#!/usr/bin/env python

################################################################################
# License text
################################################################################

__author__ = 'Nikolay Trofimyuk'
__version__ = '1.0'


import logging
import logging.handlers
#import socket
import os
#import sys

class Logger:

    def __init__(self, logger_name):
        logging.captureWarnings(True) #!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.INFO)

        self.logPath = os.path.dirname(os.path.abspath(__file__))

        LOG_FILENAME = os.path.normpath('{}/{}.log'.format(self.logPath, logger_name))

        fh = logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=5242880, backupCount=10)
        fh.setLevel(logging.INFO)
        fh.setFormatter(logging.Formatter('[%(asctime)s][%(name)s][%(levelname)s] %(message)s'))
        self.logger.addHandler(fh)


    def debug(self, msg):
        self.log(logging.DEBUG, msg)

    def info(self, msg):
        self.log(logging.INFO, msg)

    def warning(self, msg):
        self.log(logging.WARNING, msg)

    def error(self, msg):
        self.log(logging.ERROR,msg)

    def critical(self, msg):
        self.log(logging.CRITICAL, msg)

    def log(self, level, msg):
        msg = str(msg).replace('%', '')
        self.logger.log(level, str(msg) +' %s', '')

