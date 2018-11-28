DEEP-OC-{{ cookiecutter.repo_name }}
============================================

![DEEP-Hybrid-DataCloud logo](https://deep-hybrid-datacloud.eu/wp-content/uploads/2018/01/logo.png)

This is a container that will simply run the DEEP as a Service API component,
with {{ cookiecutter.repo_name }} (src: [{{ cookiecutter.repo_name }}](https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.repo_name }})).

    
# Running the container

## Directly from Docker Hub

To run the Docker container directly from Docker Hub and start using the API
simply run the following command:

```bash
$ docker run -ti -p 5000:5000 {{ cookiecutter.dockerhub_user }}/deep-oc-{{ cookiecutter.repo_name }} deepaas-run --listen-ip=0.0.0.0
```

This command will pull the Docker container from the Docker Hub
[{{ cookiecutter.dockerhub_user }}](https://hub.docker.com/u/{{ cookiecutter.dockerhub_user }}/) organization.

## Building the container

If you want to build the container directly in your machine (because you want
to modify the `Dockerfile` for instance) follow the following instructions:

Building the container:

1. Get the `DEEP-OC-{{ cookiecutter.repo_name }}` repository (this repo):

    ```bash
    $ git clone https://github.com/{{ cookiecutter.github_user }}/DEEP-OC-{{ cookiecutter.repo_name }}
    ```

2. Build the container:

    ```bash
    $ cd DEEP-OC-{{ cookiecutter.repo_name }}
    $ docker build -t {{ cookiecutter.dockerhub_user }}/deep-oc-{{ cookiecutter.repo_name }} .
    ```

3. Run the container:

    ```bash
    $ docker run -ti -p 5000:5000 {{ cookiecutter.dockerhub_user }}/deep-oc-{{ cookiecutter.repo_name }} deepaas-run --listen-ip=0.0.0.0
    ```

These three steps will download the repository from GitHub and will build the
Docker container locally on your machine. You can inspect and modify the
`Dockerfile` in order to check what is going on. For instance, you can pass the
`--debug=True` flag to the `deepaas-run` command, in order to enable the debug
mode.

# Connect to the API

Once the container is up and running, browse to `http://localhost:5000` to get
the [OpenAPI (Swagger)](https://www.openapis.org/) documentation page.
