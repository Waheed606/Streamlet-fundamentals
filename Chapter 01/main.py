import streamlit as st 

st.title("Code with Waheed")
st.subheader('Welcome with streamlit')
st.text('Welcome to the first interactive app')
st.write("It is easy way to create the app")

color =st.selectbox('choose your favourite color : ',['Blue','Red','Pink','Black'])

st.write(f'You choose {color} color .Exellent choice')

st.success('Your select the best color')