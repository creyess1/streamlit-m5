import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



st.title('Reto Módulo 5')
st.header("Alumno: Carlos Reyes Sánchez")
st.write("Elaboración de una aplicación WEB")

DATE_COLUMN = 'released'
DATA_URL = ('Employees.csv')

import codecs

@st.cache
def load_data(nrows):
    doc = codecs.open('Employees.csv','rU','latin1')
    data = pd.read_csv(doc, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    return data

def load_data_byid(id):
    data = pd.read_csv(DATA_URL)
    filtered_data_byid = data[data["Employee_ID"].str.contains(id)]
    return filtered_data_byid

def load_data_byciudad(ciudad):
    data = pd.read_csv(DATA_URL)
    filtered_data_byciudad = data[data["Hometown"].str.contains(ciudad)]
    return filtered_data_byciudad

def load_data_byunit(unit):
    data = pd.read_csv(DATA_URL)
    filtered_data_byunit = data[data["Unit"].str.contains(unit)]
    return filtered_data_byunit


data_load_state = st.text('Loading data...')
data = load_data(500)
data_load_state.text("Done! (using st.cache)")


#Checkbox en barra lateral para mostrar/ocultar el database
if st.sidebar.checkbox('Mostrar todos los filmes'):
    st.subheader('Todos los filmes')
    st.write(data)

#Buscador por ID en barra lateral
myid = st.sidebar.text_input("Buscar por Id : ")
if (myid):
    filterbyid = load_data_byid(myid)
    count_row = filterbyid.shape[0] #gives numer of rows
    st.write(f"Total names: {count_row}")
    st.dataframe(filterbyid)


#Buscador por Ciudad en barra lateral
myciudad = st.sidebar.text_input("Buscar por Ciudad : ")
if (myciudad):
    filterbyciudad = load_data_byciudad(myciudad)
    count_row = filterbyciudad.shape[0] #gives numer of rows
    st.write(f"Total names: {count_row}")
    st.dataframe(filterbyciudad)


#Buscador por Unit en barra lateral
myunit = st.sidebar.text_input("Buscar por Unit : ")
if (myunit):
    filterbyunit = load_data_byunit(myunit)
    count_row = filterbyunit.shape[0] #gives numer of rows
    st.write(f"Total names: {count_row}")
    st.dataframe(filterbyunit)


#Histograma de edades
fig, ax = plt.subplots()
ax.hist(data.Age, bins=[0,20,40,60,80,100])
st.header("Histograma de los empleados agrupados por edad")
st.pyplot(fig)


#Crear una gráfica de frecuencias para las unidades funcionales (Unit) para conocer cuántos empleados hay en cada Unidad 
fig, ax = plt.subplots()
ax.hist(data.Unit)
st.header("Histograma de los empleados agrupados por Unit")
st.pyplot(fig)


#Analizar los datos con una gráfica que nos permita visualizar las ciudades (Hometown) que tienen el mayor índice de deserción 
fig2, ax2 = plt.subplots()
y_pos = data['Hometown']
x_pos = data['Attrition_rate']
ax2.barh(y_pos, x_pos)
ax2.set_ylabel("Ciudades")
ax2.set_xlabel("Índice de deserción")
st.header("Índice de deserción por ciudades")
st.pyplot(fig2)


#Analizar la información con una gráfica que permita visualizar la edad y la tasa de deserción
st.markdown("___")
fig3, ax3 = plt.subplots()
ax3.scatter(data.Age, data.Attrition_rate)
ax3.set_xlabel("Edad")
ax3.set_ylabel("Tasa de Diserción")
st.header("Grafica de Dispersión de la edad y tasa de deserción")
st.pyplot(fig3)



#Analizar con una gráfica que determine la relación entre el tiempo de servicio y la tasa de deserción 
st.markdown("___")
fig3, ax3 = plt.subplots()
ax3.scatter(data.Time_of_service, data.Attrition_rate)
ax3.set_xlabel("Tiempo de servicio")
ax3.set_ylabel("Tasa de Diserción")
st.header("Grafica de Dispersión entre tiempo de servicio y tasa de deserción")
st.pyplot(fig3)




