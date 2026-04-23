import streamlit as st
import sqlite3
import hashlib
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parent))
from utils.theme import apply_theme

# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(
    page_title="PhysiX AI Tutor",
    page_icon="⚛️",
    layout="wide"
)

apply_theme()

# ---------------------------
# Database
# ---------------------------
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


# ---------------------------
# Login Screen
# ---------------------------
if "user" not in st.session_state:

    # Hide sidebar + toolbar on login page
    st.markdown("""
    <style>
    [data-testid="stSidebar"] {display:none;}

    header[data-testid="stHeader"] {
        display:none;
    }

    div[data-testid="stToolbar"] {
        display:none;
    }

    #MainMenu {
        visibility:hidden;
    }

    footer {
        visibility:hidden;
    }

    .block-container {
        max-width:500px;
        padding-top:3rem;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown(
        "<h1 style='text-align:center;'>⚛️ PhysiX AI Tutor</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<h2 style='text-align:center;color:#e7c65c;'>Student Login</h2>",
        unsafe_allow_html=True
    )

    tab1, tab2 = st.tabs(["Login", "Register"])

    # ---------------------------
    # Login Tab
    # ---------------------------
    with tab1:
        u = st.text_input("Username")
        p = st.text_input("Password", type="password")

        if st.button("Login", use_container_width=True):
            c.execute(
                "SELECT * FROM users WHERE username=? AND password=?",
                (u, h(p))
            )
            row = c.fetchone()

            if row:
                st.session_state["user"] = u
                st.rerun()
            else:
                st.error("Invalid Login")

    # ---------------------------
    # Register Tab
    # ---------------------------
    with tab2:
        nu = st.text_input("Create Username")
        np = st.text_input("Create Password", type="password")

        if st.button("Register", use_container_width=True):
            try:
                c.execute(
                    "INSERT INTO users VALUES (?,?)",
                    (nu, h(np))
                )
                conn.commit()
                st.success("Account created")
            except:
                st.error("Username already exists")

    st.stop()


# ---------------------------
# Role Based UI
# ---------------------------
user = st.session_state["user"]

# Students: hide sidebar + top toolbar
if user != "admin":
    st.markdown("""
    <style>
    [data-testid="stSidebar"] {display:none;}

    header[data-testid="stHeader"] {
        display:none;
    }

    div[data-testid="stToolbar"] {
        display:none;
    }

    #MainMenu {
        visibility:hidden;
    }

    footer {
        visibility:hidden;
    }
    </style>
    """, unsafe_allow_html=True)


# ---------------------------
# Main App
# ---------------------------
st.title("⚛️ PhysiX AI Tutor")
st.success("Welcome " + user)

# ---------------------------
# Admin Only
# ---------------------------
if user == "arpan":
    st.markdown("---")
    if st.button("🔒 Open Admin Dashboard"):
        st.switch_page("pages/admin_panel.py")
    st.markdown("""
        <style>
        [data-testid="stSidebar"] {display:none;}

        header[data-testid="stHeader"] {
            display:none;
        }

        div[data-testid="stToolbar"] {
            display:none;
        }

        #MainMenu {
            visibility:hidden;
        }

        footer {
            visibility:hidden;
        }
        </style>
        """, unsafe_allow_html=True)


# ---------------------------
# Dashboard Metrics
# ---------------------------
st.markdown("---")
st.subheader("📊 Student Dashboard")

col1, col2, col3 = st.columns(3)

col1.metric("Tests Taken", "12")
col2.metric("Average Score", "78%")
col3.metric("Study Streak", "5 Days")

# ---------------------------
# Progress
# ---------------------------
st.markdown("---")
st.subheader("📈 Progress Overview")

progress_data = {
    "Week 1": 55,
    "Week 2": 68,
    "Week 3": 72,
    "Week 4": 81
}

st.line_chart(progress_data)


# ---------------------------
# Quick Actions
# ---------------------------
st.markdown("---")
st.subheader("⚡ Quick Start")

c1, c2, c3 = st.columns(3)

with c1:
    if st.button("🧠 Ask Doubt"):
        st.switch_page("pages/1_Ask_Doubt.py")

with c2:
    if st.button("📘 Mock Test"):
        st.switch_page("pages/5_Mock_Test.py")

with c3:
    if st.button("📂 Upload Notes"):
        st.switch_page("pages/9_PDF_Notes_Upload.py")

# ---------------------------
# Logout
# ---------------------------
st.markdown("---")

if st.button("Logout"):
    del st.session_state["user"]
    st.rerun()