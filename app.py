from flask import Flask, render_template, request
import os
import numpy as np
import pandas as pd
from sleep_efficiency.pipeline.prediction import PredictionPipeline
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


app = Flask(__name__)

@app.route('/', methods=['GET'])
def homePage():
    return render_template("index.html")

@app.route('/train', methods=['GET'])
def training():
    os.system("python main.py")
    return "Training Successful"

@app.route('/predict', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        try:
            # reading the inputs given by the user
            Age = float(request.form['Age'])
            logger.info(f'Age: {Age}')

            # Gender needs to be converted to 0 or 1
            Gender = request.form['Gender']
            Gender = {'Female': 0, 'Male': 1}[Gender]
            logger.info(f'Gender: {Gender}')


            # get the bedtime and adjust for am vs pm
            Bedtime = float(request.form['Bedtime'])
            Bedtime_AMPM = request.form['Bedtime_AMPM']
            if Bedtime_AMPM == 'PM' and Bedtime < 12:
                Bedtime += 12
            elif Bedtime_AMPM == 'AM' and Bedtime == 12:
                Bedtime = 0

            logger.info(f'Bedtime: {Bedtime}')
            
            # get the wakeup time and adjust for am vs pm
            Wakeup_time = float(request.form['Wakeup_time'])
            Wakeup_time_AMPM = request.form['Wakeup_time_AMPM']
            if Wakeup_time_AMPM == 'PM' and Wakeup_time < 12:
                Wakeup_time += 12
            elif Wakeup_time_AMPM == 'AM' and Wakeup_time == 12:
                Wakeup_time = 0

            logger.info(f'Wakeup_time: {Wakeup_time}')

            Sleep_duration = float(request.form['Sleep_duration'])
            Awakenings = float(request.form['Awakenings'])

            logger.info(f'Sleep_duration: {Sleep_duration}')
            logger.info(f'Awakenings: {Awakenings}')

            # Caffeine and Alcohol consumption were converted to binary 
            # so we'll just make these a drop down box with yes or no options
            # and smoking status is already a yes/no column
            Caffeine_consumption = 1 if request.form['Caffeine_consumption'] == 'Yes' else 0
            logger.info(f'Caffeine_consumption: {Caffeine_consumption}')


            Alcohol_consumption = 1 if request.form['Alcohol_consumption'] == 'Yes' else 0
            logger.info(f'Alcohol_consumption: {Alcohol_consumption}')

            Smoking_status = 1 if request.form['Smoking_status'] == 'Yes' else 0
            logger.info(f'Smoking_status: {Smoking_status}')

            # Exercise_frequency is 0 for both people who don't workout or workout once a week
            Exercise_frequency = 1 if float(request.form['Exercise_frequency']) > 1 else 0
            logger.info(f'Exercise_frequency: {Exercise_frequency}')

            data = [
                Age, Gender, Bedtime, Wakeup_time, Sleep_duration, 
                Awakenings, Caffeine_consumption, Alcohol_consumption,
                Smoking_status, Exercise_frequency
            ]

            feature_names = [
                'Age',
                'Gender',
                'Bedtime',
                'Wakeup time',
                'Sleep duration',
                'Awakenings',
                'Caffeine consumption',
                'Alcohol consumption',
                'Smoking status',
                'Exercise frequency'
            ]

            data = pd.DataFrame([data], columns=list(feature_names))

            obj = PredictionPipeline()
            predict = obj.predict(data)[0]
            formatted_prediction = f"{predict:.2f}"

            return render_template('results.html', prediction = formatted_prediction)

        except Exception as e:
            print('The Exception message is: ', e)
            return 'something is wrong'
        
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 8080, debug=True)