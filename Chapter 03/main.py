import streamlit as st 


st.title('Best Programming Language')

co1,co2=st.columns(2)

with co1:
    st.subheader('Python')
    vote1=st.button('vote 1')

with co2:
    st.subheader('JavaScripts')
    vote2=st.button("vote 2")

if vote1: 
    st.success('Thanks for Python Voting')
elif vote2:
    st.success('Thanks for JavaScripts Voting')


name=st.sidebar.text_input('Enter the name')

prg=st.sidebar.selectbox('Select the language :',['Python','JavaScript'])

if prg:
    st.write(f'Welcome to {name} and your best programming language is {prg}')

with st.expander('What is the career path'):
    st.write("""
    1.Full stack development \n
    2.ML Engineer \n
    3.Data Secience \n
    """)

st.markdown('## keep on bulding the Skill')