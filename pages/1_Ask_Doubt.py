import streamlit as st
from utils.ai import route_prompt

st.title("Ask Physics Doubt")

mode = st.selectbox(
    "Tutor Mode",
    ["Concept", "Exam", "Derivation", "Hint", "Viva"]
)

q = st.text_area("Enter Question")

if st.button("Solve"):
    st.write(route_prompt(mode, q))