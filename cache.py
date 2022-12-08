import streamlit as st
import pandas as pd

st.title("Streamlit con caché")
DATA_URL = ("dataset.csv")

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL,nrows=nrows)
    return data

#Función para poner un mensaje:
data_load_state = st.text("Cargando datos ...")

#Mandamos a llamar la función
data = load_data(1000)

data_load_state.text("Listo")

st.dataframe(data)