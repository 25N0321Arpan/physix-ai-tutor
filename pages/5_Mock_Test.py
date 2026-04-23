import streamlit as st
from utils.ai import route_prompt
st.title('Mock Test')
mode=st.selectbox('Backend',['AI Tutor'])
exam=st.selectbox('Exam',['JAM','JEST','GATE'])
if st.button('Create Mock Test'):
    st.write(route_prompt(mode,f'Create a 15-question {exam} physics mock test with answers.'))