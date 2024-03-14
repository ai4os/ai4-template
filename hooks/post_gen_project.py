#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2018 - 2024 Karlsruhe Institute of Technology - Steinbuch Centre for Computing
# This code is distributed under the MIT License
# Please, see the LICENSE file

""" 
    Post-hook script
    Initialized Git repositories
    Creates 'test' branch
    Switches back to 'main'
"""
import os
import re
import shutil
import subprocess as subp
import sys

APP_REGEX = r'^[a-z][_a-z0-9]+$'

repo_name = '{{ cookiecutter.__repo_name }}'

app_name = '{{ cookiecutter.__app_name }}'
if not re.match(APP_REGEX, app_name):
    print("")
    print("[ERROR]: %s is not a valid Python package name!" % app_name)
    print("         Please, use low case and no dashes!")

    # exits with status 1 to indicate failure
    sys.exit(1)


def git_ini(repo):
    """ Function
        Initializes Git repository
    """
    gitrepo = ('{{ cookiecutter.git_base_url }}'.rstrip('/')
                + "/" +  repo + '.git')
    try:
        os.chdir("../" + repo)
        subp.call(["git", "init"])
        subp.call(["git", "add", "."])
        subp.call(["git", "commit", "-m", "initial commit"])
        subp.call(["git", "remote", "add", "origin", gitrepo])

        # create test branch automatically
        subp.call(["git", "checkout", "-b", "test"])
        # adjust [Build Status] for the test branch
        readme_content=[]
        with open("README.md") as f_old:
            for line in f_old:
                if "[![Build Status]" in line:
                    line = line.replace("/main)", "/test)")
                readme_content.append(line)

        with open("README.md", "w") as f_new:
            for line in readme_content:
                f_new.write(line)

        subp.call(["git", "commit", "-a", "-m", "update README.md for the BuildStatus"])

        # switch back to main
        subp.call(["git", "checkout", "main"])
    except OSError as os_error:
        sys.stdout.write('[Error] Creating git repository failed for ' + repo + " !")
        sys.stdout.write('[Error] {} '.format(os_error))
        return "Error"
    else:
        return gitrepo


try:
    # initialize git repository
    git_user_app = git_ini(repo_name)

    if "Error" not in git_user_app:
        print()
        print("[Info] {} was created successfully,".format(repo_name))
        print("       Don't forget to create corresponding remote repository: {}".format(git_user_app))
        print("       then you can do 'git push origin --all'")
        print()

    sys.exit(0)
except OSError as os_error:
    sys.stdout.write(
        'While attempting to create git repository an error occurred! '
    )
    sys.stdout.write('Error! {} '.format(os_error))
