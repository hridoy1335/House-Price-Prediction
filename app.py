import joblib
import pandas as pd
import numpy as np
import streamlit as st

model = joblib.load('model.jb')

st.title("Housing Price Prediction")
st.write("Enter The Details Below To Predict The Price Of A House")

imputs = [
    'OverallQual', 'GrLivArea', 'GarageArea', '1stFlrSF',
       'FullBath', 'YearBuilt', 'YearRemodAdd', 'MasVnrArea', 'Fireplaces',
       'BsmtFinSF1', 'LotFrontage', 'OpenPorchSF', 'WoodDeckSF', 'LotArea',
       'RoofStyle', 'Neighborhood', 'SaleCondition', 'BsmtFullBath',
       'Electrical', 'CentralAir'
]
input_data = {}
for feature in imputs:
    if feature == 'CentralAir':
        input_data[feature] = st.selectbox(feature, options=['Yes', 'No'], index=0)
    else:
        input_data[feature] = st.number_input(f'{feature}', value=0.0,step=0.1 if feature in ['OverallQual','FullBath','Fireplaces'] else 0.1)
    
if st.button("Predict"):
    input_data['CentralAir'] = 1 if input_data['CentralAir'] == 'Yes' else 0
    
    input_df = pd.DataFrame([input_data])
    
    prediction = model.predict(input_df)
    st.success(f'The predicted price of the house is: ${prediction[0]:,.2f}')
st.write("Note: The model is trained on a dataset of house prices and may not reflect the actual market value.")
st.write("Disclaimer: This is a demo application and the predictions may not be accurate.")