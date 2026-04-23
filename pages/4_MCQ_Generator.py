import streamlit as st
from utils.ai import route_prompt
st.title('MCQ Generator')
mode=st.selectbox('Backend',['AI Tutor'])
sub=st.text_input('Subject')
num=st.slider('Questions',5,20,10)
if st.button('Generate MCQs'):
    st.write(route_prompt(mode,f'Generate {num} MCQs with answers on {sub}.'))