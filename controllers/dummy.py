#!/usr/bin/env python3
# coding: utf8

"""
Dummy controller to test REST requests.
"""

__author__ = 'David Flury, Andreas Kaufmann, Raphael Müller'
__email__ = "info@unmix.io"


from flask_restful import Resource


class DummyController(Resource):

    def get(self, name):
        return "Hello %s, I am Get" % name, 200

    def post(self, name):
        return "Hello %s, I am Post" % name, 201

    def put(self, name):
        return "Hello %s, I am Put" % name, 418

    def delete(self, name):
        return "Hello %s, I am Delete" % name, 511