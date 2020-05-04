#!/bin/bash
#
# Copyright (c) 2017 - 2019 Karlsruhe Institute of Technology - Steinbuch Centre for Computing
# This code is distributed under the MIT License
# Please, see the LICENSE file
# 
# Bash script example for submitting jobs to DEEP Testbeds
# with the orchent tool (https://github.com/indigo-dc/orchent)

topology_file="deep-oc-marathon.yml"

USAGEMESSAGE="[Usage]: $0 [topology yaml file, default=$topology_file]"

if [[ $1 == "-h" ]] || [[ $1 == "--help" ]]; then
    shopt -s xpg_echo
    echo $USAGEMESSAGE
    exit 1
elif [ $# -eq 1 ]; then
    topology_file=$1
fi

# let's download tosca template automatically, if not found:
if [ ! -f $topology_file ]; then
    curl -o $topology_file \
    https://raw.githubusercontent.com/indigo-dc/tosca-templates/master/deep-oc/$topology_file
fi

### EXAMPLES FOR SOME PARAMETERS
# For CPU:
# "docker_image": "{{ cookiecutter.dockerhub_user }}/deep-oc-{{ cookiecutter.repo_name }}:latest",
# "num_gpus": "0",
# ## run_command options: ##
# "run_command": "deepaas-run --listen-port=0.0.0.0",
# "run_command": "deep-start -j"
###
# For GPU:
# "docker_image": "{{ cookiecutter.dockerhub_user }}/deep-oc-{{ cookiecutter.repo_name }}:gpu",
# "num_gpus": "1",
# ## run_command options: ##
# "run_command": "deepaas-run --listen-port=0.0.0.0 --listen-port=$PORT0",
# "run_command": "deep-start -j"
###
# For Jupyter add jupyter_password!:
# "jupyter_password": "my_s3cret",
###

### MAIN CALL FOR THE DEPLOYMENT
#   DEFINE PARAMETERS OF YOUR DEPLOYMENT HERE
#
orchent depcreate $topology_file '{ "docker_image": "{{ cookiecutter.dockerhub_user }}/deep-oc-{{ cookiecutter.repo_name }}:latest",
                                    "mem_size": "8192 MB",
                                    "num_cpus": "1",
                                    "num_gpus": "0",
                                    "run_command": "deepaas-run --listen-ip=0.0.0.0",
                                    "flaat_disable": "no",
                                    "rclone_conf": "/srv/.rclone/rclone.conf",
                                    "rclone_url": "https://nc.deep-hybrid-datacloud.eu/remote.php/webdav/",
                                    "rclone_user": "DEEP-XYXYXYXYXYXYXYXYXYXY",
                                    "rclone_password": "jXYXYXYXYXYXYXYXYXYXYXYX" }'

