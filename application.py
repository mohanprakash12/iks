from pycaret.classification import load_model, predict_model
import streamlit as st
import pandas as pd
import numpy as np
import pickle
model = pickle.load( open( "rand_forest_mo.p", "rb" ) )

def predict(model, input_df):
	predictions_df = predict_model(estimator=model, data=input_df)
	predictions = predictions_df['Label'][0]
	return predictions

def main():
	from PIL import Image
	add_selectbox = st.sidebar.selectbox(
	"How would you like to predict?",
	("Online", "Batch"))
	st.sidebar.info('This app is created to predict Customer Churn')
	st.title("Predicting Customer Churn")
	if add_selectbox == 'Online':
		state =st.selectbox('letter code of the US state of customer residence :',['','AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'IA','ID',\
		'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV',\
		'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV','WY'])
		output=""
		if st.button("Predict"):
			output = predict(model=model, input_df=input_df)
			output = str(output)
		st.success('Failed : {}'.format(output))
	if add_selectbox == 'Batch':
		file_upload = st.file_uploader("Upload csv file for predictions", type=["csv"])
		if file_upload is not None:
			data = pd.read_csv(file_upload)
			predictions = predict_model(estimator=model,data=data)
			st.write(predictions)
if __name__ == '__main__':
	main()
