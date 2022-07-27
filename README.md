<div align="center">
<img src="https://marketplace.deep-hybrid-datacloud.eu/images/logo-deep.png" alt="logo" width="300"/>
</div>

# DEEP Modules Template

This is the template for developing new modules in the DEEP Platform. It uses [Cookiecutter](https://cookiecutter.readthedocs.io) to generate the templates. This template is based on the CookieCutter [Datascience](http://drivendata.github.io/cookiecutter-data-science/) template.

There are two versions of this template:
* [master](https://github.com/deephdc/cookiecutter-deep/tree/master): this is what 99% of users are probably looking for. Simple, minimal template, with the minimum requirements to integrate your code in DEEP.
* [advanced](https://github.com/deephdc/cookiecutter-deep/tree/advanced): this is a more advanced template. It makes more assumptions on how to structure projects and adds more files than those strictly needed for integration. Unless you are looking for some specific feature, you are probably safer using master.

To create a new template of your project, install cookiecutter and run it with this template: 
``` bash
pip install cookiecutter
cookiecutter https://github.com/deephdc/cookiecutter-deep.git --checkout master
```

Once you answer all the questions, two directories will be created:
 - `DEEP-OC-<your_project>`: this is where the Docker container code goes
 - `<your_project>`: this is where your module's code goes

Each directory is a git repository and has two branches: `master` and `test`.
This is what the folder structures look like:

```
<your_project>
##############
├── LICENSE                <- License file
│
├── README.md              <- The top-level README for developers using this project.
│
├── requirements.txt       <- The requirements file for reproducing the analysis environment, e.g.
│                             generated with `pip freeze > requirements.txt`
│
├── setup.py, setup.cfg    <- makes project pip installable (pip install -e .) so
│                             {{cookiecutter.repo_name}} can be imported
│
├── {{cookiecutter.repo_name}}    <- Source code for use in this project.
│   │
│   ├── __init__.py        <- Makes {{cookiecutter.repo_name}} a Python module
│   │
│   └── api.py             <- Main script for the integration with DEEP API
│
└── Jenkinsfile            <- Describes basic Jenkins CI/CD pipeline


DEEP-OC-<your_project>
######################
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

More extended documentation can be found [here](http://docs.deep-hybrid-datacloud.eu/en/latest/user/overview/cookiecutter-template.html). If you want to look at a minimal app using this template structure check [demo_app](https://github.com/deephdc/DEEP-OC-demo_app) and [DEEP-OC-demo_app](https://github.com/deephdc/DEEP-OC-demo_app).
