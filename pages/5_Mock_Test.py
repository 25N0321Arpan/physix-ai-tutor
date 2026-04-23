import streamlit as st
import pandas as pd

st.title("📘 Mock Test")

exam = st.selectbox("Choose Exam", ["JAM", "JEST", "GATE", "CSIR NET"])
num = st.slider("Number of Questions", 5, 20, 5)

files = {
    "JAM": "data/questions/jam.csv",
    "JEST": "data/questions/jest.csv",
    "GATE": "data/questions/gate.csv",
    "CSIR NET": "data/questions/csir_net.csv"
}

if st.button("Start Test"):

    df = pd.read_csv(files[exam])

    if len(df) < num:
        num = len(df)

    test = df.sample(n=num).reset_index(drop=True)

    score = 0
    answers = []

    for i, row in test.iterrows():

        st.subheader(f"Q{i+1}. {row['question']}")

        choice = st.radio(
            "Choose",
            ["A", "B", "C", "D"],
            key=i
        )

        answers.append((choice, row["answer"]))

    if st.button("Submit Test"):

        for chosen, correct in answers:
            if chosen == correct:
                score += 1

        st.success(f"Your Score: {score}/{num}")