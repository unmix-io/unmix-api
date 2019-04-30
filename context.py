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


class Context(object):

    @staticmethod
    def initialize():
        Configuration.initialize('./resources/configuration.jsonc', disable_merge=True)
        Logger.initialize()
        Context.engine = Engine()
        Context.engine.load_weights('./resources/model.h5')

        Context.output_directory = "./results/"
        if not os.path.exists(Context.output_directory):
            os.makedirs(Context.output_directory)
