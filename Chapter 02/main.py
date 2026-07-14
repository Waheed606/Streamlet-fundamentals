import streamlit as st 

st.title('Shooting Game')

if st.button('fire'):
    st.success('the men is kill')

restart=st.checkbox('Restart the game')

if restart:
    st.write('The is successfully restarted')
    st.reload()


game_mode=st.radio('Select the game mode : ',['Shooting','car driving'])


st.write(f'Selected game mode is {game_mode}')

level=st.slider('select the game level',0,10)

st.write(f'The game level is {level}')

partner=st.number_input('Select the number of partner:',min_value=2,max_value=8,step=1)

st.write(f'There are {partner} in the game')

name=st.text_input('Enter Your profile name')

if name :
    st.write(f'The profile name is : {name}')
    st.success('The profile name is updated')