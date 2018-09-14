# -*- coding: utf-8 -*-

import pkg_resources
# import project config.py
import {{ cookiecutter.repo_name }}.config as cfg

def get_metadata():
    
    module = __name__.split('.', 1)    
    
    pkg = pkg_resources.get_distribution(module[0])
    meta = {
        'Name': None,
        'Version': None,
        'Summary': None,
        'Home-page': None,
        'Author': None,
        'Author-email': None,
        'License': None,
    }

    for l in pkg.get_metadata_lines("PKG-INFO"):
        for par in meta:
            if l.startswith(par):
                k, v = l.split(": ", 1)
                meta[par] = v
                
    return meta
    
def predict_file(*args):
    """
    Function to make prediction on a local file
    """
    message = 'Not implemented in the model'
    return message
 
   
def predict_data(*args):
    """
    Function to make prediction on a uploaded file
    """
    message = 'Not implemented in the model'
    return message

    
def predict_url(*args):
    """
    Function to make prediction on a URL
    """    
    message = 'Not implemented in the model'
    return message
        

def train(*args):
    """
    Train network
    """
    message = 'Not implemented in the model'
    return message    