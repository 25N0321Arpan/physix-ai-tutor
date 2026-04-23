import streamlit as st
import sqlite3

st.title('Save Progress')
conn=sqlite3.connect('data/progress.db')
c=conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS progress(name TEXT, topic TEXT, score INTEGER)')
name=st.text_input('Student Name')
topic=st.text_input('Topic Completed')
score=st.number_input('Mock Score',0,100,0)
if st.button('Save'):
    c.execute('INSERT INTO progress VALUES (?,?,?)',(name,topic,score))
    conn.commit()
    st.success('Progress saved')
if st.button('Show Records'):
    for row in c.execute('SELECT * FROM progress'):
        st.write(row)