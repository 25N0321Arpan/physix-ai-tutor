import streamlit as st
from utils.ai import route_prompt
st.title('Study Planner')
mode=st.selectbox('Backend',['AI Tutor'])
exam=st.selectbox('Exam',['JAM','JEST','GATE'])
days=st.number_input('Days left',1,365,90)
if st.button('Generate Plan'):
    st.write(route_prompt(mode,f'Make a {days}-day study plan for {exam} physics exam.'))