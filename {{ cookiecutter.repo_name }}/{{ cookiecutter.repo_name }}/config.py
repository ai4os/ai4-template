# -*- coding: utf-8 -*-
"""
   Module to define CONSTANTS used across the project
"""

import os
from webargs import fields
from marshmallow import Schema, INCLUDE

# identify basedir for the package
BASE_DIR = os.path.dirname(os.path.normpath(os.path.dirname(__file__)))

# default locations for 'data' and 'models' are either set 
# as relative to the application path
# or via environment settings
if 'APP_LOCAL_DATA' in os.environ and len(os.environ['APP_LOCAL_DATA']) > 1:
    DATA_PATH = os.environ['APP_LOCAL_DATA']
else:
    DATA_PATH = os.path.join(BASE_DIR, 'data')

if 'APP_LOCAL_MODELS' in os.environ and len(os.environ['APP_LOCAL_MODELS']) > 1:
    MODELS_PATH = os.environ['APP_LOCAL_MODELS']
else:
    MODELS_PATH = os.path.join(BASE_DIR, 'models')

# Input parameters for predict() (deepaas>=1.0.0)
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
        description="Select a file for the prediction"
    )

    # to be able to provide an URL for prediction
    urls = fields.Url(
        required=False,
        missing=None,
        description="Provide an URL of the data for the prediction"
    )
    
    # an input parameter for prediction
    arg1 = fields.Integer(
        required=False,
        missing=1,
        description="Input argument 1 for the prediction"
    )

# Input parameters for train() (deepaas>=1.0.0)
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
