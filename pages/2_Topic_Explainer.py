import streamlit as st
from utils.ai import route_prompt
st.title('Topic Explainer')
mode=st.selectbox('Backend',['AI Tutor'])
topic=st.text_input('Topic')
level=st.selectbox('Level',['Beginner','Intermediate','Advanced'])
if st.button('Explain'):
    st.write(route_prompt(mode,f'Explain {topic} for {level} level physics student.'))