#!/usr/bin/env python3
# coding: utf8

"""
Controller to return predicted results.
"""

__author__ = 'David Flury, Andreas Kaufmann, Raphael Müller'
__email__ = "info@unmix.io"


from flask_restful import Resource
from flask import send_file
import glob
import json
import os

from unmix.source.configuration import Configuration
from unmix.source.prediction.youtubeprediction import YoutTubePrediction

from context import Context


class ResultController(Resource):

    name = "Result"

    def get(self, identifier, type):
        try:
            directory = os.path.join(
                Context.output_directory, identifier)
            if type == "response":
                return self.__send_result(identifier, directory)
            return self.__send_track(identifier, directory, type)
        except Exception as e:
            return str(e), 500

    def __send_result(self, identifier, directory):
        with open(os.path.join(directory, 'result.json')) as file:
            data = json.load(file)
        return data, 200

    def __send_track(self, identifier, directory, track):
        file = None
        for file in glob.iglob(os.path.join(directory, '*_predicted_%s.*' % track)):
            file = file
            break
        if not file:
            return "%s file in results %s not found." % (track, identifier), 404
        return send_file(file,
                         mimetype='audio/mp3',
                         as_attachment=True,
                         conditional=True,
                         attachment_filename=os.path.basename(file))
