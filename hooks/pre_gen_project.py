#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2018 - 2023 Karlsruhe Institute of Technology - Scientific Computing Center
# This code is distributed under the MIT License
# Please, see the LICENSE file

"""
    Pre-hook script
    1. Check that {{ cookiecutter.git_base_url}} is a valid URL
    2. Check that {{ cookiecutter.__app_name }}:
      a. is not too short (has to be more than one character)
      b. has characters valid for python
"""

import logging
import re
import sys
from urllib.parse import urlparse

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
FOLDER_REGEX = r"^[a-zA-Z0-9_-]+$"
MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"
EMAIL_REGEX = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
APP_VERSION_REGEX = r"^\d+\.\d+\.\d+$"

# -----------------------------------------------------------------------------
def validate_git_base_url():
    """Validate git_base_url"""
    git_base_url = urlparse(url="{{ cookiecutter.git_base_url }}")
    if not bool(git_base_url.scheme and git_base_url.netloc):
        logging.error("Invalid git_base_url %s", git_base_url)
        raise ValueError(f"Invalid git_base_url : {git_base_url}")


# -----------------------------------------------------------------------------
def validate_project_name():
    """Validate project_name"""
    project_name = "{{ cookiecutter.project_name }}"
    if len(project_name) < 2:
        logging.error("Invalid project name (%s), length < 2", project_name)
        raise ValueError("Invalid project name")
    if len(project_name.split(" ")) > 4:
        logging.error("Invalid project name (%s), words > 4", project_name)
        raise ValueError("Invalid project_name, must be 2 < project_name < 4 words")

# repo_name and app_name are derived automatically in cookiecutter.json,
# nevertheless, let's check them here

def validate_repo_name():
    """Validate repo_name"""
    repo_name = "{{ cookiecutter.__repo_name }}"
    if not re.match(FOLDER_REGEX, repo_name):
        logging.error("Invalid characters in repo name (%s)", repo_name)
        raise ValueError("Invalid repository parsing")


def validate_app_name():
    """Validate app_name"""
    app_name = "{{ cookiecutter.__app_name }}"
    if not re.match(MODULE_REGEX, app_name):
        logging.error("Invalid package name (%s)", app_name)
        raise ValueError("Invalid package name parsing")

# -----------------------------------------------------------------------------
def validate_authors():
    """Validate author_emails and author_names"""
    author_emails = "{{ cookiecutter.author_email }}".split(",")
    for email in author_emails:
        if not re.match(EMAIL_REGEX, email.strip()):
            logging.error("Invalid author_email %s", email)
            raise ValueError("Invalid author_email")
    author_names = "{{ cookiecutter.author_name }}".split(",")
    lens = n_authors, n_emails = len(author_names), len(author_emails)
    if n_emails != n_authors:
        logging.error("Authors (%s) not matching number of emails (%s)", *lens)
        raise ValueError("Authors not matching number of emails")


# -----------------------------------------------------------------------------
def validate_app_version():
    """Validate app_version"""
    app_version = "{{ cookiecutter.app_version }}"
    if not re.match(APP_VERSION_REGEX, app_version):
        logging.error("Invalid app_version %s", app_version)
        raise ValueError("Invalid app_version")

# -----------------------------------------------------------------------------
# If any of the validation, exit with error
# init error_messages
error = False
error_messages = []
try:
    validate_git_base_url()
    validate_project_name()
    validate_repo_name()
    validate_app_name()
    validate_authors()
    validate_app_version()
except ValueError as err:
    error_messages.append(err)
    error = True

if error:
    logging.error(error_messages, exc_info=True)
    raise SystemExit(1) from error_messages

### old code below
# check {{ cookiecutter.git_base_url}}
# def check_url(url):
#     """Function to check URL"""
#     try:
#         result = urlparse(url)
#         return all([result.scheme, result.netloc])
#     except:
#         return False

# git_base_url = '{{ cookiecutter.git_base_url}}'
# if (not check_url(git_base_url)):
#     message = ("'{}' is not a valid URL! ".format(git_base_url) +
#                "Please, check the 'git_base_url' input")
#     print("[ERROR]: " + message)
#     error = True
#     error_messages.append(message)

# # check {{ cookiecutter.__app_name }}
# MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'
# app_name = '{{ cookiecutter.__app_name }}'
# if (not re.match(MODULE_REGEX, app_name) or
#     len(app_name) < 2):
#     message = ("'{}' is not a valid Python module name! ".format(app_name) +
#                "Please, check the 'project_name' input")
#     print("[ERROR]: " + message)
#     error = True
#     error_messages.append(message)

# if error:
#     sys.exit("; ".join(error_messages))
