import streamlit as st
import pandas as pd

st.write("""
# cool app!
Hello world
""")

df = pd.read_csv("data.csv")
st.bar_chart(df)

