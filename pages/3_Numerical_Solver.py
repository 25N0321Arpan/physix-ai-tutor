import streamlit as st
from utils.ai import route_prompt
st.title('Numerical Solver')
mode=st.selectbox('Backend',['AI Tutor'])
q=st.text_area('Paste numerical problem')
if st.button('Solve Numerical'):
    st.write(route_prompt(mode,'Solve stepwise and show formulas: '+q))