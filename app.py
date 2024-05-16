import streamlit as st
import numpy as np
import pandas as pd
import pickle

model = pickle.load(open('model.pkl','rb'))
#add title
st.title('Stroke Prediction using Machine Learning')
st.markdown("""
           <style>
           .title {
               font-family: "Arial Black", sans-serif;
               color: blue;
               font-size: 36px;
           }
           body {
               background-image: url('https://miro.medium.com/v2/resize:fit:828/format:webp/1*0LC15kC1pmgcZZanHjchDA.png');
               background-size: cover;
           }
           </style>
           """, unsafe_allow_html=True)

def predict_stroke(age, hypertension, heart_disease, ever_married, work_type, avg_glucose_level, bmi, smoking_status):
    input_values = [[age, hypertension, heart_disease, ever_married, work_type, avg_glucose_level, bmi, smoking_status]]
    prediction = model.predict(input_values)[0] #calling saved model for prediction
    if prediction == 1:
        return 'Shows indicators for stroke risk.'
    else:
        return 'Does not show indicators for stroke risk.'

def add_emoji(label, emoji):
    return label + " " + emoji

# Input fields with emojis
age = st.number_input(add_emoji('Enter Age', '👴'), value=0)
avg_glucose_level = st.number_input(add_emoji('Enter Glucose level', '🩸'), value=0)
bmi = st.number_input(add_emoji('Enter BMI', '⚖️'), value=0)
hypertension = st.radio(add_emoji('Hypertension', '⚠️'), ['No', 'Yes'])
hypertension = 1 if hypertension == 'Yes' else 0

heart_disease = st.radio(add_emoji('Heart disease', '❤️'), ['No', 'Yes'])
heart_disease = 1 if heart_disease == 'Yes' else 0

ever_married = st.radio(add_emoji('Married', '💍'), ['No', 'Yes'])
ever_married = 1 if ever_married == 'Yes' else 0

work_type = st.selectbox(add_emoji('Work type', '💼'), ['Private', 'Self-employed', 'Govt job'])
work_type_map = {'Private': 0, 'Self-employed': 1, 'Govt job': 2}
work_type = work_type_map[work_type]



smoking_status = st.selectbox(add_emoji('Smoke status', '🚭'), ['never smoked', 'Unknown', 'formerly smoked', 'smokes'])
smoke_map = {'never smoked': 0, 'Unknown': 1, 'formerly smoked': 2, 'smokes': -1}
smoking_status = smoke_map[smoking_status]

if st.button('Predict'):
    result = predict_stroke(age, hypertension, heart_disease, ever_married, work_type, avg_glucose_level, bmi, smoking_status)
    st.success(result)
