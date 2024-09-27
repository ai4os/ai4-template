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
PROJECT_METADATA = metadata.metadata(API_NAME)  # .json

# Fix metadata for emails from pyproject parsing
_EMAILS = PROJECT_METADATA["Author-email"].split(", ")
_EMAILS = map(lambda s: s[:-1].split(" <"), _EMAILS)
PROJECT_METADATA["Author-emails"] = dict(_EMAILS)

# Fix metadata for authors from pyproject parsing
_AUTHORS = PROJECT_METADATA.get("Author", "").replace(", ", ",").split(",")
_AUTHORS = [] if _AUTHORS == [""] else _AUTHORS
_AUTHORS += PROJECT_METADATA["Author-emails"].keys()
PROJECT_METADATA["Authors"] = sorted(_AUTHORS)

# Get ai4-metadata.yaml metadata
AI4_METADATA_DIR = os.getenv(
    "AI4_METADATA_DIR",
    default=f"{os.getcwd()}/../{API_NAME}",
)
with open(f"{AI4_METADATA_DIR}/ai4-metadata.yml", "r", encoding="utf-8") as stream:
    AI4_METADATA = yaml.safe_load(stream)

# Merge metadata from pyproject.toml and ai4-metadata.yml
API_METADATA = {**PROJECT_METADATA, **AI4_METADATA}

# logging level across API modules can be setup via API_LOG_LEVEL,
# options: DEBUG, INFO(default), WARNING, ERROR, CRITICAL
ENV_LOG_LEVEL = os.getenv("API_LOG_LEVEL", default="INFO")
LOG_LEVEL = getattr(logging, ENV_LOG_LEVEL.upper())
