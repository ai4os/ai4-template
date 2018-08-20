# -*- coding: utf-8 -*-
import shutil
import os
src = {{ cookiecutter.repo_name }}/DC-OC-{{ cookiecutter.repo_name }}
dest = DC-OC-{{ cookiecutter.repo_name }}

shutil.move(src, dest)
