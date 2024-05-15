import streamlit as sts
import numpy as np
import pandas as pd
import pickle

model = pickle.load(open('model.pkl','rb'))
#add title
sts.title('Stroke Prediction using Machine Learning')


def predict_stroke(age, hypertension, heart_disease, ever_married, work_type, avg_glucose_level, bmi, smoking_status):
    input_values = [[age, hypertension, heart_disease, ever_married, work_type, avg_glucose_level, bmi, smoking_status]]
    prediction = model.predict(input_values)[0] #calling saved model for prediction
    if prediction == 1:
        return 'Shows indicators for stroke risk.'
    else:
        return 'Does not show indicators for stroke risk.'

age = sts.number_input('Enter Age', value=0)
hypertension = sts.radio('Hypertension', ['No', 'Yes'])
hypertension = 1 if hypertension == 'Yes' else 0

heart_disease = sts.radio('Heart disease', ['No', 'Yes'])
heart_disease = 1 if heart_disease == 'Yes' else 0

ever_married = sts.radio('Married', ['No', 'Yes'])
ever_married = 1 if ever_married == 'Yes' else 0

work_type = sts.selectbox('Work type', ['Private', 'Self-employed', 'Govt job', 'Children', 'Never worked'])
work_type_map = {'Private': 0, 'Self-employed': 1, 'Govt job': 2, 'Children': -1, 'Never worked': -2}
work_type = work_type_map[work_type]

avg_glucose_level = sts.number_input('Enter Glucose level', value=0)
bmi = sts.number_input('Enter BMI', value=0)

smoking_status = sts.selectbox('Smoke status', ['never smoked', 'Unknown', 'formerly smoked', 'smokes'])
smoke_map = {'never smoked': 0, 'Unknown': 1, 'formerly smoked': 2, 'smokes': -1}
smoking_status = smoke_map[smoking_status]

if sts.button('Predict'):
    result = predict_stroke(age, hypertension, heart_disease, ever_married, work_type, avg_glucose_level, bmi, smoking_status)
    sts.write(result)
