# -*- coding: utf-8 -*-
"""
Functions to integrate your model with the DEEPaaS API.
It's usually good practice to keep this file minimal, only performing the interfacing tasks.
In this way you don't mix your true code with DEEPaaS code and everything is more modular.
That is, if you need to write the predict() function in api.py, you would import your true predict
function and call it from here (with some processing/postprocessing in between if needed).
For example:

    import utils

    def predict(**kwargs):
        args = preprocess(kwargs)
        resp = utils.predict(args)
        resp = postprocess(resp)
        return resp

To start populating this file, take a look at the docs [1] and at a canonical exemplar module [2].

[1]: https://docs.deep-hybrid-datacloud.eu/
[2]: https://github.com/deephdc/demo_app
"""

from functools import wraps

from aiohttp.web import HTTPBadRequest


def _catch_error(f):
    """
    Decorate function to return an error as HTTPBadRequest,
    in case it fails.
    """
    @wraps(f)
    def wrap(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            raise HTTPBadRequest(reason=e)
    return wrap


# def get_metadata():
#     return {}
#
#
# def warm():
#     pass
#
#
# def get_predict_args():
#     return {}
#
#
# @_catch_error
# def predict(**kwargs):
#     return None
#
#
# def get_train_args():
#     return {}
#
#
# def train(**kwargs):
#     return None


################################################################
# Some functions that are not mandatory but that can be useful #
# (you can remove this if you don't need them)                 #
################################################################

# import pkg_resources
# import os


# BASE_DIR = os.path.dirname(os.path.normpath(os.path.dirname(__file__)))


# def _fields_to_dict(fields_in):
#     """
#     Function to convert mashmallow fields to dict()
#     """
#     dict_out = {}
#
#     for key, val in fields_in.items():
#         param = {}
#         param['default'] = val.missing
#         param['type'] = type(val.missing)
#         if key == 'files' or key == 'urls':
#             param['type'] = str
#
#         val_help = val.metadata['description']
#         if 'enum' in val.metadata.keys():
#             val_help = "{}. Choices: {}".format(val_help,
#                                                 val.metadata['enum'])
#         param['help'] = val_help
#
#         try:
#             val_req = val.required
#         except:
#             val_req = False
#         param['required'] = val_req
#
#         dict_out[key] = param
#     return dict_out
#
#
# def get_metadata():
#     """
#     Predefined get_metadata() that renders your module package configuration.
#     """
#
#     module = __name__.split('.', 1)
#
#     try:
#         pkg = pkg_resources.get_distribution(module[0])
#     except pkg_resources.RequirementParseError:
#         # if called from CLI, try to get pkg from the path
#         distros = list(pkg_resources.find_distributions(BASE_DIR,
#                                                         only=True))
#         if len(distros) == 1:
#             pkg = distros[0]
#     except Exception as e:
#         raise HTTPBadRequest(reason=e)
#
#     ### One can include arguments for train() in the metadata
#     train_args = _fields_to_dict(get_train_args())
#     # make 'type' JSON serializable
#     for key, val in train_args.items():
#         train_args[key]['type'] = str(val['type'])
#
#     ### One can include arguments for predict() in the metadata
#     predict_args = _fields_to_dict(get_predict_args())
#     # make 'type' JSON serializable
#     for key, val in predict_args.items():
#         predict_args[key]['type'] = str(val['type'])
#
#     meta = {
#         'name': None,
#         'version': None,
#         'summary': None,
#         'home-page': None,
#         'author': None,
#         'author-email': None,
#         'license': None,
#         'help-train': train_args,
#         'help-predict': predict_args
#     }
#
#     for line in pkg.get_metadata_lines("PKG-INFO"):
#         line_low = line.lower()  # to avoid inconsistency due to letter cases
#         for par in meta:
#             if line_low.startswith(par.lower() + ":"):
#                 _, value = line.split(": ", 1)
#                 meta[par] = value
#
#     return meta
