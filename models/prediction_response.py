#!/usr/bin/env python3
# coding: utf8

"""
Response object for prediction requests.
"""

__author__ = 'David Flury, Andreas Kaufmann, Raphael Müller'
__email__ = "info@unmix.io"


import datetime
import json
import uuid
import os

from unmix.source.configuration import Configuration

from context import Context


class PredictionResponse(object):

    def __init__(self, controller):
        self.identifier = str(uuid.uuid4())
        self.controller = controller
        self.time = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
        self.configuration = {
            "name": Configuration.get('environment.name'),
            "transformation": Configuration.get('environment.name'),
            "model": Configuration.get('training.model.name'),
            "sample_rate": Configuration.get('collection.sample_rate')
        }
        self.result = {}
        self.directory = os.path.join(
            Context.output_directory, self.identifier)
        os.makedirs(self.directory)

    def serialize(self):
        content = self.__dict__
        with open(os.path.join(self.directory, 'result.json'), 'w') as file:  
            json.dump(content, file)
        return content
