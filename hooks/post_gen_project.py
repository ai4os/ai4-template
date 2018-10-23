#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Post-hook script
    Moves DEEP-OC-{{ cookiecutter.repo_name }} directory one level up.
    Initialized Git repositories
"""
import os
import shutil
import subprocess as subp
import sys

repo_name = '{{ cookiecutter.repo_name }}'
deep_oc = 'DEEP-OC-{{ cookiecutter.repo_name }}'
deep_oc_dir = os.path.join("../", deep_oc)
src = os.path.join("../", repo_name, deep_oc)

def git_ini(repo):
    """ Function
        Initializes Git repository
    """
    githubrepo = ("git@github.com:" + '{{ cookiecutter.github_user }}'
                  + "/" +  repo + '.git')
    try:
        os.chdir("../" + repo)
        subp.call(["git", "init"])
        subp.call(["git", "add", "."])
        subp.call(["git", "commit", "-m", "initial commit"])
        subp.call(["git", "remote", "add", "origin", githubrepo])
    except OSError as os_error:
        sys.stdout.write('Creating git repository failed for ' + repo + " !")
        sys.stdout.write('Error! {} '.format(os_error))


try:
    # move DEEP-OC-{{ cookiecutter.repo_name }} one level up
    shutil.move(src, deep_oc_dir)

    # initialized both git repositories
    git_ini(repo_name)
    git_ini(deep_oc)

    sys.exit(0)
except OSError as os_error:
    sys.stdout.write(
        'While attempting to move '+ src +' and create git \
         repository an error occurred! '
    )
    sys.stdout.write('Error! {} '.format(os_error))
