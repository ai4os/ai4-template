# -*- coding: utf-8 -*-
"""
Model description
"""

import argparse
import pkg_resources
# import project's config.py
import {{ cookiecutter.repo_name }}.config as cfg
from aiohttp.web import HTTPBadRequest

## Authorization
from flaat import Flaat
flaat = Flaat()


def _catch_error(f):
    def wrap(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            raise HTTPBadRequest(reason=e)
    return wrap


def get_metadata():
    """
    Function to read metadata
    https://docs.deep-hybrid-datacloud.eu/projects/deepaas/en/wip-api_v2/user/v2-api.html#deepaas.model.v2.base.BaseModel.get_metadata
    :return:
    """

    module = __name__.split('.', 1)

    try:
        pkg = pkg_resources.get_distribution(module[0])
    except pkg_resources.RequirementParseError:
        # if called from CLI, try to get pkg from the path
        distros = list(pkg_resources.find_distributions(cfg.BASE_DIR, 
                                                        only=True))
        if len(distros) == 1:
            pkg = distros[0]
    except Exception as e:
        raise HTTPBadRequest(reason=e)

    meta = {
        'Name': None,
        'Version': None,
        'Summary': None,
        'Home-page': None,
        'Author': None,
        'Author-email': None,
        'License': None,
    }

    for line in pkg.get_metadata_lines("PKG-INFO"):
        line_low = line.lower() # to avoid inconsistency due to letter cases
        for par in meta:
            if line_low.startswith(par.lower() + ":"):
                _, value = line.split(": ", 1)
                meta[par] = value

    return meta


def warm():
    """
    https://docs.deep-hybrid-datacloud.eu/projects/deepaas/en/wip-api_v2/user/v2-api.html#deepaas.model.v2.base.BaseModel.warm
    :return:
    """
    # e.g. prepare the data


def get_predict_args():
    """
    https://docs.deep-hybrid-datacloud.eu/projects/deepaas/en/wip-api_v2/user/v2-api.html#deepaas.model.v2.base.BaseModel.get_predict_args
    :return:
    """
    return cfg.PredictArgsSchema().fields

@_catch_error
def predict(**kwargs):
    """
    Function to execute prediction
    https://docs.deep-hybrid-datacloud.eu/projects/deepaas/en/wip-api_v2/user/v2-api.html#deepaas.model.v2.base.BaseModel.predict
    :param kwargs:
    :return:
    """

    if (not any([kwargs['urls'], kwargs['files']]) or
            all([kwargs['urls'], kwargs['files']])):
        raise Exception("You must provide either 'url' or 'data' in the payload")

    if kwargs['files']:
        kwargs['files'] = [kwargs['files']]  # patch until list is available
        return _predict_data(kwargs)
    elif kwargs['urls']:
        kwargs['urls'] = [kwargs['urls']]  # patch until list is available
        return _predict_url(kwargs)

def _predict_data(*args):
    """
    (Optional) Helper function to make prediction on an uploaded file
    """
    message = 'Not implemented in the model (predict_data)'
    return message


def _predict_url(*args):
    """
    (Optional) Helper function to make prediction on a URL
    """
    message = 'Not implemented in the model (predict_url)'
    return message


def get_train_args():
    """
    https://docs.deep-hybrid-datacloud.eu/projects/deepaas/en/wip-api_v2/user/v2-api.html#deepaas.model.v2.base.BaseModel.get_train_args
    :param kwargs:
    :return:
    """
    return cfg.TrainArgsSchema().fields


###
# @flaat.login_required() line is to limit access for only authorized people
# Comment this line, if you open training for everybody
# More info: see https://github.com/indigo-dc/flaat
###
@flaat.login_required() # Allows only authorized people to train
def train(**kwargs):
    """
    Train network
    https://docs.deep-hybrid-datacloud.eu/projects/deepaas/en/wip-api_v2/user/v2-api.html#deepaas.model.v2.base.BaseModel.train
    :param kwargs:
    :return:
    """

    message = { "status": "ok",
                "sys_info": [],
                "training": [],
              }

    # use the schema
    schema = cfg.TrainArgsSchema()
    # deserialize key-word arguments
    train_args = schema.load(kwargs)
    
    # 1. implement your training here
    # 2. update "message"
    
    return message


# during development it might be practical 
# to check your code from CLI (command line interface)
def main():
    """
    Runs above-described functions depending on input parameters
    (see below an example)
    """

    if args.method == 'get_metadata':
        get_metadata()       
    elif args.method == 'predict':
        predict(**vars(args))
    elif args.method == 'train':
        train(**vars(args))
    else:
        get_metadata()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Model parameters', 
                                     add_help=False)

    cmd_parser = argparse.ArgumentParser()
    subparsers = cmd_parser.add_subparsers(
                            help='methods. Use \"deep_api.py method --help\" to get more info', 
                            dest='method')

    get_metadata_parser = subparsers.add_parser('get_metadata', 
                                         help='get_metadata method',
                                         parents=[parser])                                      
    # add arguments for get_metadata() here. Normally none is provided.

    predict_parser = subparsers.add_parser('predict', 
                                           help='commands for prediction',
                                           parents=[parser])
    # add arguments for predict() here. 
    # One supposes to convert get_predict_args() to predict_parser

    train_parser = subparsers.add_parser('train', 
                                         help='commands for training',
                                         parents=[parser])
    # add arguments for train() here. 
    # One supposes to convert get_train_args() to train_parser

    args = cmd_parser.parse_args()
    
    main()
