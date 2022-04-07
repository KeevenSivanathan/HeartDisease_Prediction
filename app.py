from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
#path = '/Users/ksivanathan/Desktop/prep/Kaggle/heart_disease/'
model = pickle.load(open('decision_tree_classifier.pkl', 'rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():

    if request.method == 'POST':

        gender = request.form['Gender']
        if (gender == 'Male'):
            gender = 1
        else:
            gender = 0

        race = request.form['Race']
        if (race == 'Asian'):
            race = 1
        elif (race == 'Black'):
            race = 2
        elif (race == 'Hispanic'):
            race = 3
        elif (race == 'Native American'):
            race = 0
        elif (race == 'White'):
            race = 5
        else:
            race = 4


        age = request.form['Age']
        if (age == '18 - 24'):
            age = 0
        elif (age == '25 - 29'):
            age = 1
        elif (age == '30 - 34'):
            age = 2
        elif (age == '35 - 39'):
            age = 3
        elif (age == '40 - 44'):
            age = 4
        elif (age == '45 - 49'):
            age = 5
        elif (age == '50 - 54'):
            age = 6
        elif (age == '55 - 59'):
            age = 7
        elif (age == '60 - 64'):
            age = 8
        elif (age == '65 - 69'):
            age = 9
        elif (age == '70 - 74'):
            age = 10
        elif (age == '75 - 79'):
            age = 11
        else:
            age = 12

        bmi = request.form['BMI']
        if (bmi == 'Underweight'):
            bmi = 3
        elif (bmi == 'Normal'):
            bmi = 0
        elif (bmi == 'Overweight'):
            bmi = 2
        else:
            bmi = 1

        gen_health = request.form['GenHealth']
        if (gen_health == 'Excellent'):
            gen_health = 0
        elif (gen_health == 'Very Good'):
            gen_health = 4
        elif (gen_health == 'Good'):
            gen_health = 2
        elif (gen_health == 'Fair'):
            gen_health = 1
        else:
            gen_health = 3

        phys_activity = request.form['PhysicalActivity']
        if (phys_activity == 'Yes'):
            phys_activity = 1
        else:
            phys_activity = 0

        phys_health = int(request.form['PhysicalHealth'])
        mental_health = int(request.form['MentalHealth'])

        asthma = request.form['Asthma']
        if (asthma == 'Yes'):
            asthma = 1
        else:
            asthma = 0

        diabetic = request.form['Diabetic']
        if (diabetic == 'Yes'):
            diabetic = 2
        elif (diabetic == 'No'):
            diabetic = 0
        elif (diabetic == 'Borderline Diabetic'):
            diabetic = 1
        else:
            diabetic = 3

        stroke = request.form['Stroke']
        if (stroke == 'Yes'):
            stroke = 1
        else:
            stroke = 0

        kidney = request.form['kidneyDisease']
        if (kidney == 'Yes'):
            kidney = 1
        else:
            kidney = 0

        cancer = request.form['skinCancer']
        if (cancer == 'Yes'):
            cancer = 1
        else:
            cancer = 0

        diffWalking = request.form['DiffWalking']
        if (diffWalking == 'Yes'):
            diffWalking = 1
        else:
            diffWalking = 0

        drinking = request.form['AlcoholDrinking']
        if (drinking == 'Yes'):
            drinking = 1
        else:
            drinking = 0

        smoking = request.form['Smoking']
        if (smoking == 'Yes'):
            smoking = 1
        else:
            smoking = 0

        sleepTime = int(request.form['SleepTime'])

        prediction = model.predict([[gender, race, diabetic, bmi, gen_health, age, cancer, kidney, asthma,
        sleepTime, phys_activity, diffWalking, mental_health, phys_health, stroke, drinking, smoking]])

        if prediction == 1:
            return render_template('index.html',prediction_text = "Model indicates that you might have a heart disease.")
        else:
            return render_template('index.html',prediction_text="Model indicates that you DO NOT have a heart disease.")
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
