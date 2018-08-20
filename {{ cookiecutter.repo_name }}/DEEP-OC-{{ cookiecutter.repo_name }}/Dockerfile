FROM _(CHANGE!)_put_base_docker_image_here_ # e.g. tensorflow/tensorflow:1.7.0

LABEL maintainer='{{ cookiecutter.author_name }}'
LABEL version='{{ cookiecutter.app_version }}'
# {{ cookiecutter.description }}

# Install ubuntu updates and python related stuff
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    git \
    curl \
    wget \
    python-setuptools \
    python-pip \
    python-wheel && \ 
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    python -m ipykernel.kernelspec && \
    rm -rf /root/.cache/pip/* && \
    rm -rf /tmp/*


# Set the working directory
WORKDIR /srv

# Install user app:
RUN git clone https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.repo_name }} -b {{ cookiecutter.github_branch }} && \
    cd  {{ cookiecutter.repo_name }} && \
    pip install -e . && \
    python -m pip --no-cache-dir install -r ./requirements.txt && \
    rm -rf /root/.cache/pip/* && \
    rm -rf /tmp/* && \
    cd ..

# Install DEEPaaS:
RUN git clone https://github.com/indigo-dc/deepaas && \
    cd deepaas && \
    pip install -U . && \
    cd ..


EXPOSE 5000

CMD deepaas-run