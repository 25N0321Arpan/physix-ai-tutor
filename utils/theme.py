import streamlit as st


def apply_theme():
    st.markdown("""
    <style>
    .stApp {background:#0b0b0b; color:#f5f5f5;}
    section[data-testid='stSidebar'] {background:#111111;}
    .stButton>button {background:#c9a227; color:black; border:none; border-radius:12px; font-weight:700;}
    .stTextInput input, .stTextArea textarea {border-radius:10px;}
    div[data-testid='metric-container'] {background:#151515; padding:14px; border-radius:16px; border:1px solid #c9a22733;}
    h1,h2,h3 {color:#e7c65c;}
    </style>
    """, unsafe_allow_html=True)