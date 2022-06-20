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
                
                input_df = pd.DataFrame([input_dict])
                if st.button('Predict'):
                        output = predict(model=model, input_df=input_df)
                        output = str(output)
                st.success('churn :'.format(output))
  
                                
        else add_selectbox == 'Batch':
		file_upload = st.file_uploader("Upload csv file for predictions", type=["csv"])
		if file_upload is not None:
			data = pd.read_csv(file_upload)
			predictions = predict_model(estimator=model,data=data)
			st.write(predictions)
if __name__ == '__main__':
	main()
                                
                        
                        
                        
                        
        
        
        

        










        
