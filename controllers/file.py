#!/usr/bin/env python3
# coding: utf8

"""
Controller to receive and predict a file.
"""

__author__ = 'David Flury, Andreas Kaufmann, Raphael Müller'
__email__ = "info@unmix.io"


from flask_restful import Resource, reqparse
from flask import request
import werkzeug
import numpy as np
import os
import traceback

from unmix.source.configuration import Configuration
from unmix.source.prediction.fileprediction import FilePrediction
from unmix.source.logging.logger import Logger

from context import Context
from models.prediction_response import PredictionResponse


class FileController(Resource):

    name = "File"

    def post(self):
        try:
            response = PredictionResponse(FileController.name)
            parse = reqparse.RequestParser()
            parse.add_argument("file", type=werkzeug.datastructures.FileStorage, location="files")

            argument = parse.parse_args()["file"]
            name = argument.filename
            file = os.path.join(response.directory, name)
            argument.save(file)

            prediction = FilePrediction(
                Context.engine, sample_rate=Configuration.get("collection.sample_rate"))
            
            prediction.run(file)   
            prediction.save(name, response.directory, extension='mp3')

            response.result = {
                "name": name,
                "size": os.path.getsize(file),
                "vocals": os.path.join(response.host, "result/%s/vocals" % response.identifier),
                "instrumental": os.path.join(response.host, "result/%s/instrumental" % response.identifier),
                "response": os.path.join(response.host, "result/%s/response" % response.identifier)
            }
            return response.serialize(), 200
        except Exception as e:
            Logger.error("Error while processing %s request: %s" % (FileController.name, str(e)))
            traceback.print_exc()
            return str(e), 500
