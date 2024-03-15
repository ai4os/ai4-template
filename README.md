<div align="center">
  <img src="https://ai4eosc.eu/wp-content/uploads/sites/10/2022/09/horizontal-transparent.png" alt="logo" width="500"/>
</div>

# AI4OS Hub Modules Template (minimal)

## For users

This is a minimal template for developing new modules in the AI4OS Platform. It uses [Cookiecutter](https://cookiecutter.readthedocs.io) to generate the templates. This template is based on the  [Cookiecutter Data Science](http://drivendata.github.io/cookiecutter-data-science/) template.

This repository provides a minimal version of the AI4OS Hub template: Simple, minimal template, with the minimum requirements to integrate your AI model in AI4OS Hub.

There are other versions of the template:

* [advanced](https://github.com/ai4os/ai4-template-adv): this is a more advanced template. It makes more assumptions on how to structure projects and adds more files. If you want to integrate an already existing AI code, which you still want to keep in a separate repository, this template is for you.

* [child-module](https://github.com/ai4os/ai4-template-child): this template specifically tailors to users performing a retraining of an existing at AI4OS-Hub module. It only creates a Docker repo whose container is based on an existing module's Docker image.


To create a new template of your project, either

* install cookiecutter and run it with this template: 
``` bash
pip install cookiecutter
cookiecutter https://github.com/ai4os/ai4-template.git
```

* OR visit our Templates Hub service: https://templates.cloud.ai4eosc.eu/ and select the template

Once you answer all the questions, your repository `<your_project>` will be created.

This is what the folder structures look like:

```
<your_project>
##############
│
├── Dockerfile             <- Describes main steps on integration of DEEPaaS API and
│                             <your_project> application in one Docker image
│
├── Jenkinsfile            <- Describes basic Jenkins CI/CD pipeline (see .sqa/)
│
├── LICENSE                <- License file
│
├── README.md              <- The top-level README for developers using this project.
│
├── .sqa/                  <- CI/CD configuration files
│
├── {{cookiecutter.__app_name}}    <- Source code for use in this project.
│   │
│   ├── __init__.py        <- Makes {{cookiecutter.__app_name}} a Python module
│   │
│   ├── api.py             <- Main script for the integration with DEEP API
│   │
│   └── misc.py            <- Misc functions that were helpful accross projects
│
├── data/                  <- Folder to store the data
│
├── models/                <- Folder to store models
│
├── tests/                 <- Scripts to perfrom code testing
|
├── metadata.json          <- Defines information propagated to the AI4OS Hub
│
├── requirements.txt       <- The requirements file for reproducing the analysis environment, e.g.
│                             generated with `pip freeze > requirements.txt`
├── requirements-test.txt  <- The requirements file for running code tests (see tests/ directory)
│
└── setup.py, setup.cfg    <- makes project pip installable (pip install -e .) so
                              {{cookiecutter.__app_name}} can be imported

```

More extended documentation can be found [here](http://docs.ai4os.eu/en/latest/user/overview/cookiecutter-template.html). If you want to look at a minimal app using this template structure check [demo_app](https://github.com/ai4os-hub/ai4os-demo_app).

## For developers

Once you update the template, please, update this `README.md`, and **especially** `cookiecutter.json` file and `"__ai4_template"` entry with the corresponging, incremented version. The convention for the `"__ai4_template"` entry is to provide the template repository name, slash '/' closest version of the template, following [SymVer](https://semver.org/) specs, e.g.

```
"__ai4_template": "ai4-template/2.1.0"
```
OR
```
"__ai4_template": "ai4-template-adv/2.1.0"
```
OR
```
"__ai4_template": "ai4-template-child/2.1.0"
```
