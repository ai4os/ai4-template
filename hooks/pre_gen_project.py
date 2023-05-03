#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2018 - 2023 Karlsruhe Institute of Technology - Steinbuch Centre for Computing
# This code is distributed under the MIT License
# Please, see the LICENSE file

"""
    Pre-hook script
    1. Check that {{ cookiecutter.git_base_url}} is a valid URL
    2. Check that {{ cookiecutter.__repo_name }}:
      a. is not too short (has to be more than one character)
      b. has characters valid for python
"""

import re
import sys
from urllib.parse import urlparse

# init error_messages
error = False
error_messages = []

# check {{ cookiecutter.git_base_url}}
def check_url(url):
    """Function to check URL"""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

git_base_url = '{{ cookiecutter.git_base_url}}'
if (not check_url(git_base_url)):
    message = ("'{}' is not a valid URL! ".format(git_base_url) +
               "Please, check the 'git_base_url' input")
    print("[ERROR]: " + message)
    error = True
    error_messages.append(message)

# check {{ cookiecutter.__repo_name }}
MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'
repo_name = '{{ cookiecutter.__repo_name }}'
if (not re.match(MODULE_REGEX, repo_name) or
    len(repo_name) < 2):
    message = ("'{}' is not a valid Python module name! ".format(repo_name) +
               "Please, check the 'project_name' input")
    print("[ERROR]: " + message)
    error = True
    error_messages.append(message)

if error:
    sys.exit("; ".join(error_messages))
