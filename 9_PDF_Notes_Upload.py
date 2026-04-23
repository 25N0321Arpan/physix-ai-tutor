import streamlit as st
from pypdf import PdfReader
from utils.ai import route_prompt

st.title('PDF Notes Upload')
mode=st.selectbox('Backend',['Gemini'])
file=st.file_uploader('Upload PDF',type=['pdf'])
if file:
    reader=PdfReader(file)
    text=' '.join([p.extract_text() or '' for p in reader.pages[:5]])
    st.success('PDF loaded')
    if st.button('Summarize Notes'):
        st.write(route_prompt(mode,'Summarize these physics notes: '+text[:6000]))
    if st.button('Make MCQs'):
        st.write(route_prompt(mode,'Create 10 MCQs from these notes: '+text[:6000]))