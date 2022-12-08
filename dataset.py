import pandas as pd
import streamlit as st

names_link = '/workspaces/streamlit-m5/dataset.csv'
names_data = pd.read_csv(names_link)

st.title("Lectura de dataframe con Streamlit")
st.dataframe(names_data)