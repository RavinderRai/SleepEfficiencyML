# SleepEfficiencyML

## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the app.py

# How to run?

## STEPS:

Clone the repository

```bash
https://github.com/RavinderRai/SleepEfficiencyML
```

### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n mlproj python=3.8 -6
```

### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up your local host and port
```

## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)

##### cmd
- mlflow ui


### dagshub
[dagshub](https://dagshub.com/)

import dagshub
dagshub.init(repo_owner='RavinderRai', repo_name='SleepEfficiencyML', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)