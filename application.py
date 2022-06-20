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

model= pickle.load( open( "ran_forest_mod.p", "rb" ) )

from sklearn import preprocesing
def main():
        st.write('''# *customer payment Predictor*''')
        add_selectbox = st.sidebar.selectbox("How would you like to predict?", ("Online", "Batch"))
        st.sidebar.info('This app is created to predict Customer payment Failure')
        
        if add_selectbox == "Online":
                #Based on our optimal features selection
                st.subheader("DataFeed")
                sales = st.number_input('The amount charged to the customer monthly', min_value=0, max_value=110000, value=0)
                MemberType = st.selectbox('Member Type:', ('Full', 'Other MemberType', 'Associate', '2nd Account'))
                ProductCategory = st.selectbox('ProductCategory:', ('Fixed & Broadband', 'Liquid', 'Agrochemicals', 'Other products','Charge card', 'General - Machinery', 'General - Supplies',
                     'Building Materials', 'Mobile', 'Non HH, mains gas, MOP','Fuel Cards'))
                Town = st.selectbox('Town:', ('Thetford', 'Holt', 'Wisbech', 'Other Area', 'Norwich', 'Dereham','Kings Lynn', 'Lowestoft', 'Huntingdon', 'Diss', 'Beccles','Fakenham', 'Spalding', 'Bury St Edmunds', 'Colchester','Gt Yarmouth', 'Bungay', 'North Walsham', 'Wymondham','Great Yarmouth', 'Cambridge', 'Peterborough', 'Ely',"King's Lynn", 'Attleborough', 'March', 'Swaffham','Downham Market'))
        
                st.subheader("Member information")
                yearofjoning = st.number_input('Member Joining Year',min_value=0, max_value=3000, value=0)
                monthofjoining = st.number_input('Member Joining Month',min_value=0, max_value=12, value=0)
                dayofjoining = st.number_input('Member Joining Day',min_value=0, max_value=31, value=0)
        
                st.subheader("other Information")
                Zerosales= st.selectbox("is the invoice amount is zero if yes press 1:",("1","0"))
                refunded=st.selectbox("is the invoice amount is in -values if yes press 1:",("1","0"))
                
               
                
                st.markdown("<h3></h3>", unsafe_allow_html=True)
                st.write('Overview of input is shown below')
                st.markdown("<h3></h3>", unsafe_allow_html=True)
                
                
                preprocess_df = preprocesing(features_df, 'Online')
                
                prediction = model.predict(preprocess_df)
                
                if st.button('Predict'):
                        if prediction == 1:
                                st.warning('Yes, the customer payment is not at rish')
                        else:
                                st.success('The customer payment is at risk.')
                                
                                
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
    
if __name__ == '__main__':
        main()
                                
                        
                        
                        
                        
        
        
        

        










        
