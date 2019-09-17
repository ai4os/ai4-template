#!/bin/bash
#
# Copyright (c) 2017 - 2019 Karlsruhe Institute of Technology - Steinbuch Centre for Computing
# This code is distributed under the MIT License
# Please, see the LICENSE file
#

topology_file="deep-oc-mesos-webdav.yml"

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
# GPU command versions:
# "run_command": "jupyterPORT=$PORT2 /run_jupyter.sh --allow-root",
# "run_command": "deepaas-run --listen-port=0.0.0.0 --listen-port=$PORT0",
###
# Jupyter possible config:
# "jupyter_pass": "s3cret",
# "jupyter_config_url": "deepnc:/Datasets/jupyter"
###

### MAIN CALL FOR THE DEPLOYMENT
#   DEFINE PARAMETERS OF YOUR DEPLOYMENT HERE
#
orchent depcreate $topology_file '{ "docker_image": "deephdc/deep-oc-{{ cookiecutter.repo_name }}:cpu",
                                    "mem_size": "8192 MB",
                                    "num_cpus": "1",
                                    "num_gpus": "0",
                                    "run_command": "deepaas-run --listen-ip=0.0.0.0",
                                    "flaat_disable": "no",
                                    "rclone_conf": "/srv/.rclone/rclone.conf",
                                    "rclone_url": "https://nc.deep-hybrid-datacloud.eu/remote.php/webdav/",
                                    "rclone_user": "DEEP-XYXYXYXYXYXYXYXYXYXY",
                                    "rclone_pass": "jXYXYXYXYXYXYXYXYXYXYXYX" }'

