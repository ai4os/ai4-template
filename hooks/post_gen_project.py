#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import shutil
import subprocess as subp
import sys

repo_name = '{{ cookiecutter.repo_name }}'
deep_oc = 'DEEP-OC-{{ cookiecutter.repo_name }}'
deep_oc_dir = '../' + deep_oc
src = os.path.join("../", repo_name, deep_oc)

def git_ini(repo):
    githubrepo = ("http://github.com/" + '{{ cookiecutter.github_user }}'
                   + "/" +  '{{ cookiecutter.repo_name }}.git')
    try:
        subp.call(["cd", "../" + repo])
        subp.call(["git", "init"])
        subp.call(["git", "add", "."])
        subp.call(["git", "commit", "-m", "initial commit"]) 
        subp.call(["git", "remote", "add", "origin", githubrepo])
    except OSError as e:
        sys.stdout.write('Creating git repository failed for ' + repo + " !")
        sys.stdout.write('Error! {} '.format(e))

    
    
try:
    shutil.move(src, deep_oc_dir)

    git_ini(repo_name)
    git_ini(deep_oc)
    
    sys.exit(0)
except OSError as e:
    sys.stdout.write(
        'While attempting to move '+ src +' and create git \
         repository an error occurred! '
    )
    sys.stdout.write('Error! {} '.format(e))


