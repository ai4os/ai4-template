#!/usr/bin/env python
# -*- coding: utf-8 -*-
import shutil
import os
import sys

src = '../{{ cookiecutter.repo_name }}/DC-OC-{{ cookiecutter.repo_name }}'
dest = '../DEEP-OC-{{ cookiecutter.repo_name }}'

try:
    shutil.move(src, dest)
    sys.exit(0)
except OSError as e:
    sys.stdout.write(
        'While attempting to move DC-OC-{{ cookiecutter.repo_name }} an error occurred'
    )
    sys.stdout.write('Error! {}'.format(e))

