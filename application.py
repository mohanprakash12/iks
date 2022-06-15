#!/usr/bin/env python
# coding: utf-8

import numpy as np
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import base64
from sklearn.preprocessing import StandardScaler
from PIL import Image

st.write('''# *customer payment Predictor*''')


add_selectbox = st.sidebar.selectbox("How would you like to predict?", ("Online", "Batch"))
st.sidebar.info('This app is created to predict Customer payment Failure')

if add_selectbox == "Online":
        st.info("Input data below")
        #Based on our optimal features selection
        st.subheader("data")
        Sales = st.number_input('The amount charged to the customer monthly', min_value=0, max_value=11000, value=0)
        MemberType = st.selectbox('Member Type:', ('Full', 'Associate','2 nd Account', 'other MemberType'))
        

else:
        st.subheader("Dataset upload")
        uploaded_file = st.file_uploader("Choose a file")
        if uploaded_file is not None:
            data = pd.read_csv(uploaded_file)
            #Get overview of data
            st.write(data.head())
            st.markdown("<h3></h3>", unsafe_allow_html=True)
            #Preprocess inputs
            preprocess_df = preprocess(data, "Batch")
            if st.button('Predict'):
                #Get batch prediction
                prediction = model.predict(preprocess_df)
                prediction_df = pd.DataFrame(prediction, columns=["Predictions"])
                prediction_df = prediction_df.replace({1:'Yes, the customer will terminate the service.', 
                                                    0:'No, the customer is happy with Telco Services.'})

                st.markdown("<h3></h3>", unsafe_allow_html=True)
                st.subheader('Prediction')
                st.write(prediction_df)

        
