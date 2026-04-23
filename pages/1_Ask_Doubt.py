import streamlit as st
from utils.ai import route_prompt
from utils.theme import apply_theme
apply_theme()
st.title('Ask Doubt')
mode=st.selectbox('Backend',['AI Tutor'])
q=st.text_area('Enter your physics question')
if st.button('Solve'):
    st.write(route_prompt(mode,'Answer clearly with steps: '+q))