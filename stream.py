import streamlit as st
import pandas as pd

st.write("""
# just an app!
Hello world
""")

df = pd.read_csv("data.csv")
st.bar_chart(df)

date = st.date_input("Pick a date")