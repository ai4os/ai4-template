# Base image, e.g. tensorflow/tensorflow:1.7.0
FROM {{ cookiecutter.docker_baseimage }}

LABEL maintainer='{{ cookiecutter.author_name }}'
LABEL version='{{ cookiecutter.app_version }}'
# {{ cookiecutter.description.replace('\'', '') }}


# Install ubuntu updates and python related stuff
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    apt-get install -y --no-install-recommends \
         git \
         curl \
         wget \
         {{ cookiecutter.python_interpreter }}-setuptools \
         {{ cookiecutter.python_interpreter }}-pip \
         {{ cookiecutter.python_interpreter }}-wheel && \ 
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /root/.cache/pip/* && \
    rm -rf /tmp/*


# Set LANG environment
ENV LANG C.UTF-8

# Set the working directory
WORKDIR /srv

# install rclone
RUN wget https://downloads.rclone.org/rclone-current-linux-amd64.deb && \
    dpkg -i rclone-current-linux-amd64.deb && \
    apt install -f && \
    mkdir /srv/.rclone/ && touch /srv/.rclone/rclone.conf && \
    rm rclone-current-linux-amd64.deb && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /root/.cache/pip/* && \
    rm -rf /tmp/*

# Install DEEPaaS from PyPi
# Install FLAAT (FLAsk support for handling Access Tokens)
RUN pip install --no-cache-dir \
        deepaas \
        flaat && \
    rm -rf /root/.cache/pip/* && \
    rm -rf /tmp/*

# Disable FLAAT authentication by default
ENV DISABLE_AUTHENTICATION_AND_ASSUME_AUTHENTICATED_USER yes


# Install user app:
RUN git clone https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.repo_name }} && \
    cd  {{ cookiecutter.repo_name }} && \
    pip install --no-cache-dir -e . && \
    rm -rf /root/.cache/pip/* && \
    rm -rf /tmp/* && \
    cd ..


# Open DEEPaaS port
EXPOSE 5000

# Open Monitoring port
EXPOSE 6006

CMD ["deepaas-run","--listen-ip=0.0.0.0"]
