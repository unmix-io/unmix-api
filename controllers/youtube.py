#!/usr/bin/env python3
# coding: utf8

"""
Controller to download and predict audio from YouTube.
"""

__author__ = 'David Flury, Andreas Kaufmann, Raphael Müller'
__email__ = "info@unmix.io"


from flask_restful import Resource
from flask import request

from unmix.source.configuration import Configuration
from unmix.source.prediction.youtubeprediction import YoutTubePrediction

from context import Context
from models.prediction_response import PredictionResponse


class YouTubeController(Resource):

    name = "YoutTube"

    def get(self):
        try:
            link = request.args.get('link')
            response = PredictionResponse(YouTubeController.name)
            prediction = YoutTubePrediction(
                Context.engine, sample_rate=Configuration.get("collection.sample_rate"))
            path, name, size = prediction.run(link, response.directory)
            prediction.save(name, path)
            response.result = {
                "size": size,
                "vocals": "/result/%s/vocals" % response.identifier,
                "instrumental": "/result/%s/instrumental" % response.identifier
            }
            return response.__dict__, 200
        except Exception as e:
            return str(e), 500
