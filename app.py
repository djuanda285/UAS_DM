import pandas as pd
import numpy as np
import pickle
import streamlit as st

pickle_in = open('model_uas.pkl', 'rb')
nb = pickle.load(pickle_in)

def welcome():
    return 'Hallo'

def prediction(age, sex, bmi, children, smoker):

    prediction = nb.predict([[age, sex, bmi, children, smoker]])
    print(prediction)
    return prediction

def main():
    st.title("Aplikasi Prediksi Besar Numerik Asuransi dengan Algoritma Regresi Linier")
    st.markdown('William Djuanda_2019230032')
    st.write('\n')
    st.markdown('Lengkapi data berikut:')
    
    st.write('\n')
    age = st.number_input("Age", 0)
    sex = st.number_input("Sex", 0)
    bmi = st.number_input("BMI", 0)
    children = st.number_input("Children", 0)
    smoker = st.number_input("Smoker", 0)
    result =""
    
    if st.button("REVEAL PREDIKSI"):
        result = prediction(age, sex, bmi, children, smoker)
    st.success('Hasil Prediksi Numerik- {}'.format(result))
    
if __name__=='__main__':
    main()