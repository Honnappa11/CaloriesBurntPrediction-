# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 18:04:42 2025

@author: HONNAPPA M S
"""

import pickle
import numpy as np
import streamlit as st

load_model=pickle.load(open('C:/Users/HONNAPPA M S/Desktop/Calories Burnt Prediction/calories_trained_data.sav','rb'))

# create function for prediction
def prediction_function(input):
    
# converting data into as nparray
    input_data_asarray=np.asarray(input,dtype=np.float32)
# array as reshaped
    input_data_reshaped=input_data_asarray.reshape(1,-1)
    predict=load_model.predict(input_data_reshaped)
    return predict


def main():
    
    # creating title
    st.title('Calories Burnt Prediction Using ML')
    
  #
    #getting the input from user
    
    col1,col2,col3=st.columns(3)
    with col1:
        Gender=st.text_input('If you are Male Please Enter "0" OtherWise "1"')
    with col2:
        
        Age=st.text_input('Enter you are Age')
    with col3:
         
         Height=st.text_input('Enter you are Hight')
    with col1:
        Weight=st.text_input('Enter you are Weight')
    with col2:
        Duration=st.text_input('Enter the Duration Value')
    with col3:
        Heart_Rate=st.text_input('Enter the Heart_Rate Value')
    with col1:
        Body_Temp=st.text_input('Enter the Body_Temp Value')
 
    
    # code for prediction
    diagnosis=''
    
    # create the button for prediction
    if st.button('Calories Burnt Test Result'):
        diagnosis=prediction_function([Gender,Age,Height,Weight,Duration,Heart_Rate,Body_Temp])
    st.success(diagnosis)
    
if __name__=='__main__':
    main()
        