# -*- coding: utf-8 -*-
"""
   Module to define CONSTANTS used across the project
"""

from os import path
from webargs import fields
from marshmallow import Schema, INCLUDE

# identify basedir for the package
BASE_DIR = path.dirname(path.normpath(path.dirname(__file__)))


# Input parameters for train() and predict() (deepaas>=1.0.0)
class TrainArgsSchema(Schema):
    class Meta:
        unknown = INCLUDE  # support 'full_paths' parameter

    # available fields are e.g. fields.Integer(), fields.Str(), fields.Boolean()
    # full list of fields: https://marshmallow.readthedocs.io/en/stable/api_reference.html
    arg1 = fields.Integer(
        required=False,
        missing=1,
        description="Input argument 1 for training"
    )


class PredictArgsSchema(Schema):
    class Meta:
        unknown = INCLUDE  # support 'full_paths' parameter

    # full list of fields: https://marshmallow.readthedocs.io/en/stable/api_reference.html
    # to be able to upload a file for prediction
    files = fields.Field(
        required=False,
        missing=None,
        type="file",
        data_key="data",
        location="form",
        description="Select the image you want to classify."
    )

    # to be able to provide an URL for prediction
    urls = fields.Url(
        required=False,
        missing=None,
        description="Select an URL of the image you want to classify."
    )
    
    # an input parameter for prediction
    arg1 = fields.Integer(
        required=False,
        missing=1,
        description="Input argument 1 for prediction"
    )
