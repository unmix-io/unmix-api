#!/usr/bin/env python3
# coding: utf8

"""
Controller to return predicted results.
"""

__author__ = 'David Flury, Andreas Kaufmann, Raphael Müller'
__email__ = "info@unmix.io"


import glob
from flask_restful import Resource
from flask import send_file
import os

from unmix.source.configuration import Configuration
from unmix.source.prediction.youtubeprediction import YoutTubePrediction

from context import Context


class ResultController(Resource):

    name = "Result"

    def get(self, identifier, track):
        try:
            directory = os.path.join(
                Context.output_directory, identifier)
            file = None
            for file in glob.iglob(os.path.join(directory, "*_predicted_%s.*" % track)):
                file = file
                break
            if not file:
                return "File of %s in results %s not found." % (track, identifier), 404
            return send_file(file,
                mimetype="audio/wav",
                as_attachment=True,
                attachment_filename=os.path.basename(file))
        except Exception as e:
            return str(e), 500
