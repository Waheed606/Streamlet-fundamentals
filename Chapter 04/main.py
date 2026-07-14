import streamlit as st 

import pandas as pd

st.title('Handling Data')

file=st.file_uploader('Upload Your CSV file :',type=['csv'])

if file:
    df=pd.read_csv(file)
    st.subheader('Data Preview')
    st.dataframe(df)

if file:
    st.subheader('Summary Stats')
    st.write(df.describe)

if file:
    education=df['education'].unique()
    sel_educ=st.selectbox("select the Ecduaction ",education)
    filter_df=df[df['education']==sel_educ]
    st.dataframe(filter_df)