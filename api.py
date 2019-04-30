#!/usr/bin/env python3
# coding: utf8

"""
unmix.io RESTful API to extract vocals and instrumental from audio streams.
"""


__author__ = 'David Flury, Andreas Kaufmann, Raphael Müller'
__email__ = "info@unmix.io"


from flask import Flask
from flask_restful import Api, Resource, reqparse

from controllers.dummy import DummyController
from controllers.file import FileController
from controllers.youtube import YouTubeController
from controllers.result import ResultController
from context import Context


def register_controllers(api):
    api.add_resource(DummyController, '/dummy/<string:name>')
    api.add_resource(YouTubeController, '/predict/youtube') # Expect "link" GET parameter
    api.add_resource(FileController, '/predict/file') # Expect "link" GET parameter
    api.add_resource(ResultController, '/result/<string:identifier>/<string:track>')


if __name__ == "__main__":
    app = Flask(__name__)
    api = Api(app)
    register_controllers(api)
    Context.initialize()
    app.run()
