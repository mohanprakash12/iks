from pycaret.classification import load_model, predict_model
import streamlit as st
import pandas as pd
import numpy as np
model = pickle.load( open( "modelsly", "rb" ) )

def predict(model, input_df):
	predictions_df = predict_model(estimator=model, data=input_df)
	predictions = predictions_df['Label'][0]
	return predictions


def main():
	add_selectbox = st.sidebar.selectbox(
	"How would you like to predict?",
	("Online", "Batch"))
	st.sidebar.info('This app is created to predict Customer payment failure')
	st.title("Predicting Customer payment Failure")
	if add_selectbox == 'Online':
		sales = st.number_input('The amount charged to the customer monthly', min_value=0, max_value=110000, value=0)
		MemberType = st.selectbox('Member Type:', ('Full', 'Other MemberType', 'Associate', '2nd Account'))
		ProductCategory = st.selectbox('ProductCategory:', ('Fixed & Broadband', 'Liquid', 'Agrochemicals', 'Other products','Charge card', 'General - Machinery', 'General - Supplies',
                     'Building Materials', 'Mobile', 'Non HH, mains gas, MOP','Fuel Cards'))

		Town = st.selectbox('Town:', ('Thetford', 'Holt', 'Wisbech', 'Other Area', 'Norwich', 'Dereham','Kings Lynn', 'Lowestoft', 'Huntingdon', 'Diss', 
					      'Beccles','Fakenham', 'Spalding', 'Bury St Edmunds', 'Colchester','Gt Yarmouth', 'Bungay', 'North Walsham', 'Wymondham',
					      'Great Yarmouth', 'Cambridge', 'Peterborough', 
					      'Ely',"King's Lynn", 'Attleborough', 'March', 'Swaffham','Downham Market'))
		yearofjoning = st.number_input('Member Joining Year',min_value=0, max_value=3000, value=0)
		monthofjoining = st.number_input('Member Joining Month',min_value=0, max_value=12, value=0)
		dayofjoining = st.number_input('Member Joining Day',min_value=0, max_value=31, value=0)
		Zerosales=st.slider('is the invoice amount is zero if yes 1' , min_value=0, max_value=1, value=1)
		refunded=st.slider('is the invoice amount is in -values if yes press 1' , min_value=0, max_value=1, value=1)
		
		output=""
		input_dict={'sales':sales,'MemberType':MemberType,'ProductCategory':ProductCategory,'Town':Town,'yearofjoning':yearofjoning
		,'monthofjoining':monthofjoining,'dayofjoining':dayofjoining,'Zerosales':Zerosales
		,'refunded':refunded}
		input_df = pd.DataFrame([input_dict])
		if st.button("Predict"):
			output = predict(model=model, input_df=input_df)
			output = str(output)
		st.success('Churn : {}'.format(output))
	if add_selectbox == 'Batch':
		file_upload = st.file_uploader("Upload csv file for predictions", type=["csv"])
		if file_upload is not None:
			data = pd.read_csv(file_upload)
			predictions = predict_model(estimator=model,data=data)
			st.write(predictions)
if __name__ == '__main__':
	main()
