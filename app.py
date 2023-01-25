import streamlit as st
from utils import PrepProcesor, columns 

import numpy as np
import pandas as pd
import pickle

#st.set_option('server.host', '0.0.0.0')
#st.set_option('server.port', 8080)


model = pickle.load(open('model.pkl','rb'))
st.title('GET ME THE PRICE OF THE HOUSE? :house:')

# 'CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX','PTRATIO', 'B', 'LSTAT'

CRIM = st.number_input("Input CRIM", 0,90)
ZN = st.number_input("Choose ZN",0,100)
INDUS = st.number_input("Choose INDUS",0,30)
CHAS = st.number_input("Choose CHAS",0.01,1.00)
NOX = st.number_input("Input NOX(0.3-0.9)", 0.30,0.90)
RM = st.number_input("Input RM", 3.00,9.00)
AGE = st.slider("Choose age",0,100)
DIS = st.number_input("Choose DIS",1.00,12.00)
RAD = st.number_input("Choose RAD",1.00,24.00)
TAX = st.slider("Choose TAX",180,720)
PTRATIO = st.number_input("Input PTRATIO", 12.00,22.00)
B = st.slider("Choose B",0,400)
LSTAT = st.number_input("Input LSTAT", 1.00,38.00)

def predict(): 
    row = np.array([CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX,PTRATIO, B, LSTAT]) 
    X = pd.DataFrame([row], columns = columns)
    prediction = model.predict(X)
    
    try:
        st.success('Price of house :thumbsup:'+ ' ' + str(prediction[0]))
    except Exception as e: 
        st.error('Error :thumbsdown:')

trigger = st.button('Predict', on_click=predict)
