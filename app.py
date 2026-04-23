import streamlit as st
import sqlite3
import hashlib
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parent))
from utils.theme import apply_theme

st.set_page_config(page_title="PhysiX AI Tutor", page_icon="⚛️", layout="wide")
apply_theme()

# ---------- DB ----------
conn = sqlite3.connect("data/progress.db", check_same_thread=False)
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS users(
username TEXT PRIMARY KEY,
password TEXT
)
""")
conn.commit()

def h(x):
    return hashlib.sha256(x.encode()).hexdigest()


# ---------- LOGIN SCREEN ----------
if "user" not in st.session_state:

    st.markdown("""
    <style>
    [data-testid="stSidebar"] {display:none;}
    .block-container {max-width:500px; padding-top:3rem;}
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 style='text-align:center;'>⚛️ PhysiX AI Tutor</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center;color:#e7c65c;'>Student Login</h2>", unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["Login", "Register"])

    with tab1:
        u = st.text_input("Username")
        p = st.text_input("Password", type="password")

        if st.button("Login", use_container_width=True):
            c.execute("SELECT * FROM users WHERE username=? AND password=?", (u, h(p)))
            row = c.fetchone()

            if row:
                st.session_state["user"] = u
                st.rerun()
            else:
                st.error("Invalid login")

    with tab2:
        nu = st.text_input("Create Username")
        np = st.text_input("Create Password", type="password")

        if st.button("Register", use_container_width=True):
            try:
                c.execute("INSERT INTO users VALUES (?,?)", (nu, h(np)))
                conn.commit()
                st.success("Account created")
            except:
                st.error("Username exists")

    st.stop()


# ---------- MAIN APP ----------
st.title("⚛️ PhysiX AI Tutor")
st.success("Welcome " + st.session_state["user"])
st.write("Use sidebar tools now.")