#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2018 - 2024 Karlsruhe Institute of Technology - Scientific Computing Center
# This code is distributed under the MIT License
# Please, see the LICENSE file

""" 
    Post-hook script
    Initialized Git repositories
    Creates 'test' branch
    Switches back to 'main'
"""
import logging
import os
import re
import shutil
import subprocess as subp
import sys

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

repo_name = '{{ cookiecutter.__repo_name }}'
default_branch = 'main'
readme_file = 'README.md'

def git_ini(repo):
    """ Function to initialize Git repository
    """
    gitrepo = ('{{ cookiecutter.git_base_url }}'.rstrip('/')
                + "/" +  repo + '.git')

    subp.call(["git", "init", "-b", default_branch])
    subp.call(["git", "add", "."])
    subp.call(["git", "commit", "-m", "initial commit"])
    subp.call(["git", "remote", "add", "origin", gitrepo])

    return gitrepo


def create_branch(branch):
    """ Function to create an additional branch"""

    # switch to 'main'
    subp.call(["git", "checkout", default_branch])

    # create new branch
    subp.call(["git", "checkout", "-b", branch])
    # adjust [Build Status] for the branch
    readme_content=[]
    with open(readme_file) as f_old:
        for line in f_old:
            if "[![Build Status]" in line:
                line = re.sub("/main*", "/"+branch, line)
            readme_content.append(line)

    with open(readme_file, "w") as f_new:
        for line in readme_content:
            f_new.write(line)

    subp.call(["git", "commit", "-a", "-m", "update README.md for the BuildStatus"])

    # switch back to main
    subp.call(["git", "checkout", default_branch])


try:
    # initialize git repository
    os.chdir("../" + repo_name)
    git_user_app = git_ini(repo_name)
    create_branch("test")
    create_branch("dev")

    message = f"""
*******************************************
{repo_name} was created successfully.
Don't forget to create corresponding remote repository: {git_user_app}
then you can do 'git push origin --all'
*******************************************
"""
    print(message)
    logging.info(message)
except Exception as err:
    logging.error(f"While attempting to create git repository an error occurred! {err}", exc_info=True)
    raise SystemExit(1) from err

