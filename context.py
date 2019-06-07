#!/usr/bin/env python3
# coding: utf8

"""
unmix.io RESTful API to extract vocals and instrumental from audio streams.
"""


__author__ = 'David Flury, Andreas Kaufmann, Raphael Müller'
__email__ = "info@unmix.io"


import os

from unmix.source.engine import Engine
from unmix.source.configuration import Configuration
from unmix.source.logging.logger import Logger        
from unmix.source.helpers import envvars


class Context(object):

    @staticmethod
    def initialize():
        envvars.initialize()
        Configuration.initialize(os.environ['UNMIX_API_CONFIGURATION'], disable_merge=True)
        Logger.initialize()
        Context.engine = Engine()
        try:
            Context.engine.load(os.environ['UNMIX_API_WEIGHTS'])
        except:
            Context.engine.load_weights(os.environ['UNMIX_API_WEIGHTS'])

        Context.output_directory = "./results/"
        if not os.path.exists(Context.output_directory):
            os.makedirs(Context.output_directory)
        Context.temp_directory = "./temp/"
        if not os.path.exists(Context.temp_directory):
            os.makedirs(Context.temp_directory)
