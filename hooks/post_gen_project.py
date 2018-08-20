#!/usr/bin/env python
# -*- coding: utf-8 -*-
import shutil
import os
import sys

deep_oc = 'DEEP-OC-{{ cookiecutter.repo_name }}'
dest = '../' + deep_oc
src = '../{{ cookiecutter.repo_name }}/'+ deep_oc


try:
    shutil.move(src, dest)
    sys.exit(0)
except OSError as e:
    sys.stdout.write(
        'While attempting to move '+ src +' an error occurred! '
    )
    sys.stdout.write('Error! {} '.format(e))

