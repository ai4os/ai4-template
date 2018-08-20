#!/usr/bin/env python
# -*- coding: utf-8 -*-
import shutil
import os
import sys

DEEP-OC = 'DEEPP-OC-{{ cookiecutter.repo_name }}'
dest = '../' + DEEP-OC
src = '../{{ cookiecutter.repo_name }}/'+ DEEP-OC


try:
    shutil.move(src, dest)
    sys.exit(0)
except OSError as e:
    sys.stdout.write(
        'While attempting to move '+ src +' an error occurred! '
    )
    sys.stdout.write('Error! {} '.format(e))

