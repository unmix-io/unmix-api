#!/usr/bin/env python3
# coding: utf8

"""
unmix.io RESTful API to extract vocals and instrumental from audio streams.
"""


__author__ = 'David Flury, Andreas Kaufmann, Raphael Müller'
__email__ = "info@unmix.io"


from flask import Flask
from flask_restful import Api, Resource, reqparse


from controllers.dummy import Dummy

if __name__ == "__main__":
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(Dummy, '/dummy/<string:name>')

    app.run()