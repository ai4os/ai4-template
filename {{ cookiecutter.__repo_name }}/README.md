# {{cookiecutter.project_name}}
[![Build Status](https://jenkins.indigo-datacloud.eu/buildStatus/icon?job=Pipeline-as-code/DEEP-OC-org/{{ cookiecutter.__deephdc_code }}/master)](https://jenkins.indigo-datacloud.eu/job/Pipeline-as-code/job/DEEP-OC-org/job/{{ cookiecutter.__deephdc_code }}/job/master)

{{cookiecutter.description}}

To launch it, first install the package then run [deepaas](https://github.com/ai4os/DEEPaaS):
```bash
git clone {{ cookiecutter.git_base_url }}/{{ cookiecutter.__repo_name }}
cd {{ cookiecutter.__repo_name }}
pip install -e .
deepaas-run --listen-ip 0.0.0.0
```

## Project structure
```
├── LICENSE                <- License file
│
├── README.md              <- The top-level README for developers using this project.
│
├── requirements.txt       <- The requirements file for reproducing the analysis environment, e.g.
│                             generated with `pip freeze > requirements.txt`
│
├── setup.py, setup.cfg    <- makes project pip installable (pip install -e .) so
│                             {{cookiecutter.__repo_name}} can be imported
│
├── {{cookiecutter.__repo_name}}    <- Source code for use in this project.
│   │
│   ├── __init__.py        <- Makes {{cookiecutter.__repo_name}} a Python module
│   │
│   └── api.py             <- Main script for the integration with DEEP API
│
└── Jenkinsfile            <- Describes basic Jenkins CI/CD pipeline
```
