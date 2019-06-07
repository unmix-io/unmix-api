#!/usr/bin/env python3
# coding: utf8

"""
unmix.io RESTful API to extract vocals and instrumental from audio streams.
"""


__author__ = 'David Flury, Andreas Kaufmann, Raphael Müller'
__email__ = "info@unmix.io"


from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
import os

from controllers.dummy import DummyController
from controllers.file import FileController
from controllers.youtube import YouTubeController
from controllers.result import ResultController
from context import Context


def register_controllers(api):
    api.add_resource(DummyController, '/dummy/<string:name>')
    api.add_resource(YouTubeController, '/predict/youtube')
    api.add_resource(FileController, '/predict/file')
    api.add_resource(ResultController, '/result/<string:identifier>/<string:type>')

def app():
    app = Flask(__name__)
    api = Api(app)
    register_controllers(api)
    CORS(app, resources={"*": {"origins": "*"}})
    Context.initialize()
    ssl_context = None
    if os.environ['UNMIX_API_TLS_CERTIFICATE']:
        ssl_context = (os.environ['UNMIX_API_TLS_CERTIFICATE'], os.environ['UNMIX_API_TLS_PRIVATEKEY'])
    app.run('0.0.0.0', port=os.environ['UNMIX_API_PORT'], ssl_context=ssl_context)


if __name__ == "__main__":
    app()