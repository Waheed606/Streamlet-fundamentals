from datetime import date
import streamlit as st 



st.title('Age Calculating App')

current_year=2026

name=st.text_input('Enter Your name')
user_age=st.date_input('Enter Your Date of Birth')


user_year=date.year(user_age)

age=current_year-user_age

if age:
    st.success(f'The Age of {name} is {age}')