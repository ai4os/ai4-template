FROM _(CHANGE!)_put_base_docker_image_here_ # e.g. tensorflow/tensorflow:1.7.0

LABEL maintainer='{{ cookiecutter.author_name }}'
# {{ cookiecutter.description }}

RUN apt-get update && \ 
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
# python
    python -m ipykernel.kernelspec && \
    rm -rf /root/.cache/pip/* && \
    rm -rf /tmp/*


# Set the working directory
WORKDIR /home


# Install python packages listed in requirements.txt
COPY requirements.txt /home/requirements.txt
RUN python -m pip --no-cache-dir install -r /home/requirements.txt \
{% if cookiecutter.jupyter_use == 'yes' %}
        jupyter \
        jupyterlab \
{% endif %}
        && \
    rm -rf /root/.cache/pip/* && \
    rm -rf /tmp/*

{% if cookiecutter.jupyter_use == 'yes' %}
## Jupyter notebooks 
# Set up our notebook config.
COPY docker/jupyter/jupyter_notebook_config.py /root/.jupyter/
COPY docker/jupyter/run_jupyter.sh /
# For Jupyter terminal
ENV SHELL /bin/bash

# REMINDER: Tensorflow Docker Images already EXPOSE ports 6006 and 8888
EXPOSE 8888
##
{% endif %}

# Copy the current directory contents into the container at /home
ADD . /home
