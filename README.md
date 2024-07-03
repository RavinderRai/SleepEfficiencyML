# SleepEfficiencyML

[Live app](http://54.226.49.20:8080)

![Project Demo](SleepEfficiencyGIF.gif)

## Overview

This project aims to predict sleep efficiency using a machine learning model and deploy a simple web application for user interaction. The data science aspects are relatively straightforward, but a lot of the focus here was on adhering to MLOps and software engineering best practices to create a robust and maintainable codebase.

## Features

### Data Collection and Preprocessing:

Data sourced from Kaggle: https://www.kaggle.com/datasets/equilibriumm/sleep-efficiency

Preprocessing was straightforward. The dataset only had a little over 400 rows so to keep things simple, some features were converted to binary features instead. A few were left as is, and only the hour of the day for bedtime and wakeup time were used (the exact day has no value since we aren't doing anything time-series related here).

### Model Training:

XGBoost regressor was used, with ridsearch for optimal hyperparameters. Since MLOps best practices were follows, pipelines for each step of the data science lifecycle were done, and MLFlow was used to track the relevant training and evaluation parts. Code for CI/CD pipelines are there as well although are not currently being used since there will likely be no further updates to this project. 

### Web Application:

Deployed a simple yet aesthetic web app using Flask and Gunicorn. Interactive user interface allowing users to input sleep-related parameters and receive predictions. Displays results with corresponding visual feedback (fun AI generated Pokémon images based on sleep efficiency ranges - of which there are 4).


### References/Acknowledgements

Project structure follows from the codebase in this video: https://www.youtube.com/watch?v=pxk1Fr33-L4

Live app deployment steps follow from this video, although some adjustments were made since Flask (and gunicorn) was used for the web app rather than Streamlit: https://www.youtube.com/watch?v=oynd7Xv2i9Y&t=487s

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

#### cmd
- mlflow ui


### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/RavinderRai/SleepEfficiencyML.mlflow \
MLFLOW_TRACKING_USERNAME=RavinderRai \
MLFLOW_TRACKING_PASSWORD=98ec3895bb5f99c79771a8d5e985b6c4917c40c7 \
python script.py

Run this to export as env variables:
(use `set` instead of `export` if in anaconda prompt)

```bash

export MLFLOW+TRACKING_URI=https://dagshub.com/RavinderRai/SleepEfficiencyML.mlflow

export MLFLOW_TRACKING_USERNAME=RavinderRai

export MLFLOW_TRACKING_PASSWORD=98ec3895bb5f99c79771a8d5e985b6c4917c40c7

```

# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 590184030535.dkr.ecr.us-east-1.amazonaws.com/sleepeff

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = sleepeff




## About MLflow 
MLflow

 - Its Production Grade
 - Trace all of your expriements
 - Logging & tagging your model