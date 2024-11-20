"""Module to define CONSTANTS used across the DEEPaaS Interface.

This module is used to define CONSTANTS used across the API interface.
Do not misuse this module to define variables that are not CONSTANTS.

By convention, the CONSTANTS defined in this module are in UPPER_CASE.
"""

import logging
import os
from importlib import metadata

import yaml

# Get AI model metadata from pyproject.toml
API_NAME = "{{ cookiecutter.__app_name }}"
PACKAGE_METADATA = metadata.metadata(API_NAME)  # .json

# Get ai4-metadata.yaml metadata
CWD = os.getcwd()
AI4_METADATA_DIR = os.getenv(f"{API_NAME.capitalize()}_AI4_METADATA_DIR")
if AI4_METADATA_DIR is None:
    if "ai4-metadata.yml" in os.listdir(f"{CWD}/{API_NAME}"):
        AI4_METADATA_DIR = f"{CWD}/{API_NAME}"
    elif "ai4-metadata.yml" in os.listdir(f"{CWD}/../{API_NAME}"):
        AI4_METADATA_DIR = f"{CWD}/../{API_NAME}"

# Open ai4-metadata.yml
_file = f"{AI4_METADATA_DIR}/ai4-metadata.yml"
with open(_file, "r", encoding="utf-8") as stream:
    AI4_METADATA = yaml.safe_load(stream)

# Project metadata
PROJECT_METADATA = {
  "name": PACKAGE_METADATA["Name"],
  "description": AI4_METADATA["description"],
  "license": PACKAGE_METADATA["License"],
  "author": PACKAGE_METADATA["Author-email"],
  "version":  PACKAGE_METADATA["Version"],
  "url":  PACKAGE_METADATA["Project-URL"],
}

# Fix metadata for emails from pyproject parsing
_EMAILS = PACKAGE_METADATA["Author-email"].split(", ")
_EMAILS = map(lambda s: s[:-1].split(" <"), _EMAILS)
PROJECT_METADATA["author"] = dict(_EMAILS)

# logging level across API modules can be setup via API_LOG_LEVEL,
# options: DEBUG, INFO(default), WARNING, ERROR, CRITICAL
ENV_LOG_LEVEL = os.getenv("API_LOG_LEVEL", default="INFO")
LOG_LEVEL = getattr(logging, ENV_LOG_LEVEL.upper())
