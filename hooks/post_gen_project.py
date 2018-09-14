#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import shutil
import subprocess
import sys

repo_name = '{{ cookiecutter.repo_name }}'
deep_oc = 'DEEP-OC-{{ cookiecutter.repo_name }}'
deep_oc_dir = '../' + deep_oc
src = os.path.join("../", repo_name, deep_oc)

def git_ini(repo):
    githubrepo = ("http://github.com/" + '{{ cookiecutter.github_user }}'
                   + "/" +  '{{ cookiecutter.repo_name }}.git')
                   
    subprocess.run(["cd", "../" + repo])
    subprocess.run(["git", "init"])
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "initial commit"])      
    subprocess.run(["git", "remote", "add", "origin", githubrepo])        

    
    
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


