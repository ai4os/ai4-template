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
RUN python -m pip --no-cache-dir install -r /home/requirements.txt && \
    rm -rf /root/.cache/pip/* && \
    rm -rf /tmp/*

# Copy the current directory contents into the container at /home
ADD . /home
