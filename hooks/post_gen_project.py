#!/usr/bin/env python
# -*- coding: utf-8 -*-
import shutil
import os
import sys

dest = '../DEEPP-OC-{{ cookiecutter.repo_name }}'
src = '../{{ cookiecutter.repo_name }}/'+ dest


try:
    shutil.move(src, dest)
    sys.exit(0)
except OSError as e:
    sys.stdout.write(
        'While attempting to move'+dest+'an error occurred'
    )
    sys.stdout.write('Error! {}'.format(e))

