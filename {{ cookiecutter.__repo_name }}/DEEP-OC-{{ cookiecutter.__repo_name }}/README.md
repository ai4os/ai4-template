<div align="center">
<img src="https://marketplace.deep-hybrid-datacloud.eu/images/logo-deep.png" alt="logo" width="300"/>
</div>

# DEEP-OC-{{ cookiecutter.__repo_name }}
[![Build Status](https://jenkins.indigo-datacloud.eu/buildStatus/icon?job=Pipeline-as-code/DEEP-OC-org/{{ cookiecutter.__deephdc_docker }}/master)](https://jenkins.indigo-datacloud.eu/job/Pipeline-as-code/job/DEEP-OC-org/job/{{ cookiecutter.__deephdc_docker }}/job/master)

This is a container that will run the [{{ cookiecutter.__repo_name }}]({{ cookiecutter.git_base_url }}/{{ cookiecutter.__repo_name }}) application leveraging the DEEP as a Service API component ([DEEPaaS API V2](https://github.com/indigo-dc/DEEPaaS)).

    
## Running the container

### Directly from Docker Hub

To run the Docker container directly from Docker Hub and start using the API simply run the following command:

```bash
$ docker run -ti -p 5000:5000 -p 6006:6006 -p 8888:8888 deephdc/{{ cookiecutter.__deephdc_docker.lower() }}
```

This command will pull the Docker container from the Docker Hub [deephdc](https://hub.docker.com/u/deephdc/) repository and start the default command (`deepaas-run --listen-ip=0.0.0.0`).

**N.B.** For either CPU-based or GPU-based images you can also use [udocker](https://github.com/indigo-dc/udocker).

### Building the container

If you want to build the container directly in your machine (because you want to modify the `Dockerfile` for instance) follow the following instructions:
```bash
git clone {{ cookiecutter.git_base_url }}/DEEP-OC-{{ cookiecutter.__repo_name }}
cd DEEP-OC-{{ cookiecutter.__repo_name }}
docker build -t deephdc/{{ cookiecutter.__deephdc_docker.lower() }} .
docker run -ti -p 5000:5000 -p 6006:6006 -p 8888:8888 deephdc/{{ cookiecutter.__deephdc_docker.lower() }}
```

These three steps will download the repository from GitHub and will build the Docker container locally on your machine. You can inspect and modify the `Dockerfile` in order to check what is going on. For instance, you can pass the `--debug=True` flag to the `deepaas-run` command, in order to enable the debug mode.


## Connect to the API

Once the container is up and running, browse to http://0.0.0.0:5000/ui to get the [OpenAPI (Swagger)](https://www.openapis.org/) documentation page.


## Project structure
```
├─ Dockerfile             <- Describes main steps on integration of DEEPaaS API and
│                            <your_project> application in one Docker image
│
├─ Jenkinsfile            <- Describes basic Jenkins CI/CD pipeline
│
├─ LICENSE                <- License file
│
├─ README.md              <- README for developers and users.
│
└── metadata.json         <- Defines information propagated to the DEEP Marketplace
```

You can validate the `metadata.json` before making a git push using:
```shell
pip install git+https://github.com/deephdc/schema4apps
deep-app-schema-validator metadata.json
```
