import os

import pickle # pre trained model loading
import streamlit as st      # web app
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Prediction of Disease Outbreaks',
                   layout='wide',
                   page_icon='doctor')

diabetes_model=pickle.load(open(r"C:\Users\Shruti\Documents\predictions\training_models\diabetes_model.sav",'rb'))

parkinsons_model=pickle.load(open(r"C:\Users\Shruti\Documents\predictions\training_models\pa_model.sav",'rb'))

heart_model =pickle.load(open(r"C:\Users\Shruti\Documents\predictions\training_models\heart_model.sav",'rb'))

with st.sidebar:
    selected=option_menu("Prediction of disease outbreak system",["Diabetes Prediction", "Heart Disease Prediction", "Parkinsons prediction"],
                         menu_icon='hospital-fill',icons=['activity','heart','person'],default_index=0)
    
if selected == "Diabetes Prediction":
    st.title('Diabetes Prediction using Ml')
    col1,col2,col3 = st.columns(3)
    with col1:
        Pregnancies= st.text_input('Number of pregnancies')
    with col2:
        Glucose= st.text_input('Glucose level')
    with col3:
        Bloodpressure= st.text_input('Blood Pressure value')
    with col1:
        skinthickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin= st.text_input('Insulin level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreefunction= st.text_input('Diabetes Pedigree function value')
    with col2:
        Age= st.text_input('Age of the person')

diab_diagnosis = ''
if st.button("diabetes Test Result"):
    user_input=[Pregnancies, Glucose, Bloodpressure, skinthickness, Insulin,
                 BMI, DiabetesPedigreefunction, Age]
    user_input= [float(x) for x in user_input]
    diab_prediction= diabetes_model.predict([user_input])
    if diab_prediction[0]==1:
        diab_diagnosis= "The person is diabetic"
    else:
        diab_diagnosis= "The person is not diabetic"
st.success(diab_diagnosis)

if selected == "Parkinsons prediction":
    st.title('Parkinsons Prediction using Ml')
    col1,col2,col3 = st.columns(3)
    with col1:
        Fo= st.text_input('Fo')
    with col2:
        Fhi= st.text_input('Fhi')
    with col3:
        Flo= st.text_input('Flo')
    with col1:
        Jitter= st.text_input('Jitter')
    with col2:
        Shimmer= st.text_input('Shimmer')
    with col3:
        HNR= st.text_input('HNR')
    with col1:
        D2= st.text_input('D2')
    with col2:
        RPDE= st.text_input('RPDE')
    with col3:
        DFA= st.text_input('DFA')
    with col1:
        spread1= st.text_input('spread1')
    with col2:
        spread2= st.text_input('spread2')

    

park_diagnosis = ''
if st.button("parkinsons Test Result"):
    user_input= [ Fo, Fhi, Flo, Jitter , Shimmer, HNR, D2,
       RPDE, DFA, spread1, spread2]
    user_input= [float(x) for x in user_input]
    park_prediction= parkinsons_model.predict([user_input])
    if park_prediction[0]==1:
        park_diagnosis= "The person is parkinsons patient"
    else:
        park_diagnosis= "The person is not a parkinsons patient"
st.success(park_diagnosis)

if selected == "Heart Disease Prediction":
    st.title('Heart Disease Prediction using Ml')
    col1,col2,col3 = st.columns(3)
    with col1:
        age= st.text_input('age')
    with col2:
        sex= st.text_input('sex')
    with col3:
        cp= st.text_input('cp')
    with col1:
        trestbps = st.text_input('trestbps')
    with col2:
        chol= st.text_input('chol')
    with col3:
        fbs = st.text_input('fbs')
    with col1:
        restecg= st.text_input('restecg')
    with col2:
        thalach= st.text_input('thalach')
    with col3:
        exang= st.text_input('exang')
    with col1:
        oldpeak= st.text_input('oldpeak')
    with col2:
        slope= st.text_input('slope')
    with col3:
        ca= st.text_input('ca')
    with col1:
        thal= st.text_input('thal')
    

heart_diagnosis = ''
if st.button("heart disease Test Result"):
    user_input=[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
    user_input= [float(x) for x in user_input]
    heart_prediction= heart_model.predict([user_input])
    if heart_prediction[0]==1:
        heart_diagnosis= "The person is heart diseasesd"
    else:
        heart_diagnosis= "The person is not heart diseased"
st.success(heart_diagnosis)


    