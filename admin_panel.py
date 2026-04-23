import streamlit as st
import pandas as pd
import sqlite3
import os
from pypdf import PdfReader

st.set_page_config(page_title="Admin Dashboard", page_icon="🔒", layout="wide")

# ---------------------------
# Security
# ---------------------------
if "user" not in st.session_state or st.session_state["user"] != "admin":
    st.error("Access denied")
    st.stop()

# ---------------------------
# DB
# ---------------------------
conn = sqlite3.connect("data/progress.db", check_same_thread=False)

# ---------------------------
# UI Style
# ---------------------------
st.markdown("""
<style>
.stApp {background:#0b0b0b; color:white;}
h1,h2,h3 {color:#e7c65c;}
div[data-testid="metric-container"] {
background:#151515;
border-radius:16px;
padding:15px;
border:1px solid #c9a22744;
}
</style>
""", unsafe_allow_html=True)

st.title("🔒 PhysiX Admin Dashboard")

# ---------------------------
# Metrics
# ---------------------------
c1, c2, c3 = st.columns(3)

try:
    users = pd.read_sql("SELECT * FROM users", conn)
    total_users = len(users)
except:
    total_users = 0

try:
    progress = pd.read_sql("SELECT * FROM progress", conn)
    total_attempts = len(progress)
except:
    total_attempts = 0

question_files = len(os.listdir("data/questions")) if os.path.exists("data/questions") else 0

c1.metric("Users", total_users)
c2.metric("Saved Progress", total_attempts)
c3.metric("Question Files", question_files)

st.markdown("---")

# ---------------------------
# Tabs
# ---------------------------
tab1, tab2, tab3, tab4 = st.tabs([
    "📂 Upload PYQ PDF",
    "👥 Users",
    "📈 Analytics",
    "🗂 Question Files"
])

# ---------------------------
# Upload PDF
# ---------------------------
with tab1:

    st.subheader("Upload Previous Year Question PDF")

    exam = st.selectbox("Choose Exam", ["JAM", "JEST", "GATE"])

    uploaded = st.file_uploader("Upload PDF", type=["pdf"])

    if uploaded:

        reader = PdfReader(uploaded)

        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"

        st.success("PDF loaded")

        st.text_area("Preview", text[:5000], height=250)

        if st.button("Save PDF Text"):

            os.makedirs("data/questions", exist_ok=True)

            path = f"data/questions/{exam}_raw.txt"

            with open(path, "w", encoding="utf-8") as f:
                f.write(text)

            st.success("Saved successfully")

# ---------------------------
# Users
# ---------------------------
with tab2:

    st.subheader("Registered Users")

    try:
        st.dataframe(users, use_container_width=True)
    except:
        st.info("No users found")

# ---------------------------
# Analytics
# ---------------------------
with tab3:

    st.subheader("Student Performance")

    try:
        st.dataframe(progress, use_container_width=True)

        st.bar_chart(progress["score"])
    except:
        st.info("No analytics data")

# ---------------------------
# Files
# ---------------------------
with tab4:

    st.subheader("Uploaded Question Files")

    if os.path.exists("data/questions"):
        files = os.listdir("data/questions")

        for f in files:
            st.write("📄", f)
    else:
        st.info("No files uploaded")

# ---------------------------
# Logout
# ---------------------------
st.markdown("---")

if st.button("Logout Admin"):
    del st.session_state["user"]
    st.rerun()