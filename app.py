import streamlit as st
import pandas as pd
import joblib

model = joblib.load("KNN_heart.pkl")
scaler = joblib.load("scaler.pkl")
columns = joblib.load("columns.pkl")

st.title("Heart Disease prediction by Shyam")
st.markdown("Provide the following details")

age = st.slider("Age",18,100,40)
sex = st.selectbox("SEX",['M','F'])
chest_pain = st.selectbox("Chest pain Type ",["ATA","NAP","TA","ASY"])
resting_bp = st.number_input("Resting Blood Presure (mm Hg)",80,600,120)
cholesterol = st.number_input("Cholesterol (mg/dl)",100,600,200)
fasting_bs = st.selectbox("Fasting Blood Sugar > 180 mg/dL",[0,1])
resting_bp = st.selectbox("Resting ECG ",["Normal","ST","LVH"])
max_hr = st.slider("Max Heart Rate ",60,220,150)
exercise_angina = st.selectbox("Excercise-Induced Angina",["Y","N"])
oldpeak  = st.slider("Oldpeak (ST Depression)", 0.0,6.0,1.0)
st_Slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])

if st.button("Predict"):
    raw_input ={
        "Age" : age,
        "RestingBp" : resting_bp,
        "Cholesterol" : cholesterol,
        "FastingBs" :fasting_bs,
        "MaxHR" : max_hr,
        "Oldpeak" :oldpeak,
        "Sex" + sex :1,
        "ChestPainType_ "+ chest_pain:1,
        "RestingECG_ " + resting_bp: 1,
        "ExcerciseAngina_ "+ exercise_angina :1,
        "ST_Slope " + st_Slope :1
      }
    input_df = pd.DataFrame([raw_input])
    for col in columns:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df = input_df[columns]

    scaled_input = scaler.transform(input_df)
    prediction = model.predict(scaled_input)[0]

    if prediction == 1:
        st.error ("High Risk of Heat Disease")    
    else:
        st.success("Low Risk of Heart Disease")

