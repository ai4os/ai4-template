DEEP-OC-{{ cookiecutter.repo_name }}
============================================

Quick instructions.

1. Build the container, e.g.:

    docker build -t {{ cookiecutter.dockerhub_user }}/{{ cookiecutter.repo_name }} .

2. Run the container:

    docker run -ti -p 5000:5000 {{ cookiecutter.dockerhub_user }}/{{ cookiecutter.repo_name }}

