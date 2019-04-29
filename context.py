#!/usr/bin/env python3
# coding: utf8

"""
unmix.io RESTful API to extract vocals and instrumental from audio streams.
"""


__author__ = 'David Flury, Andreas Kaufmann, Raphael Müller'
__email__ = "info@unmix.io"


from unmix.source.engine import Engine
from unmix.source.configuration import Configuration
from unmix.source.logging.logger import Logger

from unmix.source.lossfunctions.lossfunctionfactory import *

class Context(object):

    @staticmethod
    def initialize():
        Configuration.initialize('./resources/configuration.jsonc')
        Logger.initialize()
        Context.engine = Engine()
        Context.engine.load_weights('./resources/models.h5')
