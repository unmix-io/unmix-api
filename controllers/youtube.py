#!/usr/bin/env python3
# coding: utf8

"""
Controller to download and predict audio from YouTube.
"""

__author__ = 'David Flury, Andreas Kaufmann, Raphael Müller'
__email__ = "info@unmix.io"


from flask_restful import Resource
from flask import request
import os
import pytube
import youtube_dl
import traceback

from unmix.source.configuration import Configuration
from unmix.source.prediction.youtubeprediction import YoutTubePrediction
from unmix.source.logging.logger import Logger

from context import Context
from models.prediction_response import PredictionResponse


class YouTubeController(Resource):

    name = "YoutTube"

    thumbnail_pattern = "https://img.youtube.com/vi/%s/hqdefault.jpg"

    def post(self):
        try:
            response = PredictionResponse(YouTubeController.name)

            link = request.args.get('link')

            prediction = YoutTubePrediction(
                Context.engine, sample_rate=Configuration.get("collection.sample_rate"))
            path, name, size = prediction.run(link, response.directory)
            prediction.save(name, path, extension='mp3')

            valid, id, title, thumbnail = self.__metadata(link)
            if not valid:
                id, title, thumbnail = self.__metadata_alternative(link)

            response.result = {
                "name": title if title else name,
                "thumbnail": thumbnail,
                "video_id": id,
                "size": size,
                "vocals": os.path.join(response.host, "result/%s/vocals" % response.identifier),
                "instrumental": os.path.join(response.host, "result/%s/instrumental" % response.identifier),
                "response": os.path.join(response.host, "result/%s/response" % response.identifier)
            }
            return response.serialize(), 200
        except Exception as e:
            Logger.error("Error while processing %s request: %s" %
                         (YouTubeController.name, str(e)))
            traceback.print_exc()
            return str(e), 500

    def __metadata(self, link):
        try:
            ydl_opts = {
                'format': 'bestaudio',
                'restrictfilenames': True,
                'forcefilename': True
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(link, download=False)
                return True, info["id"], info["title"], info["thumbnail"]
        except:
            return False, "", "", ""

    def __metadata_alternative(self, link):
        """
        Alternative library to download YouTube files.
        """
        try:
            id = pytube.extract.video_id(link)
            yt = pytube.YouTube(link)
            return True, id, yt.title, YouTubeController.thumbnail_pattern % id
        except:
            return False, "", "", ""
