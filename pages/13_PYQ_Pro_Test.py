import streamlit as st
import pandas as pd
import time

st.title("⏱ PYQ Pro Mock Test")

df = pd.read_csv("data/questions/jam.csv")

num = st.slider("Questions", 5, 20, 5)
mins = st.slider("Time (minutes)", 1, 60, 10)

if "start" not in st.session_state:
    if st.button("Start Test"):
        st.session_state.start = time.time()
        st.session_state.test = df.sample(n=num).reset_index(drop=True)
        st.rerun()

if "test" in st.session_state:

    elapsed = int(time.time() - st.session_state.start)
    left = mins*60 - elapsed

    st.warning(f"Time Left: {left//60}:{left%60:02d}")

    if left <= 0:
        st.error("Time Over")

    score = 0

    for i,row in st.session_state.test.iterrows():

        st.subheader(f"Q{i+1}. {row['question']}")

        ans = st.radio(
            "Choose",
            ["A","B","C","D"],
            key=i
        )

        if ans == row["answer"]:
            score += 1

    if st.button("Submit Test") or left <= 0:

        st.success(f"Score: {score}/{num}")

        del st.session_state["test"]
        del st.session_state["start"]