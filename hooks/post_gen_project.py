#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017 - 2019 Karlsruhe Institute of Technology - Steinbuch Centre for Computing
# This code is distributed under the MIT License
# Please, see the LICENSE file

""" 
    Post-hook script
    Moves DEEP-OC-{{ cookiecutter.repo_name }} directory one level up.
    Initialized Git repositories
    Creates 'test' branch
    Switches back to 'master'
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
    githubrepo = ("https://github.com/" + '{{ cookiecutter.github_user }}'
                  + "/" +  repo + '.git')
    try:
        os.chdir("../" + repo)
        subp.call(["git", "init"])
        subp.call(["git", "add", "."])
        subp.call(["git", "commit", "-m", "initial commit"])
        subp.call(["git", "remote", "add", "origin", githubrepo])

        # create test branch automatically
        subp.call(["git", "checkout", "-b", "test"])
        # adjust [Build Status] for the test branch
        readme_content=[]
        with open("README.md") as f_old:
            for line in f_old:
                if "[![Build Status]" in line:
                    line = line.replace("/master)", "/test)")
                readme_content.append(line)
                
        with open("README.md", "w") as f_new:
            for line in readme_content:
                f_new.write(line)

        # switch back to master
        subp.call(["git", "checkout", "master"])
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
